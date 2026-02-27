"""This module contains the test class for verifying the
Form habit buttons on the About Us page."""
import allure
from data.config import Config
from components.common_components.auth_components.signin_modal_component import SignInComponent
from pages.about_us_page import AboutUsPage
from pages.main_page import MainPage
from pages.my_habit_page import MyHabitPage


# pylint: disable=no-member
@allure.title("Test Validation: About Us Page Buttons Verification.")
@allure.description("This test verifies that a user can successfully click on form habit buttons. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-001")
def test_about_us_page_click_habit_buttons(driver):
    """Test that a user can click Form Habit buttons on About Us page and navigate to My Habit page.

    TC-001
    Title: About us page "Form Habit" buttons verification
    Author: Vitalina Kliuieva
    Priority: High
    """

    main_page = MainPage(driver)

    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    about_page_one: AboutUsPage = main_page.go_to_about_us()
    my_habit_page_one: MyHabitPage = about_page_one.click_section_button_form_habit_one()

    assert my_habit_page_one.is_page_loaded(), "My habit page is not opened"

    about_page_two: AboutUsPage = my_habit_page_one.go_to_about_us()
    my_habit_page_two: MyHabitPage = about_page_two.click_section_button_form_habit_two()

    assert my_habit_page_two.is_page_loaded(), "My habit page is not opened"
