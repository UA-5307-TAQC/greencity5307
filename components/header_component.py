"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from components.common_components.auth_components.signin_modal_component \
    import SignInComponent
from utils.types import Locators


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""
    new_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/news']")
    event_link_locator: Locators = (By.XPATH,
                                    ".//a[@href='#/greenCity/events']")
    sign_in_link_locator: Locators = (By.CSS_SELECTOR,
                                      ".header_navigation-menu-right-list > .header_sign-in-link")
    eco_news_locator: Locators = (By.CSS_SELECTOR, "li.nav-left-list:first-child")
    language_switcher: Locators = (By.CSS_SELECTOR,
                                   "ul.header_lang-switcher-wrp")
    language_option_ua: Locators = (By.XPATH, "//li[contains(@aria-label, 'Uk')]")
    language_option_en: Locators = (By.XPATH, "//li[contains(@aria-label, 'En')]")

    @allure.step("Clicking the news link in the header")
    def click_new_link(self) -> "EcoNewsPage":
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        from pages.eco_news_page import \
            EcoNewsPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.new_link_locator)
        ).click()
        return EcoNewsPage(self.root.parent)

    @allure.step("Getting text of the news link")
    def get_new_link_text(self) -> str:
        """Get the text of the news link in the header."""
        return WebDriverWait(self.root.parent, 10).until(
            EC.visibility_of_element_located(self.new_link_locator)
        ).text

    @allure.step("Switching language to {lang_code}")
    def switch_language_to(self, lang_code: str):
        """
        Switch language to the given language code.
        :param lang_code: 'ua' or 'en'
        """
        WebDriverWait(self.root.parent, 4).until(
            EC.element_to_be_clickable(self.language_switcher)
        ).click()

        if lang_code.lower() in ('en', 'english'):
            target_locator = self.language_option_en
        else:
            target_locator = self.language_option_ua

        WebDriverWait(self.root.parent, 4).until(
            EC.element_to_be_clickable(target_locator)
        ).click()

        WebDriverWait(self.root.parent, 4).until(
            EC.invisibility_of_element_located(target_locator)
        )

    @allure.step("Clicking the event link in the header")
    def click_event_link(self) -> "EventPage":
        """Click the event link in the header and return an instance of the EventPage."""
        from pages.event_page import \
            EventPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.event_link_locator)
        ).click()
        return EventPage(self.root.parent)

    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the sign in link in the header and return an instance of the SignInComponent."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.sign_in_link_locator)
        ).click()
        return SignInComponent(self.root.parent)
