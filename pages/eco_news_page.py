"""This module contains the EcoNewsPage class, which represents the Eco News page of the website."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from components.news_components.news_card_base_component import \
    NewsCardBaseComponent
from pages.base_page import BasePage
from utils.types import Locators


class EcoNewsPage(BasePage):
    """Page object for the Eco News page."""
    main_header_locator: Locators = (By.CSS_SELECTOR, ".cont >.main-header")
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
