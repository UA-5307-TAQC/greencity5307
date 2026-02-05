"""Base page class for all page objects."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.header_component import HeaderComponent
from utils.types import Locators


class BasePage:
    """Base page class for all page objects."""
    header_root_locator: Locators = (By.XPATH, "//header[@role='banner']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        header_root = self.driver.find_element(*self.header_root_locator)
        self.header:HeaderComponent = HeaderComponent(header_root)

    def navigate_to(self, url: str):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Get the title of the current page."""
        return self.driver.title
