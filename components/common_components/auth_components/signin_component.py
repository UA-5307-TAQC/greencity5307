"""Sign In Component"""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class SignInComponent(BaseComponent):
    """Initialize sign in component"""
    email_locator: Locators = (By.XPATH, '//*[@id="email"]')
    password_locator: Locators = (By.XPATH, '//*[@id="password"]')
    forgot_password_locator: Locators = (By.XPATH, '//app-sign-in//a[@class="forgot-password"]')
    sign_in_button_locator: Locators = (By.XPATH, '//app-sign-in//button[@type="submit"]')
    sign_in_with_google_button_locator: Locators = (By.XPATH, '//button[contains(., "Google")]')
    sign_up_button_locator: Locators = (By.XPATH, '//a[contains(text(), "Sign up")]')

    email = "greencitytest69@hotmail.com"
    password = "asweQA5346!)"

    def sign_in(self):
        """Signing in"""
        self.find(self.email_locator).send_keys(self.email)
        self.find(self.password_locator).send_keys(self.password)
        self.click(self.sign_in_button_locator)
