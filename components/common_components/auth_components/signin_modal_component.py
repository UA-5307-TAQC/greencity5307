"""Signin modal component"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent
from data.config import Config
from utils.types import Locators


class SignInComponent(BaseComponent):
    """Signin modal component class"""
    email_locator: Locators = (By.ID, "email")
    password_locator: Locators = (By.ID, "password")
    forgot_password_locator: Locators = (By.CLASS_NAME, "forgot-password")
    sign_in_button_locator: Locators = (By.XPATH,
                                        "//app-sign-in//button[@type='submit']")
    sign_in_with_google_button_locator: Locators = (By.CLASS_NAME,
                                                    "google-sign-in")
    sign_up_button_locator: Locators = (By.XPATH,
                                        '//a[contains(text(), "Sign up")]')
    def get_email(self):
        """Get email input value"""
        return self.root.find_element(*self.email_locator)

    def get_password(self):
        """Get password input value"""
        return self.root.find_element(*self.password_locator)

    def get_sign_in_button(self):
        """Get sign in button"""
        return self.root.find_element(*self.sign_in_button_locator)

    @allure.step("Sign in")
    def sign_in(self, driver: WebDriver, email: str, password: str) -> None:
        """Signing in"""
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        self.get_sign_in_button().click()
        # wait for sign in
        WebDriverWait(driver, 10).until(
            EC.url_changes(Config.BASE_UI_URL)
        )
