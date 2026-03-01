"""This module contains the SavedEventsPage class for the saved events page."""
from typing import List

from selenium.webdriver.common.by import By

from components.events_components.events_filter_component import EventsFilterComponent
from components.common_components.change_view_component import ChangeViewComponent
from components.events_components.event_card_component import EventCardComponent

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract


class SavedEventsPage(SavedAbstract):
    """Page object for the saved events page."""

    locators = {
        "events_filter": (By.CSS_SELECTOR, ".filter-container", EventsFilterComponent),
        "change_view_style": (By.CSS_SELECTOR, ".change-view", ChangeViewComponent),
        "all_cards": (By.CSS_SELECTOR, "mat-card.event-list-item", List[EventCardComponent])
    }

    events_filter: EventsFilterComponent
    change_view_style: ChangeViewComponent
    all_cards: List[EventCardComponent]

    _event_card_pattern = ("//mat-card[contains(@class, 'event-list-item')]"
                           "[.//p[contains(@class, 'event-name') and normalize-space()='{}']]")

    def get_event_card_by_name(self, name: str):
        """Finds an event card element by the event's name."""
        formatted_pattern = self._event_card_pattern.format(name)
        event_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        return EventCardComponent(event_card_element)

    def has_any_events(self):
        """Checks if the saved events list has any events."""
        event_cards_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                         "mat-card.event-list-item")
        return len(event_cards_elements) > 0
