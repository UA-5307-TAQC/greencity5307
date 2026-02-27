"""Mutual Habits component."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class MutualHabitsComponent(BaseComponent):
    """ Component for Mutual Habits Page. """

    empty_text: Locators = (By.CSS_SELECTOR, "div > div.img-absent.ng-star-inserted > h3")
    habits_card: Locators = (By.CSS_SELECTOR, "div > div.gallery.ng-star-inserted")


    def get_empty_state_text(self) -> str:
        """Get empty message text."""
        try:
            return self.root.find_element(*self.empty_text).text
        except NoSuchElementException:
            return ""


    def get_habits_count(self) -> int:
        """Return the number of habits found."""
        if self.is_empty_state_displayed():
            return 0

        habits = self.root.find_elements(*self.habits_card)
        return len(habits)

    def is_empty_state_displayed(self) -> bool:
        """Check if the empty message is displayed."""
        try:
            text = self.root.find_element(*self.empty_text)
            return text.is_displayed()
        except NoSuchElementException:
            return False
