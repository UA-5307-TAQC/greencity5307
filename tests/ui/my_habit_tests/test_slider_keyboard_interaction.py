"""test slider keyboard interaction"""
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.base_page import BasePage
from pages.my_habit_page import MyHabitPage
from pages.one_habit_page import OneHabitPage


def test_slider_keyboard_interaction(driver: WebDriver):
    """Check slider working"""
    base_page = BasePage(driver)

    sign_in_component = base_page.header.click_sign_in_link()

    sign_in_component.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

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
