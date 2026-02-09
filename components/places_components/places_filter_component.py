"""Places filter component"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class PlacesFilterComponent(BaseComponent):
    """Places filter component class"""
    cancel_button_locator: Locators = (By.CSS_SELECTOR,
                                       ".btn-wrapper > .secondary-global-button")
    add_button_locator: Locators = (By.CSS_SELECTOR,
                                    ".btn-wrapper > .primary-global-button")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.cancel_button = self.root.find_element(
            *self.cancel_button_locator)
        self.add_button = self.root.find_element(*self.add_button_locator)
