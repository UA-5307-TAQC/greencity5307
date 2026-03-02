"""Test Saved Abstract Navigation."""

import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract
from pages.common_pages.main_page import MainPage


@allure.title("Test Validation: Saved Abstract navigation.")
@allure.description("This test verifies that a user "
                    "can successfully navigate between tabs on Saved page. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-102")

def test_saved_abstract_tabs_navigation(driver):
    """
        TC-101
        Title: Tabs navigation
        Author: Vitalina Kliuieva
        Priority: High
    """

    main_page = MainPage(driver)

    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    saved_page: SavedAbstract = main_page.go_to_saved()
    assert saved_page.is_page_opened(), "Saved page is not opened"

    events_tab: SavedAbstract = saved_page.go_to_tab("Events")
    assert events_tab.is_page_opened(), "Events tab is not active"

    places_tab: SavedAbstract = saved_page.go_to_tab("Places")
    assert places_tab.is_page_opened(), "Places tab is not active"

    eco_news_tab: SavedAbstract = saved_page.go_to_tab("Eco-news")
    assert eco_news_tab.is_page_opened(), "Eco news tab is not active"
