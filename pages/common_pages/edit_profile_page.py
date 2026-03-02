"""Edit profile page."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.types import Locators


class ProfileEditPage(BasePage):
    """Page object for the Edit Profile page."""

    page_root_locator: Locators = (By.CLASS_NAME, "edit_prof-wrap")
    page_title_locator: Locators = (By.TAG_NAME, "h2")
    cancel_button_locator = (By.CSS_SELECTOR, ".buttons .secondary-global-button")
    save_button_locator = (By.CSS_SELECTOR, ".buttons .primary-global-button")


    def click_cancel(self):
        """Click Cancel button."""
        self.cancel_button.click()

    def click_save(self):
        """Click Save button."""
        self.save_button.click()

    def is_save_enabled(self) -> bool:
        """Check if Save button is enabled."""
        return self.save_button.is_enabled()
