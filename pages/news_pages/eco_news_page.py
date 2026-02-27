"""This module contains the EcoNewsPage class, which represents the Eco News page of the website."""
from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.news_components.button_create_new_component import CreateNewButtonComponent
from components.news_components.news_card_base_component import NewsCardBaseComponent
from pages.base_page import BasePage
from pages.events_pages.event_page import EventPage
from pages.news_pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
from utils.custom_web_element import CustomWebElement


class EcoNewsPage(BasePage):
    """Page object for the Eco News page."""

    locators = {
        "main_header_locator": (By.CSS_SELECTOR, ".cont >.main-header"),
        "button_create_news_locator": (By.XPATH, "//*[@id='main-content']/div/div[1]/div/a"),
        "title_locator": (By.XPATH, "//*[@id='main-content']/div/div[1]/div/h1"),
        "news_cards_locator": (By.CSS_SELECTOR,
                               ".ng-star-inserted .gallery-view-li-active",
                               List[NewsCardBaseComponent])
    }

    main_header_locator: CustomWebElement
    button_create_news_locator: CreateNewButtonComponent
    title_locator: CustomWebElement
    news_cards_locator: NewsCardBaseComponent

    def get_button_create_news(self) -> CreateNewButtonComponent:
        """Get the create news button component."""
        element = self.driver.find_element(*self.locators["button_create_news_locator"])
        return CreateNewButtonComponent(element)

    @allure.step("Clicking the create news button")
    def click_create_button(self):
        """Click the create news link in the page and return an instance of the
        CreateUpdateEcoNews."""
        self.get_button_create_news().click_create_new_button()
        return CreateUpdateEcoNewsPage(self.driver)

    @allure.step("Navigating to the Events page")
    def go_to_events(self) -> "EventPage":
        """Navigate to the Eco News page."""
        self.header.click_event_link()
        self.get_wait().until(EC.url_contains("events"))
        return EventPage(self.driver)

    @allure.step("Navigating to the About Us page from Eco News page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        self.header.click_about_us_link()
        self.get_wait().until(EC.url_contains("about"))
        from pages.common_pages.about_us_page \
            import AboutUsPage # pylint: disable=import-outside-toplevel
        return AboutUsPage(self.driver)

    @allure.step("Checking if Eco News page is opened")
    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        self.get_wait().until(EC.url_contains("news"))
        return self.button_create_news_locator.is_displayed()

    @allure.step("Checking if Eco News page is loaded")
    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded."""
        self.get_wait().until(
            EC.visibility_of_element_located(self.locators["button_create_news_locator"])
        )
        return True
