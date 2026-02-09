"""Edit profile page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.personal_info_component import PersonalInfoComponent
from utils.types import Locators


class ProfileEditPage(BasePage):
    """Page object for the Edit Profile page with only PersonalInfoComponent."""

    page_root_locator: Locators = (By.CLASS_NAME, "edit_prof-wrap")
    page_title_locator: Locators = (By.TAG_NAME, "h2")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.page_title: WebElement = self.driver.find_element(*self.page_title_locator)

        page_root = self.driver.find_element(*self.page_root_locator)

        self.personal_info: PersonalInfoComponent = PersonalInfoComponent(page_root)

    def get_page_header(self) -> str:
        """Return page title text."""
        return self.page_title.text

    def get_personal_info_component(self) -> PersonalInfoComponent:
        """Return PersonalInfoComponent instance."""
        return self.personal_info
