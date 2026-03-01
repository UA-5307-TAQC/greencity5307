"""Base page class for all page objects."""
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from components.common_components.layout_components.header_component import HeaderComponent
from utils.page_factory import Factory
from utils.custom_web_element import CustomWebElement
from utils.types import Locators


class BasePage(Factory):
    """Base page class for all page objects."""
    locators = {
        "header": (By.XPATH, "//header[@role='banner']", HeaderComponent),
        "_snack_bar_message": (By.CSS_SELECTOR, "div[matsnackbarlabel]")
    }

    title_locator: tuple
    header: HeaderComponent
    _snack_bar_message: CustomWebElement


    def navigate_to(self, url: str):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Get the title of the current page."""
        return self.driver.title

    def find(self, locator: Locators):
        """Find single element with wait"""
        return self.get_wait().until(EC.visibility_of_element_located(locator))

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

    def get_alert_msg(self) -> str:
        """Gets text from snack bar message."""
        try:
            locator_tuple = (By.CSS_SELECTOR, "div[matsnackbarlabel]")

            alert_element = self.get_wait().until(
                EC.visibility_of_element_located(locator_tuple)
            )
            return alert_element.text.strip()

        except TimeoutException:
            return ""

    def wait_for_snack_bar_disappear(self) -> None:
        """Waits for snack bar message to disappear in order to click on the header."""
        locator_tuple = (By.CSS_SELECTOR, "div[matsnackbarlabel]")

        try:
            self.get_wait().until(
                EC.visibility_of_element_located(locator_tuple)
            )
        except TimeoutException:
            pass
        self.get_wait().until(
            EC.invisibility_of_element_located(locator_tuple)
        )

    def refresh_page(self):
        """Refreshes the current page in the browser."""
        self.driver.refresh()

    def go_back(self):
        """Goes to the previous page of the browser."""
        self.driver.back()
