"""Map component."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class MapComponent(BaseComponent):
    """Component class for the Map component."""
    map_locator: Locators = (By.CSS_SELECTOR, ".google-map.ng-star-inserted")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.map = self.root.find_element(*self.map_locator)
