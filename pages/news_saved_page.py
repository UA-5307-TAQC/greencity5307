"""News Saved Page class"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.news_filter_component import NewsFilterComponent
from components.news_list_component import NewsListComponent
from components.change_view_component import ChangeViewComponent


class NewsPage(BasePage):
    """News Page class."""

    locators = {
        "tag_filter": (By.CSS_SELECTOR, "app-tag-filter"),
        "change_view": (By.CSS_SELECTOR, "app-change-view-button"),
        "news_list": (By.CSS_SELECTOR, "list gallery-view-active ng-star-inserted"),
    }

    tag_filter: NewsFilterComponent
    change_view: ChangeViewComponent
    news_list: NewsListComponent
