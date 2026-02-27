"""Create update event page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.event_header_component import EventHeaderComponent
from components.chip_set_component import ChipSetComponent
from components.event_type_component import EventTypeComponent
from components.quill_editor_component import QuillEditorComponent
from components.data_time_component import DateTimeComponent
from components.location_component import LocationComponent


class CreateEventPage(BasePage):
    """Create event page."""

    locators = {
        "header_root": (By.CSS_SELECTOR, "div.header-container"),
        "chip_set": (By.CSS_SELECTOR, "div.mdc-evolution-chip-set__chips"),
        "event_type": (By.CSS_SELECTOR, "div.event-type-wrapper"),
        "description": (By.CSS_SELECTOR, "quill-editor[formcontrolname='description']"),
        "date_time": (By.CSS_SELECTOR, "div.date-time"),
        "date_location": (By.CSS_SELECTOR, "div.date-location-container"),
    }

    header_root: EventHeaderComponent
    chip_set: ChipSetComponent
    event_type: EventTypeComponent
    description: QuillEditorComponent
    date_time: DateTimeComponent
    date_location: LocationComponent
