"""Create update event page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.event_header_component import EventHeaderComponent

from utils.types import Locators


class CreateEventPage(BasePage):
    """Create event page."""
    header_root: Locators = (By.CSS_SELECTOR, "div.header-container")

    def __init__(self, driver):
        super().__init__(driver)
        root = self.driver.find_element(*self.header_root)
        self.header = EventHeaderComponent(root)
