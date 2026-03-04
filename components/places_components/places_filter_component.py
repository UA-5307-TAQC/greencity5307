"""Places filter component"""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class PlacesFilterComponent(BaseComponent):
    """Places filter component class"""
    # filter_locator: Locators = (By.CSS_SELECTOR,
    #                             ".places-filter>.filter")
    locators = {
        "filter_button": (By.CSS_SELECTOR,
                          ".tag-button.ng-star-inserted"),
        "more_options_button": (By.CSS_SELECTOR,
                                ".mat-mdc-menu-trigger.custom-chip.global-tag")
    }

    def toggle_more_options_modal(self):
        """Toggle more_options modal"""
        self.more_options_button.click()
