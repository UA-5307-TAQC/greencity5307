"""Test create new event"""

import pytest
import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import Config
from pages.base_page import BasePage
from pages.events_pages.create_update_event_page import CreateEventPage
from pages.events_pages.event_page import EventPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
# from components.header_component import HeaderComponent

@allure.title("Create new event with valid data")
@allure.description(
    "Verify that registered user can create new event with valid data "
    "and is redirected to event page after publishing."
)
@allure.severity(allure.severity_level.NORMAL)
def test_create_new_event(driver: WebDriver):
    """TC-CE-01"""
    base_page = BasePage(driver)

    with allure.step("User signs in with valid credentials"):
        sign_in_component = base_page.header.click_sign_in_link()
        sign_in_component.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("User opens Event page"):
        my_space_page = MySpaceAbstractPage(driver)
        my_space_page.header.click_event_link()

    with allure.step("User opens Create Event page"):
        event_page = EventPage(driver)
        page = event_page.click_create_event()

    with allure.step("User enters event title"):
        page.header_root.set_title("Park Cleanup")

    with allure.step("User selects initiative type"):
        page.chip_set.select_chip("Екологічний")

    with allure.step("User selects event type"):
        page.event_type.select_event_type("Відкрита")

    with allure.step("User enters event description"):
        page.description.set_description("Community park cleaning event")

    with allure.step("User selects event date and time"):
        page.date_time.select_date("20")
        page.date_time.fill_start_time("10:00")
        page.date_time.fill_end_time("12:00")

    with allure.step("User selects Place checkbox"):
        page.date_location.set_place(True)

    with allure.step("User enters event address"):
        page.date_location.fill_address("Kyiv, Park of Glory")

    with allure.step("Publish button should become enabled"):
        WebDriverWait(driver, 5).until(
            lambda d: page.publish_button.is_enabled()
        )

    with allure.step("User publishes event"):
        page.click_publish()

    with allure.step("Verify user redirected to created event page"):
        WebDriverWait(driver, 10).until(
            EC.url_contains("/events/")
        )
