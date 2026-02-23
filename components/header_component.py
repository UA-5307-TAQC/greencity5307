"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""
from typing import Tuple

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from components.common_components.auth_components.signin_modal_component import SignInComponent


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""
    Locators = Tuple[str, str]

    new_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/news']")
    event_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/events']")
    sign_in_link_locator: Locators = (By.CSS_SELECTOR,
                                      ".header_navigation-menu-right-list > .header_sign-in-link")
    language_option = (By.XPATH,
                       "/html/body/app-root/app-main/div/app-header/"
                       "header/div[2]/div/div/div/ul/ul[1]/li/span")

    def is_language_english(self) -> bool:
        """Check if the current language is English by
         inspecting the language option in the header."""
        element = self.root.parent.find_element(*self.language_option)
        return element.text.strip().lower() in ["en", "english"]

    @allure.step("Clicking the news link in the header")
    def click_new_link(self):
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.new_link_locator)
        ).click()


    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the sign in link in the header and return an instance of the SignInComponent."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.sign_in_link_locator)
        ).click()
        return SignInComponent(self.root.parent)

    def click_event_link(self):
        """Click the event link in the header."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.event_link_locator)
        ).click()
