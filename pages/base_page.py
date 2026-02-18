"""Base page class for all page objects."""
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.header_component import HeaderComponent
from pagefactory.page_factory import BaseFactory


class BasePage(BaseFactory[Any]):
    """Base page class for all page objects."""

    locators = {
        "header": (By.XPATH, "//header[@role='banner']", HeaderComponent)
    }

    header: HeaderComponent

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, root=driver)
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url: str):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Get the title of the current page."""
        return self.driver.title

    def find(self, locator):
        """Find single element with wait"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Find list of elements"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Click on the element specified by the locator."""
        self.find(locator).click()
