"""This module contains the OneNewsPage class, which represents the One News page of the website."""
import allure
from selenium.webdriver.common.by import By

from components.common_components.likes_component import LikesComponent
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement
from utils.logger import logger


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

    tag: CustomWebElement
    title: CustomWebElement
    creation_date: CustomWebElement
    author: CustomWebElement
    likes: LikesComponent
    main_text: CustomWebElement
    comments_section: CustomWebElement

    @allure.step("Get news author")
    def get_author(self) -> bool:
        """Check if object is liked"""
        author = self.author.text
        logger.info("Author: %s", author)
        return author
