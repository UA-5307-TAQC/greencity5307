"""This module contains the CreateUpdateEcoNewsPage class,
which represents the create_update_eco_news page of a website."""

from selenium.webdriver.common.by import By
from components.create_update_eco_news_component import CreateUpdateNewsTitleComponent, \
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

    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.is_visible(self.page_title_locator)

    def get_title_component(self) -> CreateUpdateNewsTitleComponent:
        """Get the title of the page."""
        return CreateUpdateNewsTitleComponent(self.find(self.page_title_locator))

    def get_form(self) -> CreateUpdateEcoNewsFormComponent:
        """Get the form of the page."""
        return CreateUpdateEcoNewsFormComponent(self.find(self.form_locator))

    def click_submit(self):
        """Click the submit button."""
        self.click(self.submit_button)

    def click_cancel(self):
        """Click the cancel button."""
        self.click(self.cancel_button)
