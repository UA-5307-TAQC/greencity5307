"""This module contains the SavedEventsPage class for the saved events page."""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.events_components.events_filter_component import EventsFilterComponent
from components.common_components.change_view_component import ChangeViewComponent
from components.events_components.event_card_component import EventCardComponent

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract


class SavedEventsPage(SavedAbstract):
    """Page object for the saved events page."""

    locators = {
        "events_filter": (By.CSS_SELECTOR, ".filter-container", EventsFilterComponent),
        "change_view_style": (By.CSS_SELECTOR, ".change-view", ChangeViewComponent),
        "all_cards": (By.CSS_SELECTOR, "mat-card.event-list-item", List[EventCardComponent]),
        "_loader": (By.CSS_SELECTOR, "app-spinner")
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

    def is_event_card_present(self, name: str) -> bool:
        """Check if the event card is present on the page by the event's name"""
        formatted_pattern = self._event_card_pattern.format(name)
        found_cards = self.driver.find_elements(By.XPATH, formatted_pattern)
        return len(found_cards) > 0

    def has_any_events(self):
        """Checks if the saved events list has any events."""
        event_cards_locator = self.locators["all_cards"][:2]
        all_event_cards = self.driver.find_elements(*event_cards_locator)
        return len(all_event_cards) > 0

    def is_loaded(self):
        """Check if the SavedEventsPage is loaded by loading spinner."""
        try:
            self.get_wait(5).until(
                EC.invisibility_of_element_located(self.locators["_loader"][:2])
            )
            return True
        except TimeoutException:
            return False

    def get_first_event_card(self):
        """Gets the first card from the event cards list."""
        return self.all_cards[0]
