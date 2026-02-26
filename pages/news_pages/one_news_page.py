"""This module contains the OneNewsPage class, which represents the One News page of the website."""
from selenium.webdriver.common.by import By

from components.common_components.likes_component import LikesComponent
from pages.base_page import BasePage


class OneNewsPage(BasePage):
    """Page object for the One News page."""
    locators = {
        "tag": (By.CSS_SELECTOR, ".tags > .tags-item"),
        "title": (By.CSS_SELECTOR, ".news-title.word-wrap"),
        "creation_date": (By.CSS_SELECTOR, ".news-info > .news-info-date"),
        "author": (By.CSS_SELECTOR, ".news-info > .news-info-author"),
        "likes": (By.CSS_SELECTOR, ".news-info > .like_wr", LikesComponent),
        "main_text": (By.CSS_SELECTOR, ".ql-editor"),
        "comments_section": (By.TAG_NAME, "app-comments-container")
    }

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
