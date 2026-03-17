"""This module contains the OneNewsPage class, which represents the One News page of the website."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.common_components.likes_component import LikesComponent
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class OneNewsPage(BasePage):
    """Page object for the One News page."""

    locators = {
        "tag": (By.CSS_SELECTOR, ".tags > .tags-item"),
        "title": (By.CSS_SELECTOR, ".news-title.word-wrap"),
        "creation_date": (By.CSS_SELECTOR, ".news-info > .news-info-date"),
        "author": (By.CSS_SELECTOR, ".news-info > .news-info-author"),
        "likes": (By.CSS_SELECTOR, ".news-info > .like_wr", LikesComponent),
        "main_text": (By.CSS_SELECTOR, ".ql-editor"),
        "comments_section": (By.TAG_NAME, "app-comments-container"),
    }

    tag: CustomWebElement
    title: CustomWebElement
    creation_date: CustomWebElement
    author: CustomWebElement
    likes: LikesComponent
    main_text: CustomWebElement
    comments_section: CustomWebElement

    def get_tag(self) -> str:
        """Gets tag text of the news page."""
        return self.tag.text

    def get_title(self) -> str:
        """Gets title text of the news page."""
        return self.title.text

    def get_creation_date(self) -> str:
        """Gets creation date text of the news page."""
        return self.creation_date.text

    def get_author(self) -> str:
        """Gets author text of the news page."""
        return self.author.text

    def get_main_text(self) -> str:
        """Gets main text's text of the news page."""
        return self.main_text.text

    @allure.step("Wait until One News page is loaded")
    def wait_page_loaded(self) -> None:
        """Wait until One News page is loaded."""
        self.get_wait().until(EC.url_contains("/news/"))
        self.get_wait().until(
            EC.visibility_of_element_located(self.locators["title"])
        )

    @allure.step("Get current One News page URL")
    def get_current_url(self) -> str:
        """Return current page URL."""
        return self.driver.current_url

    @allure.step("Check title is visible")
    def is_title_visible(self) -> bool:
        """Check if title is visible."""
        return self.title.is_displayed()

    @allure.step("Check main text is visible")
    def is_main_text_visible(self) -> bool:
        """Check if main text is visible."""
        return self.main_text.is_displayed()

    @allure.step("Check creation date is visible")
    def is_creation_date_visible(self) -> bool:
        """Check if creation date is visible."""
        return self.creation_date.is_displayed()
