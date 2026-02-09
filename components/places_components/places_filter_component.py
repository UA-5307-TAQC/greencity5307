"""Places filter component"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class PlacesFilterComponent(BaseComponent):
    """Places filter component class"""
    # filter_locator: Locators = (By.CSS_SELECTOR,
    #                             ".places-filter>.filter")
    filter_button_locator: Locators = (By.CSS_SELECTOR,
                                       ".tag-button.ng-star-inserted")
    more_options_button_locator: Locators = (By.CSS_SELECTOR,
                                             ".mat-mdc-menu-trigger.custom-chip.global-tag")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.filter_buttons = self.root.find_elements(
            *self.filter_button_locator)
        self.more_options_button = self.root.find_element(
            *self.more_options_button_locator)

    def toggle_more_options_modal(self):
        """Toggle more_options modal"""
        self.more_options_button.click()
