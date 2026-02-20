"""Base page class for all page objects."""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from components.header_component import HeaderComponent
from utils.types import Locators


class BasePage:
    """Base page class for all page objects."""
    header_root_locator: Locators = (By.XPATH, "//header[@role='banner']")
    _snack_bar_message = (By.CSS_SELECTOR, "div[matsnackbarlabel]")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.header: HeaderComponent = HeaderComponent(
            self.driver.find_element(*self.header_root_locator))

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

    def is_visible(self, locator: Locators) -> bool:
        """Check if the element specified by the locator is visible."""
        try:
            self.find(locator)
            return True
        except NoSuchElementException:
            return False

    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
        return self

    def go_back(self):
        """Go back to the previous page."""
        self.driver.back()

    def get_alert_msg(self):
        """Gets text from snack bar message."""
        try:
            snack_bar_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self._snack_bar_message)
            )
            return snack_bar_element.text.strip()
        except TimeoutException:
            return ""

    def wait_for_snack_bar_disappear(self):
        """Waits for snack bar message to disappear in order to click on the header."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self._snack_bar_message)
            )
        except TimeoutException:
            pass
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self._snack_bar_message)
        )
