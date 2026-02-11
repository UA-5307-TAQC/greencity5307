"""News Saved Page class"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.news_filter_component import NewsFilterComponent
from components.news_list_component import NewsListComponent
from components.change_view_component import ChangeViewComponent

from utils.types import Locators


class NewsPage(BasePage):
    """News Page class."""
    tag_filter_root: Locators = (By.CSS_SELECTOR, "app-tag-filter")
    change_view_root: Locators = (By.CSS_SELECTOR, "app-change-view-button")

    def __init__(self, driver):
        super().__init__(driver)
        root = self.driver.find_element(*self.tag_filter_root)
        self.tag_filter = NewsFilterComponent(root)
        self.news_list = NewsListComponent(root)

        view_root = self.driver.find_element(*self.change_view_root)
        self.change_view = ChangeViewComponent(view_root)

    def get_news_filter_component(self) -> NewsFilterComponent:
        """Retue NewsFilterComponent instance."""
        return self.tag_filter

    def get_news_list_component(self) -> NewsListComponent:
        """Reture NewsListComponent instance."""
        return self.news_list

    def get_change_view_component(self) -> ChangeViewComponent:
        """Retur ChangeViewComponent instance."""
        return self.change_view
