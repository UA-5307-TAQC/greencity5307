"""Module for testing filters and search controls on Saved Places page."""

from selenium.webdriver.remote.webdriver import WebDriver
import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.saved_abstract.places_saved_page import PlacesSavedPage
from pages.common_pages.main_page import MainPage


@allure.title("Verify filters and search controls are displayed on Saved Places page")
@allure.feature("Saved Places")
@allure.story("Filters and search controls")
def test_filters_and_search_controls_on_saved_places_page(driver: WebDriver):
    """Test visibility of filters and search controls on Saved Places page."""
    with allure.step("Open GreenCity main page"):
        main_page = MainPage(driver)
        assert main_page.is_page_opened()

    with allure.step("Sign in"):
        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("Open Saved page"):
        main_page.go_to_saved()

    with allure.step("Switch to Places tab"):
        saved_places_page = PlacesSavedPage(driver)
        saved_places_page.open_places_tab()
        assert saved_places_page.is_page_opened()

    with allure.step("Verify search input is displayed"):
        assert saved_places_page.is_search_input_visible()

    with allure.step("Verify location input is displayed"):
        assert saved_places_page.is_location_input_visible()

    with allure.step("Verify filter buttons are displayed"):
        assert saved_places_page.is_shops_filter_visible()
        assert saved_places_page.is_restaurants_filter_visible()
        assert saved_places_page.is_recycling_points_filter_visible()
        assert saved_places_page.is_events_filter_visible()
        assert saved_places_page.is_saved_places_filter_visible()
        assert saved_places_page.is_more_options_filter_visible()

    with allure.step("Verify map section is displayed"):
        assert saved_places_page.is_map_section_visible()
