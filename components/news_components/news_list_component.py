"""Component representing news list."""

from typing import List
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from components.news_components.news_item_component import NewsItemComponent
from utils.types import Locators


class NewsListComponent(BaseComponent):
    """Component representing list of news."""

    news_items: Locators = (By.CSS_SELECTOR, "ul[aria-label='news list'] > li")

    def get_all_news(self) -> List[NewsItemComponent]:
        """Return all news items."""
        elements = self.root.find_elements(*self.news_items)
        return [NewsItemComponent(el) for el in elements]

    def get_news_by_title(self, title: str) -> NewsItemComponent:
        """Return news by title."""
        for item in self.get_all_news():
            if item.get_title() == title:
                return item
        raise ValueError(f"News with title '{title}' not found.")
