"""tests for slider boundaries"""

from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.base_page import BasePage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.habit_pages.one_habit_page import OneHabitPage


def test_slider_keyboard_interaction(driver: WebDriver):
    """Check slider working"""
    base_page = BasePage(driver)

    sign_in_component = base_page.header.click_sign_in_link()

    sign_in_component.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    page = MyHabitPage(driver)

    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()

    one_habit_page = OneHabitPage(driver)

    slider_value = one_habit_page.get_slider_value()
    one_habit_page.move_slider_right(3)
    assert one_habit_page.get_slider_value() == slider_value + 3, f"Slider should display {slider_value + 3}"

    slider_value = one_habit_page.get_slider_value()
    one_habit_page.move_slider_left(1)
    assert one_habit_page.get_slider_value() == slider_value - 1, f"Slider should display {slider_value - 1}"

    one_habit_page.move_slider_left(57)
    assert one_habit_page.get_slider_value() == 7, "Slider should not go below 7"

    one_habit_page.move_slider_right(57)
    assert one_habit_page.get_slider_value() == 56, "Slider should not exceed 56"
