"""Base component class for web elements using Selenium WebDriver."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from utils.page_factory import Factory


class BaseComponent(Factory):
    """Base component class for web elements using Selenium WebDriver."""

    def __init__(self, driver: WebDriver, root: WebElement):
        super().__init__(driver)
        self.root = root

    def is_displayed(self) -> bool:
        """Check if the component is displayed."""
        return self.root.is_displayed()

    def is_enabled(self) -> bool:
        """Check if the component is enabled."""
        return self.root.is_enabled()

    def click(self):
        """Click on the element specified by the locator."""
        self.root.click()

    def get_text(self) -> str:
        """Get text from the element specified by the locator."""
        return self.root.text.strip()
