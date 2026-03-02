"""File to test user menu functionality."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from components.common_components.auth_components.signin_modal_component import \
    SignInComponent
from data.config import Config
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.common_pages.main_page import MainPage
from pages.common_pages.ubc_courier_page import UBSCourierPage


@allure.epic("GreenCity Main Functionality")
@allure.feature("User Profile")
@allure.story("User menu functionality check.")
@allure.testcase("https://github.com/UA-5307-TAQC/greencity5307/issues/45")
@allure.severity(allure.severity_level.MINOR)
@allure.title("User menu check")
def test_user_menu(driver: WebDriver):
    """Check user menu functionality."""
    main_page = MainPage(driver)

    with allure.step("Pre-condition: Ensure the user is logged in"):
        initial_url = driver.current_url

        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

        main_page.get_wait().until(
            EC.url_changes(initial_url),
            message="URL did not change after login. Login might have failed."
        )

        my_space_page = MySpaceAbstractPage(driver)
        assert ("profile" in driver.current_url and
                my_space_page.user_name.text ==
                "test"), "This is not my space page."


    with allure.step("Step 1: click on user menu, and ensure that 'Profile' and 'Sign out' buttons is enabled."):
        main_page.header.click_user_menu()

        assert (main_page.header.user_menu_profile_link.is_enabled() and
                main_page.header.user_menu_sign_out_link.is_enabled()), \
            "Profile or Sign out button is not enabled or visible in the user menu!"

    with allure.step("Step 2: Click on 'Profile' option and verify redirection."):
        current_url = driver.current_url

        main_page.header.click_user_menu_profile_link()
        main_page.get_wait().until(
            EC.url_changes(current_url)
        )

        assert "orders" in driver.current_url, "Did not redirect after clicking 'Profile'."

    with allure.step("Step 3: Click on 'Sign Out' link, and ensure it change url and make user logged out."):
        driver.get("https://www.greencity.cx.ua/#/greenCity/profile")
        main_page.header.click_user_menu()
        initial_url = driver.current_url
        main_page.header.click_user_menu_sign_out_link()

        main_page.get_wait().until(
            EC.url_changes(initial_url)
        )

        assert ("greencity" in driver.current_url and
                main_page.header.sign_in_link.is_enabled()), "Sign out button did not work properly."
