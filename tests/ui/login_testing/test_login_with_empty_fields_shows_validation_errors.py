import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage

@allure.epic("User Management")
@allure.feature("Login")
@allure.story("Negative Login Scenarios")
@allure.suite("Authentication Tests")
@allure.title("Verify validation errors when signing in with empty fields")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_empty_fields_shows_validation_errors(driver: WebDriver):
    """
    Test Objective: Verify that the system correctly triggers and displays
    validation error messages when a user attempts to sign in without entering data.
    """
    base_page = BasePage(driver)

    sign_in_component = base_page.header.click_sign_in_link()

    sign_in_component.clear_email_and_password()

    sign_in_component.compare_error(
        error_email_text="Email is required.",
        error_password_text="This field is required"
    )
