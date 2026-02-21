"""This module contains the CreateUpdateEcoNewsPage class,
which represents the create_update_eco_news page of a website."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.create_update_eco_news_component import CreateUpdateEcoNewsTitleComponent, \
    CreateUpdateEcoNewsFormComponent
from pages.base_page import BasePage
from utils.types import Locators


class CreateUpdateEcoNewsPage(BasePage):
    """Page object for the create_update_eco_news page."""
    page_title_locator: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]")
    form_locator: Locators = (By.XPATH, "//*[@id='main-content']//form")

    cancel_button: Locators = (By.XPATH, "//button[contains(text(),'Cancel')]")
    preview_button: Locators = (By.XPATH, "//button[contains(text(),'Preview')]")
    submit_button: Locators = (By.XPATH, "//button[contains(text(),'Submit')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.title_component = CreateUpdateEcoNewsTitleComponent(self.find(self.page_title_locator))
        self.form_component = CreateUpdateEcoNewsFormComponent(self.find(self.form_locator))

    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.is_visible(self.page_title_locator)

    def get_title_component(self) -> CreateUpdateEcoNewsTitleComponent:
        """Get the title component of the page."""
        return self.title_component

    @allure.step("Getting the form component")
    def get_form(self) -> CreateUpdateEcoNewsFormComponent:
        """Get the form of the page."""
        return self.form_component

    @allure.step("Clicking the submit button")
    def click_submit(self):
        """Click the submit button."""
        self.click(self.submit_button)

    def click_cancel(self):
        """Click the cancel button."""
        self.click(self.cancel_button)

    @allure.step("Clicking the submit button is disabled")
    def is_submit_button_disabled(self) -> bool:
        """Check if the submit button is disabled."""
        return self.find(self.submit_button).is_enabled()
