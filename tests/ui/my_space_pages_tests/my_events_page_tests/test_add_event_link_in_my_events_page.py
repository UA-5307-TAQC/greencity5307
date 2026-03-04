"""Module for test like one news page like one news"""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage


@allure.title("Test add event link in my events page")
def test_add_event_link_in_my_events_page(driver: WebDriver):
    """Test like one news page like one news"""

    # open main page
    main_page = MainPage(driver)
    # sign in
    sign_in_modal = main_page.header.click_sign_in_link()
    my_habits_page = sign_in_modal.sign_in(Config.USER_EMAIL,
                                           Config.USER_PASSWORD)
    # check language
    my_events_page = my_habits_page.click_my_events_tab()
    # link to CreateEventPage
    create_event_page = my_events_page.navigate_to_add_event_page()
    # check if linked correctly
    assert (create_event_page.page_header.text == "Створити подію"
            or create_event_page.page_header.text == "Create event")
