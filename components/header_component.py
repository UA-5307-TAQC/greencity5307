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
    main_page_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity']")
    new_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/news']")
    event_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/events']")
    places_link_locator: Locators = (By.XPATH, "//div/nav/ul/li[3]/a")
    about_us_link_locator: Locators = (By.XPATH, "//div/nav/ul/li[4]/a")
    my_space_link_locator: Locators = (By.XPATH, "//div/nav/ul/li[5]/a")
    ubs_courier_link_locator: Locators = (By.XPATH, ".//a[contains(@href, 'ubs')]")
    sign_in_link_locator: Locators = (By.CSS_SELECTOR,
                                      ".header_navigation-menu-right-list > .header_sign-in-link")

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

    @allure.step("Clicking the main page link in the header")
    def click_main_page_link(self) -> "MainPage":
        """Click the main page link in the header and return an instance of the MainPage."""
        from pages.main_page import MainPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.main_page_locator)).click()
        return MainPage(self.root.parent)

    @allure.step("Clicking the places link in the header")
    def click_places_link(self) -> "PlacesPage":
        """Click the places link in the header and return an instance of the PlacesPage."""
        from pages.places_page import PlacesPage # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.places_link_locator)).click()
        return PlacesPage(self.root.parent)

    @allure.step("Clicking the about us link in the header")
    def click_about_us_link(self) -> "AboutUsPage":
        """Click the about us link in the header and return an instance of the AboutUsPage."""
        from pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.about_us_link_locator)).click()
        return AboutUsPage(self.root.parent)

    @allure.step("Clicking the my space link in the header")
    def click_my_space_link(self) -> "MySpaceAbstractPage":
        """
        Click the my space link in the header and
        return an instance of the MySpaceAbstractPage.
        """
        from pages.my_space_abstract_page import MySpaceAbstractPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.my_space_link_locator)).click()
        return MySpaceAbstractPage(self.root.parent)

    @allure.step("Clicking the UBS Courier link in the header")
    def click_ubs_courier_link(self) -> "UBSCourierPage":
        """Click the UBS Courier link in the header and return an instance of the UBSCourierPage."""
        from pages.ubc_courier_page import UBSCourierPage  # pylint: disable=import-outside-toplevel
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.ubs_courier_link_locator)).click()
        return UBSCourierPage(self.root.parent)

    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the sign in link in the header and return an instance of the SignInComponent."""
        WebDriverWait(self.root.parent,
                      10).until(EC.element_to_be_clickable(self.sign_in_link_locator)).click()
        return SignInComponent(self.root.parent)
