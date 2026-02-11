"""News Saved Page class"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.news_filter_component import NewsFilterComponent
from components.news_list_component import NewsListComponent

from utils.types import Locators


class NewsPage(BasePage):
    """News Page class."""
    tag_filter_root: Locators = (By.CSS_SELECTOR, "app-tag-filter")

    def __init__(self, driver):
        super().__init__(driver)
        root = self.driver.find_element(*self.tag_filter_root)
        self.tag_filter = NewsFilterComponent(root)
        self.news_list = NewsListComponent(root)

    def news_filter_component(self) -> NewsFilterComponent:
        """Retue NewsFilterComponent instance."""
        return self.tag_filter

    def news_list_component(self) -> NewsListComponent:
        """Reture NewsListComponent instance."""
        return self.news_list
