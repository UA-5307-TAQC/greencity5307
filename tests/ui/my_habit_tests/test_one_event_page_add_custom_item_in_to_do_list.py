"""test add custom item into do_list."""
import time

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.base_page import BasePage
from pages.my_habit_page import MyHabitPage
from pages.one_habit_page import OneHabitPage


@allure.title("Add custom item into to_do_list")
@allure.description("We check possibility add field into to do list of some special habit")
@allure.severity(allure.severity_level.NORMAL)
def test_one_event_page_add_custom_item_in_to_do_list(driver: WebDriver):
    """test add custom item into do_list."""
    base_page = BasePage(driver)

    sign_in_component = base_page.header.click_sign_in_link()

    sign_in_component.sign_in(driver, Config.USER_EMAIL, Config.USER_PASSWORD)

    page = MyHabitPage(driver)

    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()

    one_habit_page = OneHabitPage(driver)

    one_habit_page.press_to_do_list_edit_button()
    time.sleep(5)
    new_item_text = "Eco Bag"
    one_habit_page.add_element_into_list(new_item_text)

    one_habit_page.save_element()

    items = one_habit_page.check_added_element()

    assert new_item_text in items, "Текст не зберігся!"
