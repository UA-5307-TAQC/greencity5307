"""PlacesSearchbarComponent component."""

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class PlacesSearchbarComponent(BaseComponent):
    """PlacesSearchbarComponent component class."""
    search_icon_locator: Locators = (By.CSS_SELECTOR,
                                     ".search-elements > .search-icon")
    searchbar_locator: Locators = (By.CSS_SELECTOR,
                                   ".form-control.search-write")
    choose_location_locator: Locators = (By.CSS_SELECTOR,
                                         ".mat-mdc-input-element"
                                         ".choose-location-input"
                                         ".cdk-text-field-autofill-monitored")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.search_icon = self.root.find_element(
            *self.search_icon_locator)
        self.searchbar = self.root.find_element(*self.searchbar_locator)
        self.choose_location = self.root.find_element(
            *self.choose_location_locator)

    def click_search_icon(self):
        """Click search_icon button."""
        self.search_icon.click()

    def search_place(self, value: str):
        """Search place."""
        self.searchbar.send_keys(value, Keys.ENTER)

    def choose_location_method(self, value: str):
        """Choose location."""
        self.searchbar.send_keys(value, Keys.ENTER)
