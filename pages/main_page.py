"""This module contains the MainPage class, which represents the main page of the application.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the main page elements."""
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.common_components.auth_components.signin_modal_component import SignInComponent
from pages.about_us_page import AboutUsPage
from pages.base_page import BasePage
from pages.eco_news_page import EcoNewsPage

class MainPage(BasePage):
    """Page object for the main page."""
    Locators = Tuple[str, str]
    there_are_locator: Locators = (By.CSS_SELECTOR, "#stats > h2")
    header_locator: Locators = (By.CSS_SELECTOR, "#stats > h1")
    main_header_locator: Locators = (By.CSS_SELECTOR, ".cont >.main-header")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.there_are: WebElement = self.driver.find_element(*self.there_are_locator)

    def sign_in(self) -> "SignInComponent":
        """Click the Sign-in link in the header and return an instance of the SignInComponent."""
        return self.header.click_sign_in_link()

    @allure.step("Navigating to the Eco News page")
    def go_to_eco_news(self) -> "EcoNewsPage":
        """Navigate to the Eco News page."""
        self.header.click_new_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("news")
        )
        return EcoNewsPage(self.driver)

    @allure.step("Navigating to the About Us page")
    def go_to_about_us(self) -> AboutUsPage:
        """Navigate to the About Us page."""
        self.header.click_about_us_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)
