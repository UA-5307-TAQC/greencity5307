"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from components.base_component import BaseComponent
from components.common_components.auth_components.signin_modal_component import \
    SignInComponent
from utils.custom_web_element import CustomWebElement
from utils.logger import logger


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""
    locators = {
        "main_page": (By.XPATH, ".//a[@href='#/greenCity']"),
        "new_link": (By.XPATH, ".//a[@href='#/greenCity/news']"),
        "event_link": (By.XPATH, ".//a[@href='#/greenCity/events']"),
        "sign_in_link": (By.CSS_SELECTOR,
                         ".header_navigation-menu-right-list > .header_sign-in-link"),
        "about_us_link": (By.XPATH, ".//a[@href='#/greenCity/about']"),
        "my_space_tab": (By.XPATH,
                         ".//a[contains(.,'Мій кабінет') or contains(., 'My space')]"),
        "language_option": (By.XPATH,
                            ".//li[contains(@class, 'lang-option')]/span"),
        "other_language_option": (By.XPATH,
                                  ".//ul[contains(@aria-label, 'language switcher')]/li[2]/span"),
        "ubs_courier_link": (By.XPATH, ".//a[contains(@href, 'ubs')]"),
        "places_link": (By.XPATH, "//div/nav/ul/li[3]/a"),
        "logo_link": (By.CSS_SELECTOR, ".header_logo"),
        "_username": (By.CSS_SELECTOR, ".body-2.user-name"),
        "user_menu": (By.XPATH, "//*[@id='header_user-wrp']"),
        "user_menu_profile_link": (By.XPATH,
                                   "//*[@id='header_user-wrp']/ul/li[@role='navigation']"),
        "user_menu_sign_out_link": (By.XPATH,
                                    "//*[@id='header_user-wrp']/ul/li[@aria-label='sign-out']"),
        "saved_link": (By.XPATH, "/html/body/app-root/app-main/div/app-header"
                                 "/header/div[2]/div/div/div/ul/li[1]/img")
    }

    main_page: CustomWebElement
    new_link: CustomWebElement
    event_link: CustomWebElement
    sign_in_link: CustomWebElement
    about_us_link: CustomWebElement
    my_space_tab: CustomWebElement
    language_option: CustomWebElement
    other_language_option: CustomWebElement
    ubs_courier_link: CustomWebElement
    places_link: CustomWebElement
    logo_link: CustomWebElement
    _username: CustomWebElement
    user_menu: CustomWebElement
    user_menu_profile_link: CustomWebElement
    user_menu_sign_out_link: CustomWebElement
    saved_link: CustomWebElement

    @allure.step("Clicking the saved link in the header")
    def click_saved_link(self) -> "SavedAbstract":
        """Click the saved link in the header and return an instance of the SavedAbstract page."""
        from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract  # pylint: disable=import-outside-toplevel
        self.saved_link.wait_and_click()
        return SavedAbstract(self.driver)

    @allure.step("Clicking the My Space link in the header")
    def click_my_space(self):
        """Click My Space link in the header and delegate to the primary
         navigation method for My Space."""
        return self.click_my_space_link()

    @allure.step("Clicking the language button in the header.")
    def switch_language(self) -> "MainPage":
        """Switch language button in the header."""
        logger.info("Clicking switch language button in the header.")

        self.language_option.wait_and_click()
        self.other_language_option.wait_and_click()
        return self

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

            from pages.news_pages.eco_news_page import \
                EcoNewsPage  # pylint: disable=import-outside-toplevel
            return EcoNewsPage(self.driver)

        except Exception:
            logger.exception("Failed to click the news link in the header.")
            raise

    @allure.step("Clicking the event link in the header")
    def click_event_link(self) -> "EventPage":
        """Click the event link in the header and return an instance of the EventPage."""
        from pages.events_pages.event_page import \
            EventPage  # pylint: disable=import-outside-toplevel
        self.event_link.wait_and_click()
        return EventPage(self.driver)

    @allure.step("Clicking the main page link in the header")
    def click_main_page_link(self) -> "MainPage":
        """Click the main page link in the header and return an instance of the MainPage."""
        from pages.common_pages.main_page import \
            MainPage  # pylint: disable=import-outside-toplevel
        self.main_page.wait_and_click()
        return MainPage(self.driver)

    @allure.step("Clicking the places link in the header")
    def click_places_link(self) -> "PlacesPage":
        """Click the places link in the header and return an instance of the PlacesPage."""
        from pages.common_pages.places_page import \
            PlacesPage  # pylint: disable=import-outside-toplevel

        self.places_link.wait_and_click()
        return PlacesPage(self.driver)

    @allure.step("Clicking the about us link in the header")
    def click_about_us_link(self) -> "AboutUsPage":
        """Click the about us link in the header and return an instance of the AboutUsPage."""
        from pages.common_pages.about_us_page import \
            AboutUsPage  # pylint: disable=import-outside-toplevel
        self.about_us_link.wait_and_click()

        return AboutUsPage(self.driver)

    @allure.step("Clicking the my space link in the header")
    def click_my_space_link(self) -> "MyHabitPage":
        """
        Click the my space link in the header and
        return an instance of the MyHabitPage.
        """
        from pages.abstract_pages.my_space_abstract.my_habit_page \
            import MyHabitPage  # pylint: disable=import-outside-toplevel
        self.my_space_tab.wait_and_click()
        return MyHabitPage(self.driver)

    @allure.step("Clicking the UBS Courier link in the header")
    def click_ubs_courier_link(self) -> "UBSCourierPage":
        """Click the UBS Courier link in the header and return an instance of the UBSCourierPage."""
        from pages.common_pages.ubc_courier_page import \
            UBSCourierPage  # pylint: disable=import-outside-toplevel
        self.ubs_courier_link.wait_and_click()
        return UBSCourierPage(self.driver)

    @allure.step("Clicking signin button in the header")
    def click_sign_in_link(self) -> SignInComponent:
        """Click the Sign-in link and return the SignInComponent modal."""
        self.sign_in_link.wait_and_click()

        modal_locator = (By.TAG_NAME, "app-auth-modal")
        modal_element = self.get_wait().until(
            EC.visibility_of_element_located(modal_locator)
        )

        return SignInComponent(modal_element)

    def click_logo(self):
        """Click the logo in the header and return an instance of the MainPage."""
        self.logo_link.wait_and_click()
        from pages.common_pages.main_page import MainPage  # pylint: disable=import-outside-toplevel
        return MainPage(self.root.parent)

    def get_signed_in_user_name(self):
        """Get the username of the signed-in user from the header."""
        username_element = self.get_wait().until(
            EC.visibility_of(self._username)
        )
        return username_element.text

    @allure.step("Clicking the user menu in the header.")
    def click_user_menu(self):
        """Click the user menu in the header."""
        self.user_menu.wait_and_click()

    @allure.step("Clicking the profile link in user menu in the header.")
    def click_user_menu_profile_link(self):
        """Click the profile link in the header."""
        self.user_menu_profile_link.wait_and_click()

    @allure.step("Clicking the sign out link in user menu in the header.")
    def click_user_menu_sign_out_link(self) -> "MainPage":
        """Click the sign out link in the header."""
        from pages.common_pages.main_page import \
            MainPage  # pylint: disable=import-outside-toplevel
        self.user_menu_sign_out_link.wait_and_click()
        return MainPage(self.driver)
