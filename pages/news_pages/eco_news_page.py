"""This module contains the EcoNewsPage class, which represents the Eco News page of the website."""
from typing import List

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.news_components.button_create_new_component import CreateNewButtonComponent
from components.news_components.news_card_base_component import NewsCardBaseComponent

from pages.base_page import BasePage
from pages.events_pages.event_page import EventPage
from pages.news_pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
from pages.news_pages.one_news_page import OneNewsPage

from utils.custom_web_element import CustomWebElement


class EcoNewsPage(BasePage): # pylint: disable=too-many-public-methods
    """Page object for the Eco News page."""

    locators = {
        "main_header": (By.CSS_SELECTOR, "h1.main-header"),

        "button_create_news": (By.CSS_SELECTOR, "a.create[href*='create-news']"),

        "title": (By.CSS_SELECTOR, "h1.main-header"),

        "news_cards": (
            By.CSS_SELECTOR,
            "app-news-list li.ng-star-inserted, app-news-list-gallery-view li.ng-star-inserted",
            List[NewsCardBaseComponent],
        ),
        "news_cards_raw": (
            By.XPATH,
            "//a[contains(@class,'link') "
            "and contains(@href,'#/greenCity/news/') "
            "and not(contains(@href,'create-news'))]"
            "/ancestor::li[1]",
        ),

        "card_title_relative": (
            By.XPATH,
            ".//h1|.//h2|.//h3|.//h4",
        ),

        "card_meta_relative": (
            By.XPATH,
            ".//img[@alt='date of creation']/following-sibling::span[1]",
        ),
        "news_feed_container": (By.CSS_SELECTOR, "div.list-gallery"),
    }

    main_header: CustomWebElement
    button_create_news: CreateNewButtonComponent
    title: CustomWebElement
    news_cards: List[NewsCardBaseComponent]

    def get_button_create_news(self) -> CreateNewButtonComponent:
        """Get the create news button component."""
        element = self.driver.find_element(
            *self.locators["button_create_news"])
        return CreateNewButtonComponent(element)

    @allure.step("Clicking the create news button")
    def click_create_button(self):
        """Click the create news link in the page and return an instance of the
        CreateUpdateEcoNews."""
        self.get_button_create_news().click_create_new_button()
        return CreateUpdateEcoNewsPage(self.driver)

    @allure.step("Navigating to the Events page")
    def go_to_events(self) -> "EventPage":
        """Navigate to the Eco News page."""
        self.header.click_event_link()
        self.get_wait().until(EC.url_contains("events"))
        return EventPage(self.driver)

    @allure.step("Navigating to the About Us page from Eco News page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        self.header.click_about_us_link()
        self.get_wait().until(EC.url_contains("about"))
        from pages.common_pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel

        return AboutUsPage(self.driver)

    @allure.step("Checking if Eco News page is opened")
    def is_page_opened(self) -> bool:
        """Check if the Eco News page is opened."""
        self.get_wait().until(EC.url_contains("news"))
        self.get_wait().until(EC.visibility_of(self.title))
        return self.title.is_displayed()

    @allure.step("Checking if Eco News page is loaded")
    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded."""
        self.get_wait().until(
            EC.visibility_of_element_located(
                self.locators["button_create_news"])
        )
        return True

    @allure.step("Wait Eco News page loaded")
    def wait_page_loaded(self) -> None:
        """Wait until Eco News page is loaded."""
        self.get_wait().until(EC.url_contains("greenCity/news"))
        self.get_wait().until(
            EC.visibility_of_element_located(self.locators["main_header"])
        )

    @allure.step("Check title/header is visible")
    def is_header_visible(self) -> bool:
        """Return True if title header is visible."""
        return self.get_wait().until(
            EC.visibility_of_element_located(self.locators["main_header"])
        ).is_displayed()

    @allure.step("Get page header text")
    def get_header_text(self) -> str:
        """Return title/header text."""
        return self.get_wait().until(
            EC.visibility_of_element_located(self.locators["main_header"])
        ).text.strip()

    @allure.step("Check news feed container is visible")
    def is_feed_visible(self) -> bool:
        """Return True if main header container is visible."""
        return self.get_wait().until(
            EC.visibility_of_element_located(self.locators["main_header"])
        ).is_displayed()

    @allure.step("Wait at least one news card is present")
    def wait_cards_present(self) -> None:
        """Wait until the news feed container and at least one news card are present."""
        self.get_wait().until(
            EC.presence_of_element_located(
                self.locators["news_feed_container"])
        )
        self.get_wait().until(
            EC.presence_of_all_elements_located(
                self.locators["news_cards_raw"])
        )

    def get_cards_raw(self) -> List[WebElement]:
        """Return list of raw card WebElements."""
        return self.driver.find_elements(*self.locators["news_cards_raw"])

    @allure.step("Get news cards count")
    def get_cards_count(self) -> int:
        """Return number of visible news cards."""
        return len(self.get_cards_raw())

    @allure.step("Verify each visible news card has a title")
    def each_card_has_title(self) -> bool:
        """Verify each visible card contains non-empty title text."""
        cards = self.get_cards_raw()
        if not cards:
            return False

        for card in cards:
            titles = card.find_elements(*self.locators["card_title_relative"])
            if not titles:
                return False
            if not any((t.text or "").strip() for t in titles):
                return False
        return True

    @allure.step("Verify each visible news card has metadata (date/author/tags)")
    def each_card_has_metadata(self) -> bool:
        """Verify each visible card contains some metadata (date/time/author/tags)."""
        cards = self.get_cards_raw()
        if not cards:
            return False

        for card in cards:
            metas = card.find_elements(*self.locators["card_meta_relative"])
            if not metas:
                return False
            if not any((m.text or m.get_attribute("datetime") or "").strip() for m in metas):
                return False
        return True

    @allure.step("Scroll to bottom")
    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the page."""
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Refresh Eco News page")
    def refresh(self) -> None:
        """Refresh the page and wait until it is loaded again."""
        self.driver.refresh()
        self.wait_page_loaded()

    @allure.step("Wait cards count at least {expected_min}")
    def wait_cards_count_at_least(self, expected_min: int) -> bool:
        """Wait until cards count is at least expected_min. Return True if ok, else False."""
        try:
            self.get_wait().until(
                lambda d: len(d.find_elements(
                    *self.locators["news_cards_raw"])) >= expected_min
            )
            return True
        except TimeoutException:
            return False

    # TC-EN-02: Open Eco News article and verify details #162
    @allure.step("Open first news card")
    def open_first_news_card(self) -> OneNewsPage:
        """Open the first visible news card."""
        self.wait_cards_present()
        first_card = self.get_cards_raw()[0]
        first_card.click()
        return OneNewsPage(self.driver)

    @allure.step("Get first news card title")
    def get_first_card_title(self) -> str:
        """Return title text of the first visible news card."""
        self.wait_cards_present()
        first_card = self.get_cards_raw()[0]
        titles = first_card.find_elements(*self.locators["card_title_relative"])

        for title in titles:
            text = title.text.strip()
            if text:
                return text
        return ""

    # TC-EN-03: Create Eco News and verify it appears in the feed #163
    @allure.step("Check if news with title '{title}' is present in feed")
    def is_news_present_in_feed(self, title: str) -> bool:
        """Check if news with given title is present in the feed."""
        self.wait_cards_present()
        cards = self.get_cards_raw()
        for card in cards:
            titles = card.find_elements(*self.locators["card_title_relative"])
            for item in titles:
                if item.text.strip() == title.strip():
                    return True
        return False

    @allure.step("Open news card with title '{title}'")
    def open_news_by_title(self, title: str) -> OneNewsPage:
        """Open news card with the given title."""
        cards = self.get_cards_raw()
        for card in cards:
            titles = card.find_elements(*self.locators["card_title_relative"])
            for item in titles:
                if item.text.strip() == title.strip():
                    item.click()
                    return OneNewsPage(self.driver)
        raise ValueError(f"News with title '{title}' was not found in feed.")

    @allure.step("Scroll until news with title '{title}' is found")
    def scroll_until_news_found(self, title: str, attempts: int = 5) -> bool:
        """Scroll several times until news with given title is found."""
        for _ in range(attempts):
            if self.is_news_present_in_feed(title):
                return True
            self.scroll_to_bottom()
            self.wait_cards_present()
        return False

    def is_loaded(self) -> bool:
        """Backward-compatible alias."""
        return self.is_page_opened()

    @allure.step("Checking if Eco News page title is visible")
    def is_title_visible(self) -> bool:
        """Check if Eco News page title is visible."""
        return self.title.is_displayed()

    @allure.step("Checking if Eco News feed is visible")
    def is_news_feed_visible(self) -> bool:
        """Check if Eco News feed is visible."""
        return self.main_header.is_displayed()

    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.driver.current_url
