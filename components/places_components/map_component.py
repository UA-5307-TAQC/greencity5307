"""Map component."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class MapComponent(BaseComponent):
    """Component class for the Map component."""

    locators = {
        "map": (By.CSS_SELECTOR, ".google-map.ng-star-inserted"),
    }

    map: CustomWebElement
