"""Edit profile page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.personal_info_component import PersonalInfoComponent
from components.social_networks_component import SocialNetworksComponent
from components.profile_privacy_component import ProfilePrivacyComponent
from components.email_preferences_component import EmailPreferencesComponent
from utils.types import Locators


class ProfileEditPage(BasePage):
    """Page object for the Edit Profile page."""

    page_root_locator: Locators = (By.CLASS_NAME, "edit_prof-wrap")
    page_title_locator: Locators = (By.TAG_NAME, "h2")
    cancel_button_locator = (By.CSS_SELECTOR, ".buttons .secondary-global-button"    )
    save_button_locator = (By.CSS_SELECTOR, ".buttons .primary-global-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page_title: WebElement = self.driver.find_element(*self.page_title_locator)
        page_root = self.driver.find_element(*self.page_root_locator)

        self.personal_info: PersonalInfoComponent = PersonalInfoComponent(page_root)
        self.social_networks: SocialNetworksComponent = SocialNetworksComponent(page_root)
        self.profile_privacy: ProfilePrivacyComponent = ProfilePrivacyComponent(page_root)
        self.email_preferences: EmailPreferencesComponent = EmailPreferencesComponent(page_root)
        self.cancel_button: WebElement = page_root.find_element(*self.cancel_button_locator)
        self.save_button: WebElement = page_root.find_element(*self.save_button_locator)

    def get_page_header(self) -> str:
        """Return page title text."""
        return self.page_title.text

    def get_personal_info_component(self) -> PersonalInfoComponent:
        """Return PersonalInfoComponent instance."""
        return self.personal_info

    def get_social_networks_component(self) -> SocialNetworksComponent:
        """Return SocialNetworksComponent instance."""
        return self.social_networks

    def get_profile_privacy_component(self) -> ProfilePrivacyComponent:
        """Return ProfilePrivacyComponent instance."""
        return self.profile_privacy

    def get_email_preferences_component(self) -> EmailPreferencesComponent:
        """Return EmailPreferencesComponent instance."""
        return self.email_preferences

    def click_cancel(self):
        """Click Cancel button."""
        self.cancel_button.click()

    def click_save(self):
        """Click Save button."""
        self.save_button.click()

    def is_save_enabled(self) -> bool:
        """Check if Save button is enabled."""
        return self.save_button.is_enabled()
