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
