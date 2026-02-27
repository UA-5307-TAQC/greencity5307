"""This module contains the CreateUpdateEcoNewsPage class,
which represents the create_update_eco_news page of a website."""
import allure
from selenium.webdriver.common.by import By

from components.news_components.create_update_eco_news_component \
    import CreateUpdateEcoNewsTitleComponent, \
    CreateUpdateEcoNewsFormComponent
from pages.base_page import BasePage


class CreateUpdateEcoNewsPage(BasePage):
    """Page object for the create_update_eco_news page."""
    locators = {
        "page_title": (By.XPATH, "//*[@id='main-content']/div/div[1]"),
        "form": (By.XPATH, "//*[@id='main-content']//form"),

        "cancel_button": (By.XPATH, "//button[contains(text(),'Cancel')]"),
        "preview_button": (By.XPATH, "//button[contains(text(),'Preview')]"),
        "submit_button": (By.XPATH, "//button[contains(text(),'Submit')]")
    }
    page_title: CreateUpdateEcoNewsTitleComponent
    cancel_button: CreateUpdateEcoNewsFormComponent
    preview_button: CreateUpdateEcoNewsFormComponent
    submit_button: CreateUpdateEcoNewsFormComponent

    @allure.step("Check if CreateUpdateEcoNewsPage is opened")
    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.page_title.is_displayed()

    @allure.step("Getting the form component")
    def get_form(self) -> CreateUpdateEcoNewsFormComponent:
        """Get the form component."""
        element = self.driver.find_element(*self.locators["form"])
        return CreateUpdateEcoNewsFormComponent(element)

    @allure.step("Clicking the submit button")
    def click_submit(self):
        """Click the submit button."""
        self.submit_button.wait_and_click()

    def click_cancel(self):
        """Click the cancel button."""
        self.cancel_button.wait_and_click()

    @allure.step("Clicking the submit button is disabled")
    def is_submit_button_disabled(self) -> bool:
        """Check if the submit button is disabled."""
        return self.submit_button.is_enabled()
