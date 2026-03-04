"""This module contains tests for about us page vision cards buttons check before sign in."""
import allure

from pages.common_pages.about_us_page import AboutUsPage
from pages.common_pages.main_page import MainPage



# pylint: disable=no-member
@allure.title("Test Validation: Click buttons in the vision card before sign in.")
@allure.description("This test verifies that a user, who is not signed in, "
                    "sees the correct behavior after clicking on buttons in vision cards on the page.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-103")
def test_about_us_page_nosignin_vision_cards_buttons_check(driver):
    """
        TC-103
        Title: Click buttons in the vision card before sign in
        Author: Vitalina Kliuieva
        Priority: Medium
    """

    main_page = MainPage(driver)

    about_page: AboutUsPage = main_page.go_to_about_us()
    assert about_page.is_page_loaded(), "About Us page is not opened"

    for i in range(1, 5):
        if i == 3:
            news_page = about_page.click_vision_card_button_without_sign_in(i)
            assert news_page.is_page_opened(), "News page is not opened"
            about_page = news_page.go_to_about_us()
            assert about_page.is_page_loaded(), "About Us page is not opened"
        else:
            sign_in_modal = about_page.click_vision_card_button_without_sign_in(i)
            assert sign_in_modal.is_displayed(), f"Sign In modal is not opened for card {i}"

            sign_in_modal.close_sign_in()

            main_page = MainPage(driver)
            assert main_page.is_page_opened(), "Main page is not opened after closing Sign In modal"

            about_page = main_page.go_to_about_us()
            assert about_page.is_page_loaded(), "About Us page is not opened"
