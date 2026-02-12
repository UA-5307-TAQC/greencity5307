"""Create update event page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.event_header_component import EventHeaderComponent
from components.chip_set_component import ChipSetComponent
from components.event_type_component import EventTypeComponent

from utils.types import Locators


class CreateEventPage(BasePage):
    """Create event page."""
    header_root: Locators = (By.CSS_SELECTOR, "div.header-container")
    chip_set_root: Locators = (By.CSS_SELECTOR, "div.mdc-evolution-chip-set__chips")
    event_type_root: Locators = (By.CSS_SELECTOR, "div.event-type-wrapper")

    def __init__(self, driver):
        super().__init__(driver)
        h_root = self.driver.find_element(*self.header_root)
        self.event_header = EventHeaderComponent(h_root)
        chip_root = self.driver.find_element(*self.chip_set_root)
        self.chip_set = ChipSetComponent(chip_root)
        type_root = self.driver.find_element(*self.event_type_root)
        self.event_type = EventTypeComponent(type_root, self.driver)
