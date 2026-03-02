"""This module contains the MyNewsPage class."""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.types import Locators

from components.news_components.my_news.news_filter_component import NewsFilterComponent
from components.news_components.my_news.user_news_card_component import UserNewsCardComponent


class MyNewsPage(BasePage):
    """Page object for 'My Space -> My News' tab."""

    add_news_btn_locator: Locators = (By.ID, "create-button-news")
    filter_container_locator: Locators = (By.CSS_SELECTOR, "div.ul-eco-buttons")
    news_cards_locator: Locators = (By.CSS_SELECTOR, "ul.news-list app-one-news")
    empty_state_text_locator: Locators = (By.CSS_SELECTOR, ".description_title h2")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.add_news_btn: WebElement = self.driver.find_element(*self.add_news_btn_locator)


    def click_add_news(self):
        """Clicks the 'Add News' button."""
        self.add_news_btn.click()

    def get_filters(self) -> NewsFilterComponent:
        """Returns the News Filter component."""
        root = self.driver.find_element(*self.filter_container_locator)
        return NewsFilterComponent(root)

    def get_news_cards(self) -> List[UserNewsCardComponent]:
        """Returns a list of news card components."""
        card_elements = self.driver.find_elements(*self.news_cards_locator)
        return [UserNewsCardComponent(card) for card in card_elements]

    def get_empty_state_text(self) -> str:
        """Returns text of the empty state message if visible (e.g. 'Hi Eco Friend')."""
        return self.driver.find_element(*self.empty_state_text_locator).text
