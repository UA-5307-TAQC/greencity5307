"""Module for testing switching to Places tab on Saved page."""

from selenium.webdriver.remote.webdriver import WebDriver
import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.saved_abstract.places_saved_page import PlacesSavedPage
from pages.common_pages.main_page import MainPage


@allure.title("Verify user can switch to Places tab on Saved page")
@allure.feature("Saved Places")
@allure.story("Switch to Places tab")
def test_switch_to_places_tab_on_saved_page(driver: WebDriver):
    """Test switching to Places tab on Saved page."""
    with allure.step("Open GreenCity main page"):
        main_page = MainPage(driver)
        assert main_page.is_page_opened()

    with allure.step("Sign in"):
        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("Open Saved page"):
        main_page.go_to_saved()

    with allure.step("Switch to Places tab"):
        places_saved_page = PlacesSavedPage(driver)
        places_saved_page.open_places_tab()

    with allure.step("Verify Places tab is active"):
        assert places_saved_page.is_places_tab_active()

    with allure.step("Verify URL is changed"):
        assert "places" in driver.current_url
        assert "isBookmark=true" in driver.current_url

    with allure.step("Verify Places-specific content is displayed"):
        assert places_saved_page.is_search_input_visible()
        assert places_saved_page.is_location_input_visible()