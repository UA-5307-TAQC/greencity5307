"""This module contains the MainPage class, which represents the main page of the application.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the main page elements."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage, WebDriver
from utils.types import Locators


class UBSCourierPage(BasePage):
    """Page object for the UBSCourier page."""
    there_are_locator: Locators = (By.CSS_SELECTOR, "#stats > h2")
    section_text_locator: Locators = (By.CSS_SELECTOR, "section > h2:first-child")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.there_are: WebElement = self.driver.find_element(*self.there_are_locator)
        self.section_text: WebElement = self.driver.find_element(*self.section_text_locator)

    @allure.step("Navigating to the Main page")
    def go_to_main_page(self) -> "MainPage":
        """Navigate to the Main page."""
        from pages.main_page import MainPage # pylint: disable=import-outside-toplevel
        self.header.click_main_page_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("greenCity")
        )
        return MainPage(self.driver)
