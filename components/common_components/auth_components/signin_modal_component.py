"""Signin modal component"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
        "sign_up_button": (By.XPATH,'//a[contains(text(), "Sign up")]')
    }

    email: CustomWebElement
    password: CustomWebElement
    forgot_password: CustomWebElement
    sign_in_button: CustomWebElement
    sign_in_with_google_button: CustomWebElement
    sign_up_button: CustomWebElement

    @allure.step("Sign in")
    def sign_in(self, email: str, password: str):
        """Signing in"""
        self.email.send_keys(email)
        self.password.send_keys(password)
        self.sign_in_button.wait_and_click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(Config.BASE_UI_URL)
        )
        from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage # pylint: disable=import-outside-toplevel
        return MyHabitPage(self.driver)
