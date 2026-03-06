"""test slider keyboard interaction"""
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.base_page import BasePage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.habit_pages.one_habit_page import OneHabitPage


def test_slider_keyboard_interaction(driver_with_login):
    """Check slider working"""
    driver = driver_with_login

    page = MyHabitPage(driver)

    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()

    one_habit_page = OneHabitPage(driver)

    initial = one_habit_page.get_slider_value()
    step = 10
    one_habit_page.move_slider_right(step)
    assert one_habit_page.get_slider_value() == initial + step

    one_habit_page.move_slider_left(step)
    assert one_habit_page.get_slider_value() == initial
