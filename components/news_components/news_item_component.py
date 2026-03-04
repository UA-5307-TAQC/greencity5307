"""Component representing single news item in news list."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class NewsItemComponent(BaseComponent):
    """Single news card component."""

    title: Locators = (By.CSS_SELECTOR, "h3")
    description: Locators = (By.CSS_SELECTOR, ".list-text")
    author: Locators = (By.CSS_SELECTOR, ".user-data-text-date .mw")
    date: Locators = (By.CSS_SELECTOR, ".user-data-text-date.text-nowrap span")
    likes: Locators = (By.XPATH, ".//img[@alt='likes']/following-sibling::span")
    comments: Locators = (By.XPATH, ".//img[@alt='comments']/following-sibling::span")
    link: Locators = (By.CSS_SELECTOR, "a.link")

    def get_title(self) -> str:
        """Get the title of the news card."""
        return self.root.find_element(*self.title).text.strip()

    def get_description(self) -> str:
        """Get the description of the news card."""
        return self.root.find_element(*self.description).text.strip()

    def get_author(self) -> str:
        """Get the author of the news card."""
        return self.root.find_element(*self.author).text.strip()

    def get_date(self) -> str:
        """Get the date of the news card."""
        return self.root.find_element(*self.date).text.strip()

    def get_likes(self) -> int:
        """Get the number of likes of the news card."""
        return int(self.root.find_element(*self.likes).text)

    def get_comments(self) -> int:
        """Get the number of comments of the news card."""
        return int(self.root.find_element(*self.comments).text)

    def open(self):
        """Click news item link."""
        self.root.find_element(*self.link).click()
