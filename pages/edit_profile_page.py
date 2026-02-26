"""Edit profile page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.personal_info_component import PersonalInfoComponent
from components.social_networks_component import SocialNetworksComponent
from components.profile_privacy_component import ProfilePrivacyComponent
from components.email_preferences_component import EmailPreferencesComponent


class ProfileEditPage(BasePage):
    """Page object for the Edit Profile page."""

    # page_root_locator: Locators = (By.CLASS_NAME, "edit_prof-wrap")
    # page_title_locator: Locators = (By.TAG_NAME, "h2")
    # cancel_button_locator = (By.CSS_SELECTOR, ".buttons .secondary-global-button")
    # save_button_locator = (By.CSS_SELECTOR, ".buttons .primary-global-button")

    locators = {
        "page_root": (By.CLASS_NAME, "edit_prof-wrap"),
        "page_title": (By.TAG_NAME, "h2"),
        "cancel_button": (By.CSS_SELECTOR, ".buttons .secondary-global-button"),
        "save_button": (By.CSS_SELECTOR, ".buttons .primary-global-button"),
        "personal_info": (By.CSS_SELECTOR, "div.wrapper", PersonalInfoComponent),
        "social_networks": (By.CLASS_NAME, "edit_prof-wrap", SocialNetworksComponent),
        "profile_privacy": (By.CLASS_NAME, "edit_prof-wrap", ProfilePrivacyComponent),
        "email_preferences": (By.CLASS_NAME, "edit_prof-wrap", EmailPreferencesComponent),
    }

    page_root: WebElement
    page_title: WebElement
    cancel_button: WebElement
    save_button: WebElement
    personal_info: PersonalInfoComponent
    social_networks: SocialNetworksComponent
    profile_privacy: ProfilePrivacyComponent
    email_preferences: EmailPreferencesComponent

    # def __init__(self, driver: WebDriver):
    #     super().__init__(driver)
    #     self.page_title: WebElement = self.driver.find_element(*self.page_title_locator)
    #     page_root = self.driver.find_element(*self.page_root_locator)
    #
    #     self.personal_info: PersonalInfoComponent = PersonalInfoComponent(page_root)
    #     self.social_networks: SocialNetworksComponent = SocialNetworksComponent(page_root)
    #     self.profile_privacy: ProfilePrivacyComponent = ProfilePrivacyComponent(page_root)
    #     self.email_preferences: EmailPreferencesComponent = EmailPreferencesComponent(page_root)
    #     self.cancel_button: WebElement = page_root.find_element(*self.cancel_button_locator)
    #     self.save_button: WebElement = page_root.find_element(*self.save_button_locator)


    @allure.step("Click Cancel button")
    def click_cancel(self):
        """Click Cancel button."""
        self.cancel_button.click()

    @allure.step("Click Save button")
    def click_save(self):
        """Click Save button."""
        self.save_button.click()

    @allure.step("Check if Save button is enabled")
    def is_save_enabled(self) -> bool:
        """Check if Save button is enabled."""
        return self.save_button.is_enabled()
