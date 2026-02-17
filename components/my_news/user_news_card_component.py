"""This module contains the UserNewsCardComponent class."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class UserNewsCardComponent(BaseComponent):
    """Component representing a single news card created by the user."""

    title_locator: Locators = (By.CSS_SELECTOR, "div.title")
    date_locator: Locators = (By.CSS_SELECTOR, "div.user-info")
    image_locator: Locators = (By.CSS_SELECTOR, "img.news-image")
    tags_locator: Locators = (By.CSS_SELECTOR, "div.tags")


    def __init__(self, root: WebElement):
        super().__init__(root)
        self.title_element = self.root.find_element(*self.title_locator)
        self.date_element = self.root.find_element(*self.date_locator)
        self.tags_element = self.root.find_element(*self.tags_locator)

    def get_title(self) -> str:
        """Returns the news title text."""
        return self.title_element.text.strip()

    def get_date_text(self) -> str:
        """Returns the text from user-info block."""
        return self.date_element.text.strip()

    def get_tags_text(self) -> str:
        """Returns the tags text."""
        return self.tags_element.text.strip()
