"""Page object for the Places page."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.places_components.add_place_modal_component import AddPlaceModalComponent
from pages.about_us_page import AboutUsPage
from pages.base_page import BasePage
from utils.types import Locators


class PlacesPage(BasePage):
    """Page object for the Eco News page."""
    add_place_button_locator: Locators = (By.CSS_SELECTOR,
                                          ".secondary-global-button.m-btn.ng-star-inserted")
    add_place_modal_locator: Locators = (By.CSS_SELECTOR, ".ng-star-inserted > .form-container")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.add_place_button: WebElement = self.driver.find_element(*self.add_place_button_locator)

    def open_add_place_modal(self) -> AddPlaceModalComponent:
        """Open add place modal component."""
        self.add_place_button.click()
        return AddPlaceModalComponent(self.driver.find_element(*self.add_place_modal_locator))

    @allure.step("Navigating to the AboutUs page")
    def go_to_about_us(self) -> "AboutUsPage":
        """Navigate to the Eco News page."""
        self.header.click_about_us_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)
