"""This module contains the OneNewsPage class, which represents the One News page of the website."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.types import Locators


class OneNewsPage(BasePage):
    """Page object for the One News page."""
    tag_locator: Locators = (By.CSS_SELECTOR, ".tags > .tags-item")
    title_locator: Locators = (By.CSS_SELECTOR, ".news-title.word-wrap")
    creation_date_locator: Locators = (By.CSS_SELECTOR,
                                       ".news-info > .news-info-date")
    author_locator: Locators = (By.CSS_SELECTOR,
                                ".news-info > .news-info-author")
    main_text_locator: Locators = (By.CLASS_NAME, ".ql-editor")
    comments_section_locator: Locators = (By.TAG_NAME,
                                          "app-comments-container")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.tag: WebElement = self.driver.find_element(
            *self.tag_locator)
        self.title: WebElement = self.driver.find_element(
            *self.title_locator)
        self.creation_date: WebElement = self.driver.find_element(
            *self.creation_date_locator)
        self.author: WebElement = self.driver.find_element(
            *self.author_locator)
        self.main_text: WebElement = self.driver.find_element(
            *self.main_text_locator)
        self.comments_section: WebElement = self.driver.find_element(
            *self.comments_section_locator)

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
