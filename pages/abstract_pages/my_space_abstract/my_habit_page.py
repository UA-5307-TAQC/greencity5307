"""
Habit page
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.user_habit_card_component import UserHabitCardComponent
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from utils.custom_web_element import CustomWebElement


class MyHabitPage(MySpaceAbstractPage):
    """ Habit page """
    locators = {
        "first_habit_card": (By.XPATH, "(//app-one-habit)[1]", UserHabitCardComponent),
        "habit_cards_list": (By.TAG_NAME, "app-one-habit", UserHabitCardComponent),

        "add_new_habit_button": (By.XPATH, ".//span[text()='Add New Habit']/.."),
        "my_habits_tab": (By.XPATH, ".//div[contains(@class, 'my-habits-tab')]")
    }

    first_habit_card: UserHabitCardComponent
    add_new_habit_button: CustomWebElement
    my_habits_tab: CustomWebElement

    @allure.step("Get habit card component")
    def get_habit_card(self) -> UserHabitCardComponent:
        """Get the first habit card component"""
        return self.first_habit_card

    @allure.step("Get all habit cards")
    def get_all_habit_cards(self) -> list[UserHabitCardComponent]:
        """Отримує список усіх карток звичок на сторінці"""
        return self.resolve_list("habit_cards_list")

    def wait_page_loaded(self):
        """Wait for the My Habit page to load."""
        locator = self.locators["add_new_habit_button"][:2]
        self.get_wait().until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Clicking Add New Habit button on the My Habit page")
    def click_add_new_habit_button(self):
        """Click on Add New Habit button."""
        from pages.habit_pages.all_habits_page import AllHabitPage  # pylint: disable=import-outside-toplevel
        self.add_new_habit_button.wait_and_click()
        return AllHabitPage(self.driver)

    @allure.step("Navigating to the About Us page from My Habit page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        from pages.common_pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel

        self.header.click_about_us_link()
        self.get_wait().until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)

    @allure.step("Checking if My Habit page is opened")
    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        try:
            return self.my_habits_tab.is_displayed()
        except Exception:  # pylint: disable=broad-exception-caught
            return False

    @allure.step("Checking if My Habit page is loaded")
    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded by verifying the visibility of the title and friend tabs."""
        self.get_wait().until(
            EC.visibility_of(self.add_new_habit_button)
        )
        return True
