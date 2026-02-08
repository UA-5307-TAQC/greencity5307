"""Base component class for web elements using Selenium WebDriver."""

from selenium.webdriver.remote.webelement import WebElement


class BaseComponent:
    """Base component class for web elements using Selenium WebDriver."""

    def __init__(self, root: WebElement):
        self.root = root

    def is_displayed(self) -> bool:
        """Check if the component is displayed."""
        return self.root.is_displayed()

    def is_enabled(self) -> bool:
        """Check if the component is enabled."""
        return self.root.is_enabled()

    def find_element(self, locator: tuple) -> WebElement:
        """Find element by locator."""
        return self.root.find_element(*locator)

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Find list of elements inside this component."""
        return self.root.find_elements(*locator)

    def click(self, locator: tuple):
        self.find_element(locator).click()

    def input_text(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find_element(locator).text.strip()