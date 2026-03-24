"""UI test for verifying Sign In is accessible from Main Page."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage


@allure.feature("Main Page")
@allure.story("Sign In")
@allure.title("TC-MP-03: Verify Sign In is accessible from Main Page")
def test_sign_in_from_main_page(driver: WebDriver) -> None:
    """TC-MP-03: Verify Sign In is accessible from Main Page."""

    with allure.step("Step 1: Open browser"):
        assert driver is not None, "Browser was not opened"

    with allure.step("Step 2: Open GreenCity website"):
        main_page = MainPage(driver)

    with allure.step("Step 3: Verify main page is displayed"):
        assert main_page.is_loaded(), "Main page is not displayed"

    with allure.step("Step 4: Locate the header section"):
        assert main_page.is_header_visible(), "Header is not displayed"

    with allure.step("Step 5: Find 'Sign in' button/link"):
        assert main_page.header.sign_in_link.is_displayed(), "Sign in control is not visible"

    with allure.step("Step 6: Click 'Sign in'"):
        sign_in_modal = main_page.header.click_sign_in_link()
        assert sign_in_modal.is_displayed(), "Sign in modal did not open"

    with allure.step("Step 7: Verify email field is displayed"):
        assert sign_in_modal.email.is_displayed(), "Email input is not visible"

    with allure.step("Step 8: Verify password field is displayed"):
        assert sign_in_modal.password.is_displayed(), "Password input is not visible"

    with allure.step("Step 9: Verify login button is displayed"):
        assert sign_in_modal.sign_in_button.is_displayed(), "Login button is not visible"

    with allure.step("Step 10: Verify 'Sign in' modal remains open"):
        assert sign_in_modal.is_displayed(), "Sign in form is not accessible"
