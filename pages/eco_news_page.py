"""This module contains the EcoNewsPage class, which represents the Eco News page of the website."""
import allure



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from components.button_create_new_component import CreateNewButtonComponent
from components.news_components.news_card_base_component import \
    NewsCardBaseComponent
from pages.base_page import BasePage
from pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
from pages.event_page import EventPage
from utils.types import Locators


class EcoNewsPage(BasePage):
    """Page object for the Eco News page."""

    main_header_locator: Locators = (By.CSS_SELECTOR, ".cont >.main-header")
    button_create_news_locator: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/a")
    title_locator: Locators = (By.CSS_SELECTOR, "#main-content > div > div:nth-child(1) > div > h1")
    news_cards_locator: Locators = (By.CSS_SELECTOR,
                                    ".ng-star-inserted .gallery-view-li-active")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header: WebElement = self.driver.find_element(
            *self.main_header_locator)
        self.news_cards: list[NewsCardBaseComponent] = [
            NewsCardBaseComponent(element)
            for element
            in self.driver.find_elements(*self.news_cards_locator)
        ]

    def get_new_button_component(self):
        """Get the create news button component."""
        return CreateNewButtonComponent(self.find(self.button_create_news_locator))

    @allure.step("Clicking the create news button")
    def click_create_button(self):
        """Click the create news link in the page and return an instance of the
        CreateUpdateEcoNews."""
        self.get_new_button_component().click_create_new_button()
        return CreateUpdateEcoNewsPage(self.driver)

    @allure.step("Navigating to the Events page")
    def go_to_events(self) -> "EventPage":
        """Navigate to the Eco News page."""
        self.header.click_event_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("events")
        )
        return EventPage(self.driver)

    @allure.step("Navigating to the About Us page from Eco News page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        from pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        self.header.click_about_us_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)
