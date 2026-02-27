"""This module contains tests for about us page vision cards buttons check after sing in."""
import allure
from data.config import Config
from components.common_components.auth_components.signin_modal_component import SignInComponent
from pages.about_us_page import AboutUsPage
from pages.eco_news_page import EcoNewsPage
from pages.friends_abstract_page import FriendsAbstractPage
from pages.main_page import MainPage
from pages.places_pages.places_page import PlacesPage


# pylint: disable=no-member
@allure.title("Test Validation: Click buttons in the vision card after sing in.")
@allure.description("This test verifies that a user can successfully open pages "
                    "after clicking on buttons in vision cards on the page. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-102")
def test_about_us_page_sing_in_vision_cards_buttons_check(driver):
    """
        TC-102
        Title: Click buttons in the vision card after sing in
        Author: Vitalina Kliuieva
        Priority: Medium
    """

    main_page = MainPage(driver)

    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    about_page: AboutUsPage = main_page.go_to_about_us()
    assert about_page.is_page_loaded(), "About Us page is not opened"

    place_page: PlacesPage = about_page.click_vision_card_button(1)
    assert place_page.is_page_loaded(), "Eco News page is not opened"

    about_page = place_page.go_to_about_us()
    assert about_page.is_page_loaded(), "About Us page is not opened"

    friends_page: FriendsAbstractPage = about_page.click_vision_card_button(2)
    assert friends_page.is_page_loaded(), "Friends page is not opened"

    about_page = friends_page.go_to_about_us()
    assert about_page.is_page_opened(), "About Us page is not opened"

    news_page: EcoNewsPage = about_page.click_vision_card_button(3)
    assert news_page.is_page_opened(), "Eco News page is not opened"

    about_page = news_page.go_to_about_us()
    assert about_page.is_page_opened(), "About Us page is not opened"

    friends_page = about_page.click_vision_card_button(4)
    assert friends_page.is_page_loaded(), "Friends page is not opened"
