"""
Page factory module
"""
from typing import Generic, TypeVar, Any, Union, get_origin, get_args, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from data.config import Config
from utils.custom_web_element import CustomWebElement

T = TypeVar("T")

LocatorTuple = tuple[str, str] | tuple[str, str, type[Any]]


class Factory(Generic[T]):
    """
    Base class implementing lazy loading and dynamic resolution of web elements and components.
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
        self._lazy_resolvers: dict[str, Any] = {}
        self._bind_locators()

    def __getattr__(self, name: str) -> Any:
        """
        Lazy loading mechanism. Invoked only when the requested attribute
        does not exist in the instance's __dict__.
        """
        if name in self._lazy_resolvers:
            # Note: Caching with setattr is omitted to prevent StaleElementReferenceException
            # in dynamic environments (Angular/React).
            return self._lazy_resolvers[name]()

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
        all_locators = {}

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
        """
        try:
            if self.root:
                web_element = self.root.find_element(by, value)
            else:
                web_element = self.driver.find_element(by, value)
        except NoSuchElementException as e:
            raise NoSuchElementException(
                f"Lazy resolution failed: Element via '{by}'='{value}' not found."
            ) from e

        return element_type(web_element)

    def _resolve_list(self, by: str, value: str, element_type: type[T]) -> List[T]:
        """
        Locates all elements matching the locator and returns a list of objects or components.
        """
        try:
            if self.root:
                web_elements = self.root.find_elements(by, value)
            else:
                web_elements = self.driver.find_elements(by, value)
        except NoSuchElementException as e:
            raise NoSuchElementException(
                f"Lazy resolution failed: Elements via '{by}'='{value}' not found."
            ) from e

        return [element_type(element) for element in web_elements]
