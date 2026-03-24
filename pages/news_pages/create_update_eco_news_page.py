"""This module contains the CreateUpdateEcoNewsPage class,
which represents the create_update_eco_news page of a website."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.news_components.create_update_eco_news_component \
    import CreateUpdateEcoNewsTitleComponent, \
    CreateUpdateEcoNewsFormComponent
from pages.base_page import BasePage


class CreateUpdateEcoNewsPage(BasePage):
    """Page object for the create_update_eco_news page."""
    locators = {
        "page_title": (By.XPATH, "//*[@id='main-content']/div/div[1]/h2"),
        "form": (By.XPATH, "//*[@id='main-content']//form"),

        "cancel_button": (By.XPATH, "//button[contains(text(),'Cancel')]"),
        "preview_button": (By.XPATH, "//button[contains(text(),'Preview')]"),
        "submit_button": (
            By.XPATH,
            "//button[@type='submit' and contains(@class,'primary-global-button')]",
        ),
        "success_message": (
            By.XPATH,
            "//*[contains(text(),'успішно опублікована') "
            "or contains(text(),'successfully published')]",
        )
    }
    page_title: CreateUpdateEcoNewsTitleComponent
    cancel_button: CreateUpdateEcoNewsFormComponent
    preview_button: CreateUpdateEcoNewsFormComponent
    submit_button: CreateUpdateEcoNewsFormComponent

    @allure.step("Wait until CreateUpdateEcoNewsPage is loaded")
    def wait_page_loaded(self) -> None:
        """Wait until the page is loaded."""
        self.get_wait().until(EC.url_contains("create-news"))
        self.get_wait().until(
            EC.visibility_of_element_located(self.locators["form"])
        )

    @allure.step("Check if CreateUpdateEcoNewsPage is opened")
    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.page_title.is_displayed()

    @allure.step("Getting the form component")
    def get_form(self) -> CreateUpdateEcoNewsFormComponent:
        """Get the form component."""
        element = self.driver.find_element(*self.locators["form"])
        return CreateUpdateEcoNewsFormComponent(element)

    @allure.step("Fill mandatory Eco News form")
    def fill_mandatory_news_form(
        self,
        title: str,
        tags: tuple,
        content: str,
    ) -> None:
        """Fill mandatory Eco News fields."""
        self.get_form().fill_mandatory_fields(title, tags, content)

    @allure.step("Clicking the submit button")
    def click_submit(self):
        """Click the submit button."""
        self.submit_button.wait_and_click()

    @allure.step("Wait until Eco News page is opened after submit")
    def wait_redirect_to_news(self):
        """Wait until redirect to Eco News page after submit."""
        self.get_wait().until(
            EC.visibility_of_element_located(self.locators["success_message"])
        )
        self.get_wait().until(EC.url_contains("/news"))

        from pages.news_pages.eco_news_page import EcoNewsPage  # pylint: disable=import-outside-toplevel
        return EcoNewsPage(self.driver)

    def click_cancel(self):
        """Click the cancel button."""
        self.cancel_button.wait_and_click()

    @allure.step("Clicking the submit button is disabled")
    def is_submit_button_disabled(self) -> bool:
        """Check if the submit button is disabled."""
        return self.submit_button.is_enabled()
