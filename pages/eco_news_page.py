"""This module contains the EcoNewsPage class, which represents the Eco News page of the website."""
from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


from components.button_create_new_component import CreateNewButtonComponent
from components.news_components.news_card_base_component import \
    NewsCardBaseComponent
from pages.base_page import BasePage
from pages.create_update_eco_news_page import CreateUpdateEcoNewsPage


class EcoNewsPage(BasePage):
    """Page object for the Eco News page."""
    Locators = Tuple[str, str]

    main_header_locator: Locators = (By.CSS_SELECTOR, ".cont >.main-header")
    button_create_news_locator: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/a")
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

    def click_create_button(self):
        """Click the create news link in the page and return an instance of the
        CreateUpdateEcoNews."""
        self.get_new_button_component().click_create_new_button()
        return CreateUpdateEcoNewsPage(self.driver)
