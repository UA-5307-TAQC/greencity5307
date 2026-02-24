"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from components.common_components.auth_components.signin_modal_component import SignInComponent
from utils.logger import logger
from utils.types import Locators


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""
    new_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/news']")
    event_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/events']")
    sign_in_link_locator: Locators = (By.CSS_SELECTOR,
                                      ".header_navigation-menu-right-list > .header_sign-in-link")
    about_us_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/about']")
    my_space_tab_locator: Locators = (By.XPATH,
                                      ".//a[contains(.,'Мій кабінет') or contains(., 'My space')]")
    language_option = (By.XPATH, ".//li[contains(@class, 'lang-option')]/span")

    @allure.step("Clicking the My Space link in the header")
    def click_my_space(self) -> "MySpaceAbstractPage":
        """Click the my space link in the header
        and return an instance of the MySpaceAbstractPage."""
        from pages.my_space_abstract_page import MySpaceAbstractPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.my_space_tab_locator)
        ).click()
        return MySpaceAbstractPage(self.root.parent)

    def is_language_english(self) -> bool:
        """Check if the current language is English by
         inspecting the language option in the header."""
        element = self.root.parent.find_element(*self.language_option)
        return element.text.strip().lower() in ["en", "english"]

    @allure.step("Clicking the news link in the header")
    def click_new_link(self):
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        logger.info("Clicking the news link in the header.")

        try:
            WebDriverWait(self.root.parent, 10).until(
                EC.element_to_be_clickable(self.new_link_locator)
            ).click()
            logger.info("Successfully clicked the news link in the header.")
            from pages.eco_news_page import EcoNewsPage  # pylint: disable=import-outside-toplevel
            return EcoNewsPage(self.root.parent)

        except Exception:
            logger.exception("Failed to click the news link in the header.")
            raise

    @allure.step("Clicking the event link in the header")
    def click_event_link(self):
        """Click the event link in the header and return an instance of the EventPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.event_link_locator)
        ).click()
        from pages.event_page import EventPage  # pylint: disable=import-outside-toplevel
        return EventPage(self.root.parent)

    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the sign-in link in the header and return an instance of the SignInComponent."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.sign_in_link_locator)
        ).click()
        return SignInComponent(self.root.parent)

    @allure.step("Clicking the About Us link in the header")
    def click_about_us_link(self):
        """Click the About Us link in the header and return an instance of the AboutUsPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.about_us_link_locator)
        ).click()
        from pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        return AboutUsPage(self.root.parent)
