"""Module for testing opening Saved Places page."""

from selenium.webdriver.remote.webdriver import WebDriver
import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.saved_abstract.places_saved_page import PlacesSavedPage
from pages.common_pages.main_page import MainPage
from pages.common_pages.places_page import PlacesPage


@allure.title("Verify Saved Places page opens correctly")
@allure.feature("Saved Places")
@allure.story("Open Saved Places page")
def test_saved_places_page_opens_correctly(driver: WebDriver):
    """Test opening Saved Places page and verifying its main elements."""
    with allure.step("Open GreenCity main page"):
        main_page = MainPage(driver)
        assert main_page.is_page_opened()

    with allure.step("Sign in"):
        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("Open Places page from header"):
        places_page: PlacesPage = main_page.header.click_places_link()
        assert places_page.is_page_opened()

    with allure.step("Open Saved Places page"):
        saved_places_page: PlacesSavedPage = places_page.go_to_saved_places()
        assert saved_places_page.is_page_opened()

    with allure.step("Verify page title"):
        assert saved_places_page.get_page_title_text() in ["Saved", "Збережені"]

    with allure.step("Verify Places tab is active"):
        assert saved_places_page.is_places_tab_active()

    with allure.step("Verify URL contains bookmark parameter"):
        assert "isBookmark=true" in driver.current_url

    with allure.step("Verify URL contains places section"):
        assert "places" in driver.current_url