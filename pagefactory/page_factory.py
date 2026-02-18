"""
Page factory module
"""
from typing import Generic, TypeVar, Any, cast
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

T = TypeVar("T")

LocatorTuple = tuple[str, str, type[Any]]


class BaseFactory(Generic[T]):
    """
    Base class implementing lazy loading and dynamic resolution of web elements and components.
    """
    locators: dict[str, LocatorTuple] = {}

    def __init__(self, driver: WebDriver, root: WebDriver | WebElement | None = None) -> None:
        self.driver = driver
        self.root = root or driver

        self._lazy_resolvers: dict[str, Any] = {}

        self._bind_locators()

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
        for name, (by, value, el_type) in all_locators.items():
            self._lazy_resolvers[name] = \
                lambda b=by, v=value, t=el_type: self._resolve_element(b, v, t)

    def _resolve_element(self, by: str, value: str, element_type: type[T]) -> T:
        """
        Explicitly locates and instantiates a WebElement or a Component.
        """
        try:
            # Search is triggered ONLY at the moment of physical attribute access
            web_element = self.root.find_element(by, value)
        except NoSuchElementException as e:
            raise NoSuchElementException(
                f"Lazy resolution failed: Element via '{by}'='{value}' not found."
            ) from e

        # Local import to break circular dependency with BaseComponent
        from components.base_component import BaseComponent # pylint: disable=C0415

        # Handle Nested Components (objects inheriting from BaseComponent)
        if issubclass(element_type, BaseComponent):
            return cast(T, element_type(self.driver, root=web_element))

        # Handle raw Selenium WebElements
        if element_type is WebElement:
            return cast(T, web_element)

        # Handle custom element wrappers
        return cast(T, element_type(web_element))

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

    def wait_and_click(self, attr_name: str, timeout: int = 10) -> None:
        """
        Universal click method with lazy waiting and 'Auto-Healing' for stale elements.
        """

        def _clickable_condition():
            try:
                # Triggers dynamic resolution (__getattr__)
                element = getattr(self, attr_name)

                # Determine if we are clicking a component root or a raw WebElement
                target = getattr(element, "root", element)

                if target.is_displayed() and target.is_enabled():
                    return target
                return False

            except (NoSuchElementException, StaleElementReferenceException):
                # Suppress exceptions during wait loop to allow for retry/DOM update
                return False

        # Loop until the element is ready for interaction
        ready_element = WebDriverWait(self.driver, timeout).until(
            _clickable_condition,
            message=f"Element '{attr_name}' was not clickable after {timeout} seconds"
        )
        ready_element.click()

    def resolve_list(self, locator_name: str) -> list[Any]:
        """
        Locates all elements matching the locator and returns a list of objects or components.
        """
        by, value, el_type = self.locators[locator_name]
        elements = self.root.find_elements(by, value)

        from components.base_component import BaseComponent # pylint: disable=C0415

        # Instantiate each element in the list as a component if applicable
        if issubclass(el_type, BaseComponent):
            return [el_type(self.driver, root=el) for el in elements]
        return elements
