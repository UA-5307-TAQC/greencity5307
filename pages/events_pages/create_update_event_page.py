"""Create update event page."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.events_components.event_header_component import EventHeaderComponent
from components.events_components.chip_set_component import ChipSetComponent
from components.events_components.event_type_component import EventTypeComponent
from components.events_components.quill_editor_component import QuillEditorComponent
from components.events_components.data_time_component import DateTimeComponent
from components.events_components.location_component import LocationComponent
from components.events_components.link_component import OnlineLinkComponent


class CreateEventPage(BasePage):
    """Create event page."""

    locators = {
        "header_root": (By.CSS_SELECTOR, "div.header-container", EventHeaderComponent),
        "chip_set": (By.CSS_SELECTOR, "div.mdc-evolution-chip-set__chips", ChipSetComponent),
        "event_type": (By.CSS_SELECTOR, "div.event-type-wrapper", EventTypeComponent),
        "description": (By.CSS_SELECTOR, "quill-editor[formcontrolname='description']",
                        QuillEditorComponent),
        "date_time": (By.CSS_SELECTOR, "div.date-time", DateTimeComponent),
        "date_location": (By.CSS_SELECTOR, "div.date-location-container", LocationComponent),

        "preview_button": (By.CSS_SELECTOR, "div.submit-container button.secondary-global-button"),
        "publish_button": (By.CSS_SELECTOR, "div.submit-container button.primary-global-button"),
        "cancel_button": (By.CSS_SELECTOR, "div.submit-container button.tertiary-global-button"),
        "online_link_block": (By.XPATH,
            "//div[contains(@class,'d-flex') and .//input[@formcontrolname='onlineLink']]",
            OnlineLinkComponent),
    }

    header_root: EventHeaderComponent
    chip_set: ChipSetComponent
    event_type: EventTypeComponent
    description: QuillEditorComponent
    date_time: DateTimeComponent
    date_location: LocationComponent
    online_link_block: OnlineLinkComponent

    preview_button: WebElement
    publish_button: WebElement
    cancel_button: WebElement

    @allure.step("Click Preview button")
    def click_preview(self):
        """Click Preview button."""
        self.preview_button.click()

    @allure.step("Click Publish button")
    def click_publish(self):
        """Click Publish button."""
        self.publish_button.click()

    @allure.step("Click Cancel button")
    def click_cancel(self):
        """Click Cancel button."""
        self.cancel_button.click()
