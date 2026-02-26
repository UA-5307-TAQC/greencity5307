"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent
from components.common_components.auth_components.signin_modal_component import SignInComponent
from utils.custom_web_element import CustomWebElement
from utils.logger import logger


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""
    locators = {
        "main_page":(By.XPATH, ".//a[@href='#/greenCity']"),
        "new_link": (By.XPATH, ".//a[@href='#/greenCity/news']"),
        "event_link": (By.XPATH, ".//a[@href='#/greenCity/events']"),
        "sign_in_link": (By.CSS_SELECTOR,
                         ".header_navigation-menu-right-list > .header_sign-in-link"),
        "about_us_link": (By.XPATH, ".//a[@href='#/greenCity/about']"),
        "my_space_tab": (By.XPATH, ".//a[contains(.,'Мій кабінет') or contains(., 'My space')]"),
        "language_option": (By.XPATH, ".//li[contains(@class, 'lang-option')]/span"),
        "ubs_courier_link": (By.XPATH, ".//a[contains(@href, 'ubs')]"),
        "places_link": (By.XPATH, "//div/nav/ul/li[3]/a")
    }

    main_page: CustomWebElement
    new_link: CustomWebElement
    event_link: CustomWebElement
    sign_in_link: CustomWebElement
    about_us_link: CustomWebElement
    my_space_tab: CustomWebElement
    language_option: CustomWebElement
    ubs_courier_link: CustomWebElement
    places_link: CustomWebElement


    @allure.step("Clicking the My Space link in the header")
    def click_my_space(self):
        """Click my space link in the header
        and return an instance of the MySpaceAbstractPage."""
        from pages.my_space_abstract_page \
            import MySpaceAbstractPage  # pylint: disable=import-outside-toplevel
        self.my_space_tab.wait_and_click()
        return MySpaceAbstractPage(self.driver)

    def is_language_english(self) -> bool:
        """Check if the current language is English by
         inspecting the language option in the header."""
        return self.language_option.text.strip().lower() in ["en", "english"]

    @allure.step("Clicking the news link in the header")
    def click_new_link(self) -> "EcoNewsPage":
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        logger.info("Clicking the news link in the header.")

        try:
            self.new_link.wait_and_click()
            logger.info("Successfully clicked the news link in the header.")

            from pages.eco_news_page import EcoNewsPage  # pylint: disable=import-outside-toplevel
            return EcoNewsPage(self.driver)

        except Exception:
            logger.exception("Failed to click the news link in the header.")
            raise

    @allure.step("Clicking the event link in the header")
    def click_event_link(self) -> "EventPage":
        """Click the event link in the header and return an instance of the EventPage."""
        from pages.event_page import EventPage  # pylint: disable=import-outside-toplevel
        self.event_link.wait_and_click()
        return EventPage(self.driver)

    @allure.step("Clicking the main page link in the header")
    def click_main_page_link(self) -> "MainPage":
        """Click the main page link in the header and return an instance of the MainPage."""
        from pages.main_page import MainPage  # pylint: disable=import-outside-toplevel
        self.main_page.click()
        return MainPage(self.root.parent)

    @allure.step("Clicking the places link in the header")
    def click_places_link(self) -> "PlacesPage":
        """Click the places link in the header and return an instance of the PlacesPage."""
        from pages.places_pages.places_page import PlacesPage # pylint: disable=import-outside-toplevel

        self.places_link.click()
        return PlacesPage(self.root.parent)

    @allure.step("Clicking the about us link in the header")
    def click_about_us_link(self) -> "AboutUsPage":
        """Click the about us link in the header and return an instance of the AboutUsPage."""
        from pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        self.about_us_link.click()

        return AboutUsPage(self.root.parent)

    @allure.step("Clicking the my space link in the header")
    def click_my_space_link(self) -> "MySpaceAbstractPage":
        """
        Click the my space link in the header and
        return an instance of the MySpaceAbstractPage.
        """
        from pages.my_space_abstract_page import MySpaceAbstractPage  # pylint: disable=import-outside-toplevel
        self.my_space_tab.click()
        return MySpaceAbstractPage(self.root.parent)

    @allure.step("Clicking the UBS Courier link in the header")
    def click_ubs_courier_link(self) -> "UBSCourierPage":
        """Click the UBS Courier link in the header and return an instance of the UBSCourierPage."""
        from pages.ubc_courier_page import UBSCourierPage  # pylint: disable=import-outside-toplevel
        self.ubs_courier_link.click()
        return UBSCourierPage(self.root.parent)

    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the Sign-in link and return the SignInComponent modal."""
        self.sign_in_link.wait_and_click()

        modal_locator = (By.TAG_NAME, "app-auth-modal")
        modal_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(modal_locator)
        )

        return SignInComponent(modal_element)
