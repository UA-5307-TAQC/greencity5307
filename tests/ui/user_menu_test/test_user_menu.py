"""File to test user menu functionality."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from data.config import Config
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.common_pages.main_page import MainPage


@allure.epic("GreenCity Main Functionality")
@allure.feature("User Profile")
@allure.story("User menu functionality check.")
@allure.testcase("https://github.com/UA-5307-TAQC/greencity5307/issues/45")
@allure.severity(allure.severity_level.MINOR)
@allure.title("User menu check")
def test_user_menu(driver_with_login: WebDriver):
    """Check user menu functionality."""
    main_page = MainPage(driver_with_login)

    with allure.step("Pre-condition: Ensure the user is logged in"):
        my_space_page = MySpaceAbstractPage(driver_with_login)
        assert ("profile" in driver_with_login.current_url and
                my_space_page.user_name.text ==
                Config.USER_NAME), "This is not my space page or user name is incorrect."

    with allure.step("Step 1: click on user menu, and ensure that 'Profile' and 'Sign out' buttons are enabled."):
        main_page.header.click_user_menu()

        assert (main_page.header.user_menu_profile_link.is_enabled() and
                main_page.header.user_menu_profile_link.is_displayed() and
                main_page.header.user_menu_sign_out_link.is_enabled() and
                main_page.header.user_menu_sign_out_link.is_displayed()), \
            "Profile or Sign out button is not enabled or visible in the user menu!"

    with allure.step("Step 2: Click on 'Profile' option and verify redirection."):
        current_url = driver_with_login.current_url

        main_page.header.click_user_menu_profile_link()
        main_page.get_wait().until(
            EC.url_changes(current_url)
        )

        assert "orders" in driver_with_login.current_url, "Did not redirect after clicking 'Profile'."

    with allure.step("Step 3: Click on 'Sign Out' link, and ensure it change url and make user logged out."):
        driver_with_login.get(f"{Config.BASE_UI_URL.rstrip('/')}/profile")
        main_page.header.click_user_menu()
        initial_url = driver_with_login.current_url
        main_page.header.click_user_menu_sign_out_link()

        main_page.get_wait().until(
            EC.url_changes(initial_url)
        )

        assert ("greencity" in driver_with_login.current_url and
                main_page.header.sign_in_link.is_displayed()), "Sign out button did not work properly."
