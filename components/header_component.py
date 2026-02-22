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
    my_space_link_locator: Locators = (By.XPATH, "//app-header//ul/li[5]/a")

    @allure.step("Clicking the My Space link in the header")
    def click_my_space(self) -> "MySpaceAbstractPage":
        """
        Click the My Space link in the header and return
        an instance of the MySpaceAbstractPage.
        """
        from pages.my_space_abstract_page import  MySpaceAbstractPage  # pylint: disable=import-outside-toplevel

        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.my_space_link_locator)
        ).click()
        return MySpaceAbstractPage(self.root.parent)

    @allure.step("Clicking the news link in the header")
    def click_new_link(self) -> "EcoNewsPage":
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        from pages.eco_news_page import EcoNewsPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.new_link_locator)
        ).click()
        return EcoNewsPage(self.root.parent)

    @allure.step("Clicking the event link in the header")
    def click_event_link(self) -> "EventPage":
        """Click the event link in the header and return an instance of the EventPage."""
        from pages.event_page import EventPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.event_link_locator)
        ).click()
        return EventPage(self.root.parent)

    def click_sign_in_link(self) -> SignInComponent:
        """Click the Sign-in link and return the SignInComponent modal."""
        driver = self.root.parent

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_link_locator)
        ).click()

        modal_locator = (By.TAG_NAME, "app-auth-modal")

        modal_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(modal_locator)
        )

        return SignInComponent(modal_element)
