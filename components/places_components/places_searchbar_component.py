"""PlacesSearchbarComponent component."""

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class PlacesSearchbarComponent(BaseComponent):
    """PlacesSearchbarComponent component class."""
    locators = {
        "search_icon": (By.CSS_SELECTOR,
                        ".search-elements > .search-icon"),
        "searchbar": (By.CSS_SELECTOR,
                      ".form-control.search-write"),
        "choose_location": (By.CSS_SELECTOR,
                            ".mat-mdc-input-element"
                            ".choose-location-input"
                            ".cdk-text-field-autofill-monitored"),
    }

    def click_search_icon(self):
        """Click search_icon button."""
        self.search_icon.click()

    def search_place(self, value: str):
        """Search place."""
        self.searchbar.send_keys(value, Keys.ENTER)

    def choose_location_method(self, value: str):
        """Choose location."""
        self.choose_location.send_keys(value, Keys.ENTER)
