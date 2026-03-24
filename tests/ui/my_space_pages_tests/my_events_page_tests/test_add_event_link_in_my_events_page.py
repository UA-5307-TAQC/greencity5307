"""Module for test like one news page like one news"""
from time import sleep

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage


@allure.title("Test add event link in my events page")
def test_add_event_link_in_my_events_page(driver_with_login: WebDriver):
    """Test like one news page like one news"""

    my_habits_page = MyHabitPage(driver_with_login)
    # check language
    my_events_page = my_habits_page.click_my_events_tab()
    # link to CreateEventPage
    create_event_page = my_events_page.navigate_to_add_event_page()
    # check if linked correctly
    assert (create_event_page.page_header.text == "Створити подію"
            or create_event_page.page_header.text == "Create event")
