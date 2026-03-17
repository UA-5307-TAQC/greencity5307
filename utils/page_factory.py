"""
Page factory module
"""
import threading
from typing import Generic, TypeVar, Any, Union, get_origin, get_args, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from data.config import Config
from utils.custom_web_element import CustomWebElement

T = TypeVar("T")

LocatorTuple = tuple[str, str] | tuple[str, str, type[Any]]

_STALE_ELEMENT_RETRIES = 3


class Factory(Generic[T]):
    """
    Base class implementing lazy loading and dynamic resolution of web elements and components.

    Thread safety: each instance owns its own ``_lock`` so that parallel workers
    (pytest-xdist) that happen to share a Factory subclass do not race on the
    internal resolver dictionary.  The resolvers themselves are stateless lambdas,
    so the lock only guards the one-time ``_bind_locators`` call.
    """
    locators: dict[str, LocatorTuple] = {}
    driver: WebDriver
    root: WebElement | None

    def __init__(self, context: Union[WebDriver, WebElement]):
        if isinstance(context, WebDriver):
            self.driver = context
            self.root = None
        elif isinstance(context, WebElement):
            self.driver = context.parent
            self.root = context
        else:
            raise TypeError(
                f"{type(self).__name__} expects a WebDriver or WebElement, "
                f"got {type(context).__name__!r} instead."
            )
        self._lock = threading.Lock()
        self._lazy_resolvers: dict[str, Any] = {}
        self._bind_locators()

    def __getattr__(self, name: str) -> Any:
        """
        Lazy loading mechanism. Invoked only when the requested attribute
        does not exist in the instance's __dict__.
        """
        # Guard against infinite recursion during __init__ before _lazy_resolvers is set
        if name == "_lazy_resolvers":
            raise AttributeError(name)
        resolvers = self.__dict__.get("_lazy_resolvers", {})
        if name in resolvers:
            # Note: Caching with setattr is omitted to prevent StaleElementReferenceException
            # in dynamic environments (Angular/React).
            return resolvers[name]()

        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def get_wait(self, timeout: int = Config.EXPLICITLY_WAIT) -> WebDriverWait:
        """Returns a WebDriverWait instance for the current driver."""
        return WebDriverWait(self.driver, timeout)

    def _bind_locators(self) -> None:
        """
        Iterates through 'locators' dictionaries across the entire class hierarchy (MRO)
        and creates resolvers. This ensures child classes inherit parent locators
        (e.g., from BasePage) without manual merging.
        """
        with self._lock:
            all_locators: dict[str, LocatorTuple] = {}

            # Traverse the inheritance tree from oldest parent to current class
            for cls in reversed(self.__class__.__mro__):
                if hasattr(cls, 'locators') and isinstance(cls.locators, dict):
                    all_locators.update(cls.locators)

            # Map each locator name to a lazy-loading lambda
            for name, locator_data in all_locators.items():
                by = locator_data[0]
                value = locator_data[1]
                multiple = False
                el_type: type[Any] = CustomWebElement
                if len(locator_data) > 2:
                    multiple = get_origin(locator_data[2]) is list
                    el_type = locator_data[2] if not multiple else get_args(locator_data[2])[0]

                if multiple:
                    self._lazy_resolvers[name] = \
                        lambda b=by, v=value, t=el_type: self._resolve_list(b, v, t)
                else:
                    self._lazy_resolvers[name] = \
                        lambda b=by, v=value, t=el_type: self._resolve_element(b, v, t)

    def _resolve_element(self, by: str, value: str, element_type: type[T]) -> T:
        """
        Explicitly locates and instantiates a WebElement or a Component.

        Retries up to ``_STALE_ELEMENT_RETRIES`` times on
        ``StaleElementReferenceException`` to handle Angular/React re-renders.
        """
        for attempt in range(_STALE_ELEMENT_RETRIES):
            try:
                if self.root:
                    web_element = self.root.find_element(by, value)
                else:
                    web_element = self.driver.find_element(by, value)
                return element_type(web_element)
            except StaleElementReferenceException as exc:
                if attempt == _STALE_ELEMENT_RETRIES - 1:
                    raise StaleElementReferenceException(
                        f"Element via '{by}'='{value}' was stale after "
                        f"{_STALE_ELEMENT_RETRIES} retries."
                    ) from exc
            except NoSuchElementException as exc:
                raise NoSuchElementException(
                    f"Lazy resolution failed: Element via '{by}'='{value}' not found."
                ) from exc
        # Unreachable: all paths either return or raise inside the loop.
        raise AssertionError("unreachable")  # pragma: no cover

    def _resolve_list(self, by: str, value: str, element_type: type[T]) -> List[T]:
        """
        Locates all elements matching the locator and returns a list of objects or components.

        Retries up to ``_STALE_ELEMENT_RETRIES`` times on
        ``StaleElementReferenceException``.
        """
        for attempt in range(_STALE_ELEMENT_RETRIES):
            try:
                if self.root:
                    web_elements = self.root.find_elements(by, value)
                else:
                    web_elements = self.driver.find_elements(by, value)
                return [element_type(element) for element in web_elements]
            except StaleElementReferenceException as exc:
                if attempt == _STALE_ELEMENT_RETRIES - 1:
                    raise StaleElementReferenceException(
                        f"Elements via '{by}'='{value}' were stale after "
                        f"{_STALE_ELEMENT_RETRIES} retries."
                    ) from exc
        # Unreachable: all paths either return or raise inside the loop.
        raise AssertionError("unreachable")  # pragma: no cover

    def resolve_list(self, locator_name: str) -> List[Any]:
        """
        Public convenience method to resolve a named locator as a list.

        Allows page objects and components to call ``self.resolve_list("key")``
        without accessing private underscore methods directly.
        """
        if locator_name not in self._lazy_resolvers:
            raise KeyError(
                f"Locator '{locator_name}' is not defined in "
                f"{type(self).__name__}.locators"
            )
        locator_data = None
        for cls in reversed(self.__class__.__mro__):
            if hasattr(cls, 'locators') and locator_name in cls.locators:
                locator_data = cls.locators[locator_name]
                break

        if locator_data is None:
            raise KeyError(f"Locator '{locator_name}' not found in class hierarchy.")

        by = locator_data[0]
        value = locator_data[1]
        el_type: type[Any] = CustomWebElement
        if len(locator_data) > 2:
            origin = get_origin(locator_data[2])
            el_type = get_args(locator_data[2])[0] if origin is list else locator_data[2]

        return self._resolve_list(by, value, el_type)
