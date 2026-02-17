"""This module contains the AllHabitPage class."""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators

from components.all_habits.create_habit_button_component import CreateHabitButtonComponent
from components.all_habits.habit_filter_component import HabitFilterComponent
from components.all_habits.change_view_component import ChangeViewComponent
from components.all_habits.habit_card_component import HabitCardComponent
from components.all_habits.bread_crumbs_component import BreadCrumbsComponent


class AllHabitPage(BasePage):
    """Page object for the 'All habits' page."""

    main_header_locator: Locators = (By.XPATH, "//h1[contains(text(),\
     'All habits') or contains(text(), 'Всі звички')]")
    filter_container_locator: Locators = (By.TAG_NAME, "app-filter-search")
    change_view_container_locator: Locators = (By.TAG_NAME, "app-change-view-button")
    habit_cards_locator: Locators = (By.CSS_SELECTOR, "app-habits-gallery-view > div,\
     app-habits-list-view > div")
    breadcrumbs_container_locator: Locators = (By.CLASS_NAME, "breadcrumbs-container")
    create_habit_button_locator: Locators = (By.CSS_SELECTOR, "div.habit-header > button")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)


    def get_create_habit_button(self) -> CreateHabitButtonComponent:
        """Returns the Create Habit button component."""

        create_habit_button = self.driver.find_element(*self.create_habit_button_locator)
        return CreateHabitButtonComponent(create_habit_button)


    def get_filters(self) -> HabitFilterComponent:
        """Returns the Filters component."""
        root = self.driver.find_element(*self.filter_container_locator)
        return HabitFilterComponent(root)

    def get_view_switcher(self) -> ChangeViewComponent:
        """Returns the View Switcher component."""
        root = self.driver.find_element(*self.change_view_container_locator)
        return ChangeViewComponent(root)

    def get_breadcrumbs(self) -> BreadCrumbsComponent:
        """Returns the Breadcrumbs component."""
        root = self.driver.find_element(*self.breadcrumbs_container_locator)
        return BreadCrumbsComponent(root)

    def get_all_habit_cards(self) -> List[HabitCardComponent]:
        """Returns a list of habit cards."""
        elements = self.driver.find_elements(*self.habit_cards_locator)
        return [HabitCardComponent(el) for el in elements]
