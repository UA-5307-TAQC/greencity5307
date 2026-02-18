"""Signin modal component"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent
from data.config import Config

class SignInComponent(BaseComponent):
    """Signin modal component class"""
    locators = \
    {
        "email": (By.ID, 'email', WebElement),
        "password": (By.ID, 'password', WebElement),
        "forgot_password": (By.CLASS_NAME, 'forgot-password', WebElement),
        "sign_in_button": (By.XPATH, '//app-sign-in//button[@type="submit"]', WebElement),
        "sign_in_with_google_button": (By.CLASS_NAME,'google-sign-in', WebElement),
        "sign_up_button": (By.XPATH,'//a[contains(text(), "Sign up")]', WebElement),
    }
    email: WebElement
    password: WebElement
    forgot_password: WebElement
    sign_in_button: WebElement
    sign_in_with_google_button: WebElement
    sign_up_button: WebElement

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, root=driver)

    @allure.step("Sign in")
    def sign_in(self, email: str, password: str) -> None:
        """Signing in"""
        self.email.send_keys(email)
        self.password.send_keys(password)
        self.sign_in_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_changes(Config.BASE_UI_URL)
        )
