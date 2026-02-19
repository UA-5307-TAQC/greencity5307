"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""

    locators = {
        "news_link": (By.XPATH, ".//a[@href='#/greenCity/news']", WebElement),
        "event_link": (By.XPATH, ".//a[@href='#/greenCity/events']", WebElement),
        "sign_in_link": (By.CSS_SELECTOR,
                         ".header_navigation-menu-right-list > .header_sign-in-link", WebElement)
    }

    news_link: WebElement
    event_link: WebElement
    sign_in_link: WebElement

    @allure.step("Clicking the news link in the header")
    def click_new_link(self) -> "EcoNewsPage":
        """
        Click the news link in the header
        and return an instance of the EcoNewsPage.
        """
        from pages.eco_news_page import EcoNewsPage # pylint: disable=C0415

        self.wait_and_click("news_link")
        return EcoNewsPage(self.driver)

    @allure.step("Clicking the event link in the header")
    def click_event_link(self) -> "EventPage":
        """
        Click the event link in the header
        and return an instance of the EventPage.
        """
        from pages.event_page import EventPage # pylint: disable=C0415

        self.wait_and_click("event_link")
        return EventPage(self.driver)

    @allure.step("Clicking sign-in button in the header")
    def click_sign_in_link(self) -> "SignInComponent":
        """
        Click the sign-in link in the header
        and return an instance of the SignInComponent.
        """
        from components.common_components.auth_components.signin_modal_component \
        import (SignInComponent) # pylint: disable=C0415

        self.wait_and_click("sign_in_link")
        return SignInComponent(self.driver)
