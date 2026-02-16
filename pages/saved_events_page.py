"""This module contains the SavedEventsPage class for the saved events page."""
from selenium.webdriver.common.by import By

from pages.saved_abstract import SavedAbstract


class SavedEventsPage(SavedAbstract):
    """Page object for the saved events page."""
    events_filter_locator = (By.CSS_SELECTOR, ".filter-container")
    _event_card_pattern = ("//mat-card[contains(@class, 'event-list-item')]"
                           "[.//p[contains(@class, 'event-name') and normalize-space()='{}']]")
    all_cards_locator = (By.CSS_SELECTOR, "mat-card.event-list-item")
    change_view_style_locator = (By.CSS_SELECTOR, ".change-view")

    @property
    def filters(self):
        """Returns the events filter component."""
        events_filter_element = self.driver.find_element(*self.events_filter_locator)
        from components.events_filter_component import EventsFilterComponent  # pylint: disable=import-outside-toplevel
        return EventsFilterComponent(events_filter_element)

    def get_event_card_by_name(self, name: str):
        """Finds an event card element by the event's name."""
        formatted_pattern = self._event_card_pattern.format(name)
        event_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        from components.event_card_component import EventCardComponent  # pylint: disable=import-outside-toplevel
        return EventCardComponent(event_card_element)

    def get_all_event_cards(self):
        """Finds all event card elements on the page."""
        event_card_elements = self.driver.find_elements(*self.all_cards_locator)
        from components.event_card_component import EventCardComponent  # pylint: disable=import-outside-toplevel
        return [EventCardComponent(element) for element in event_card_elements]

    def change_view_style_buttons(self):
        """Returns the buttons for changing the view style."""
        change_view_style_element = self.driver.find_element(*self.change_view_style_locator)
        from components.change_view_component import ChangeViewComponent  # pylint: disable=import-outside-toplevel
        return ChangeViewComponent(change_view_style_element)

    def has_any_events(self):
        """Checks if the saved events list has any events."""
        event_cards_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                         "mat-card.event-list-item")
        return len(event_cards_elements) > 0
