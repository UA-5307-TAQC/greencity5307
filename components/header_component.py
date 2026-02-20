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
    logo_link_locator: Locators = (By.CSS_SELECTOR, ".header_logo")
    new_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/news']")
    event_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/events']")
    sign_in_link_locator: Locators = (By.CSS_SELECTOR,
                                      ".header_navigation-menu-right-list > .header_sign-in-link")
    my_space_link_locator: Locators = (By.CSS_SELECTOR, "a[href='#/greenCity/profile']")
    _user_name_locator: Locators = (By.CSS_SELECTOR, ".body-2.user-name")

    @allure.step("Clicking the news link in the header")
    def click_new_link(self) -> "EcoNewsPage":
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        from pages.eco_news_page import EcoNewsPage  # pylint: disable=import-outside-toplevel

        logger.info("Clicking the news link in the header.")

        try:
            WebDriverWait(self.root.parent,
                          10).until(EC.element_to_be_clickable(self.new_link_locator)).click()
            logger.info("Successfully clicked the news link in the header.")
            return EcoNewsPage(self.root.parent)

        except Exception:
            logger.exception("Failed to click the news link in the header.")
            raise

    @allure.step("Clicking the event link in the header")
    def click_event_link(self) -> "EventPage":
        """Click the event link in the header and return an instance of the EventPage."""
        from pages.event_page import EventPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.event_link_locator)).click()
        return EventPage(self.root.parent)

    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the sign in link in the header and return an instance of the SignInComponent."""
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.sign_in_link_locator)).click()
        return SignInComponent(self.root.parent)

    @allure.step("Clicking 'My Space' link button in the header")
    def click_my_space_link(self):
        """Click the 'My Space' link in the header and
        return an instance of the MySpaceAbstractPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.my_space_link_locator)
        ).click()
        from pages.my_habit_page import MyHabitPage  # pylint: disable=import-outside-toplevel
        return MyHabitPage(self.root.parent)

    @allure.step("Clicking the logo link in the header")
    def click_logo(self):
        """Click the logo in the header and return an instance of the MainPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.logo_link_locator)
        ).click()
        from pages.main_page import MainPage  # pylint: disable=import-outside-toplevel
        return MainPage(self.root.parent)

    def get_signed_in_user_name(self):
        """Get the username of the signed-in user from the header."""
        username_element = WebDriverWait(self.root.parent, 5).until(
            EC.visibility_of_element_located(self._user_name_locator)
        )
        return username_element.text
