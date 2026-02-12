"""Page object for the Places page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from components.places_components.add_place_modal_component import AddPlaceModalComponent
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
