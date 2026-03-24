"""News Saved Page class"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract
from components.news_components.news_filter_component import NewsFilterComponent
from components.news_components.news_list_component import NewsListComponent
from components.common_components.change_view_component import ChangeViewComponent

from utils.custom_web_element import CustomWebElement


class NewsPage(SavedAbstract):
    """News Page class."""

    locators = {
        "tag_filter": (By.CSS_SELECTOR, "app-tag-filter", NewsFilterComponent),
        "change_view": (By.CSS_SELECTOR, "app-change-view-button", ChangeViewComponent),
        "news_list": (By.CSS_SELECTOR, ".list.gallery-view-active.ng-star-inserted",
                      NewsListComponent),
        "unfortunate_text": (By.CSS_SELECTOR, ".description__title")
    }

    tag_filter: NewsFilterComponent
    change_view: ChangeViewComponent
    news_list: NewsListComponent
    unfortunate_text: CustomWebElement

    def is_loaded(self):
        try:
            self.get_wait().until(
                EC.visibility_of_element_located(self.locators["tag_filter"][:2])
            )
            self.get_wait().until(
                lambda d: d.find_elements(*self.locators["news_list"][:2])
                or d.find_elements(*self.locators["unfortunate_text"][:2])
            )
            return True
        except TimeoutException:
            return False
