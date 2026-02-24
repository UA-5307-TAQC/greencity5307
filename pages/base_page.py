"""Base page class for all page objects."""
from typing import Any

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.header_component import HeaderComponent
from utils.page_factory import Factory
from utils.types import Locators


class BasePage(Factory[Any]):
    """Base page class for all page objects."""

    locators = {
        "header": (By.XPATH, "//header[@role='banner']", HeaderComponent)
    }

    title_locator: tuple

    def __init__(self, driver: WebDriver):
        """Initialize the component"""
        super().__init__(driver)

        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url: str):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Get the title of the current page."""
        return self.driver.title

    def find(self, locator: Locators):
        """Find single element with wait"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator: Locators) -> bool:
        """Check if the element specified by the locator is visible."""
        try:
            self.find(locator)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def is_page_opened(self) -> bool:
        """Check if the page is opened by verifying the visibility of the title element."""
        if not hasattr(self, "title_locator"):
            raise NotImplementedError("Page must define title_locator")
        return self.is_visible(self.title_locator)
