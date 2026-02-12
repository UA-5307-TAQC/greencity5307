"""Create update event page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.event_header_component import EventHeaderComponent
from components.chip_set_component import ChipSetComponent
from components.event_type_component import EventTypeComponent
from components.quill_editor_component import QuillEditorComponent
from components.data_time_component import DateTimeComponent
from components.location_component import LocationComponent

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

        description_root = self.driver.find_element(
            By.CSS_SELECTOR,
            "quill-editor[formcontrolname='description']"
        )
        self.description = QuillEditorComponent(description_root)

        date_time_root = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.date-time"
        )
        self.date_time = DateTimeComponent(date_time_root)

        date_location_root = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.date-location-container"
        )
        self.date_location = LocationComponent(date_location_root)
