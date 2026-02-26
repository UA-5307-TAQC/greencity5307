"""
Page factory module
"""
from typing import Generic, TypeVar, Any, cast
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from utils.custom_web_element import CustomWebElement

T = TypeVar("T")

LocatorTuple = tuple[str, str] | tuple[str, str, type[Any]]


class Factory(Generic[T]):
    """
    Base class implementing lazy loading and dynamic resolution of web elements and components.
    """
    locators: dict[str, LocatorTuple] = {}

    def __init__(self, driver: WebDriver, root: WebDriver | WebElement | None = None) -> None:
        self.driver = driver

        if isinstance(root, WebElement):
            self.root = CustomWebElement(self.driver, root)
        else:
            # Якщо це WebDriver (ціла сторінка), залишаємо як є
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
        for name, locator_data in all_locators.items():
            by = locator_data[0]
            value = locator_data[1]
            el_type = locator_data[2] if len(locator_data) > 2 else WebElement

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

        if issubclass(element_type, BaseComponent):
            return cast(T, element_type(web_element))

        # Handle raw Selenium WebElements -> ТЕПЕР ОБГОРТАЄМО ЇХ
        if element_type is WebElement:
            return cast(T, CustomWebElement(self.driver, web_element))

        # Handle custom element wrappers (якщо ви передали інший кастомний тип)
        try:
            return cast(T, element_type(self.driver, web_element))
        except TypeError:
            # Fallback для простих обгорток, які приймають лише web_element
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

    def resolve_list(self, locator_name: str) -> list[Any]:
        """
        Locates all elements matching the locator and returns a list of objects or components.
        """
        locator_data = self.locators[locator_name]

        by = locator_data[0]
        value = locator_data[1]
        el_type = locator_data[2] if len(locator_data) > 2 else WebElement

        elements = self.root.find_elements(by, value)

        from components.base_component import BaseComponent  # pylint: disable=C0415

        # Instantiate each element in the list as a component if applicable
        if issubclass(el_type, BaseComponent):
            return [el_type(self.driver, root=el) for el in elements]

        # Якщо це стандартний WebElement, обгортаємо кожен елемент списку у CustomWebElement,
        # щоб поведінка була консистентною з _resolve_element
        if el_type is WebElement:
            return [CustomWebElement(self.driver, el) for el in elements]

        # Fallback для інших кастомних обгорток
        try:
            return [el_type(self.driver, el) for el in elements]
        except TypeError:
            return [el_type(el) for el in elements]
