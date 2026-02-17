"""Signin modal component"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
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

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.email_input = self.root.find_element(*self.email_locator)
        self.password_input = self.root.find_element(*self.password_locator)
        self.sign_in_button = self.root.find_element(
            *self.sign_in_button_locator)

    @allure.step("Sign in")
    def sign_in(self, driver: WebDriver, email: str, password: str) -> None:
        """Signing in"""
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.sign_in_button.click()
        # wait for sign in
        WebDriverWait(driver, 10).until(
            EC.url_changes(Config.BASE_UI_URL)
        )
