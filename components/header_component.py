"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from components.common_components.auth_components.signin_modal_component \
    import SignInComponent
from utils.logger import logger


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""

    locators = {
        "new_link": (By.XPATH, ".//a[@href='#/greenCity/news']"),
        "event_link": (By.XPATH, ".//a[@href='#/greenCity/events']"),
        "sign_in_link": (By.CSS_SELECTOR,
                         ".header_navigation-menu-right-list > .header_sign-in-link"),
        "about_us_link": (By.XPATH, ".//a[@href='#/greenCity/about']"),
        "my_space_tab": (By.XPATH, ".//a[contains(.,'Мій кабінет') or contains(., 'My space')]"),
        "language_option": (By.XPATH, ".//li[contains(@class, 'lang-option')]/span"),
    }

    new_link: WebElement
    event_link: WebElement
    sign_in_link: WebElement
    about_us_link: WebElement
    my_space_tab: WebElement
    language_option: WebElement

    @allure.step("Clicking the My Space link in the header")
    def click_my_space(self) -> "MySpaceAbstractPage":
        """Click the my space link in the header
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

    def click_sign_in_link(self) -> SignInComponent:
        """Click the Sign-in link and return the SignInComponent modal."""
        self.sign_in_link.wait_and_click()

        modal_locator = (By.TAG_NAME, "app-auth-modal")
        modal_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(modal_locator)
        )

        return SignInComponent(self.driver, root=modal_element)

    @allure.step("Clicking the About Us link in the header")
    def click_about_us_link(self):
        """Click the About Us link in the header and return an instance of the AboutUsPage."""
        self.about_us_link.wait_and_click()

        from pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        return AboutUsPage(self.driver)
