"""This module contains the EventPage class,which represents the event page of a website.
 It inherits from the BasePage class and provides specific locators and methods
for interacting with the event page elements."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.places_page import PlacesPage
from utils.types import Locators


class EventPage(BasePage):
    """Page object for the event page."""

    main_header_locator: Locators = (By.CSS_SELECTOR, ".top-header>.main-header")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)

    @allure.step("Navigating to the Places page")
    def go_to_places(self) -> "PlacesPage":
        """Navigate to the Eco News page."""
        self.header.click_places_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("places")
        )
        return PlacesPage(self.driver)
