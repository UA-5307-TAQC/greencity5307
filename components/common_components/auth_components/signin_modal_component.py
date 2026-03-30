"""Signin modal component"""
import allure
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from components.base_component import BaseComponent
from data.config import Config
from utils.custom_web_element import CustomWebElement


class SignInComponent(BaseComponent):
    """Signin modal component class"""
    locators = {
        "email": (By.ID, "email"),
        "password": (By.ID, "password"),
        "forgot_password": (By.CLASS_NAME, "forgot-password"),
        "sign_in_button": (By.XPATH,
                                   "//app-sign-in//button[@type='submit']"),
        "sign_in_with_google_button": (By.CLASS_NAME,"google-sign-in"),
        "sign_up_button": (By.XPATH,'//a[contains(text(), "Sign up")]'),
        "close_button": (By.CLASS_NAME,
                         "close-modal-window"),
        "email_error": (By.ID, "email-err-msg"),
        "password_error": (By.ID, "pass-err-msg"),
    }

    email: CustomWebElement
    password: CustomWebElement
    forgot_password: CustomWebElement
    sign_in_button: CustomWebElement
    sign_in_with_google_button: CustomWebElement
    sign_up_button: CustomWebElement
    close_button: CustomWebElement
    email_error: CustomWebElement
    password_error: CustomWebElement

    @allure.step("Sign in")
    def sign_in(self, email: str, password: str):
        """Signing in"""
        self.email.send_keys(email)
        self.password.send_keys(password)
        self.sign_in_button.wait_and_click()
        self.get_wait().until(
            EC.url_changes(Config.BASE_UI_URL)
        )
        from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage # pylint: disable=import-outside-toplevel
        return MyHabitPage(self.driver)

    @allure.step("Closing the sign-in modal")
    def close_sign_in(self):
        """Closing the sign-in modal"""
        self.close_button.wait_and_click()
        self.get_wait().until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".cdk-overlay-backdrop")
        ))

    @allure.step("Checking if the sign-in modal is displayed")
    def is_displayed(self):
        """Check if the sign-in modal is displayed."""
        try:
            self.get_wait(5).until(
                EC.visibility_of_element_located(self.locators["email"])
            )
            return True
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            return False

    @allure.step("Clear email and password fields to trigger validation")
    def clear_email_and_password(self):
        """
        Clears input fields and cycles focus to ensure 'onBlur'
        validation is triggered on the frontend.
        """
        self.email.clear()
        self.password.wait_and_click()
        self.password.clear()
        self.email.wait_and_click()
        self.password.wait_and_click()
        return self

    @allure.step("Verify email and password validation error messages (supports EN/UA)")
    def compare_error(self):
        """
        Waits for error messages to be visible and matches their text content.
        """
        wait = self.get_wait()
        email_error_element = wait.until(
            EC.visibility_of_element_located(self.locators["email_error"])
        )
        password_error_element = wait.until(
            EC.visibility_of_element_located(self.locators["password_error"])
        )
        actual_email_error = email_error_element.text.strip()
        actual_password_error = password_error_element.text.strip()

        valid_email_errors = ["Введіть пошту.", "Email is required."]
        valid_password_errors = ["Це поле є обов'язковим",
                                 "Password is required"]
        assert actual_email_error in valid_email_errors, (
            f"Expected email error to be one of {valid_email_errors}, but got '{actual_email_error}'"
        )
        assert actual_password_error in valid_password_errors, (
            f"Expected password error to be one of {valid_password_errors}, but got '{actual_password_error}'"
        )
