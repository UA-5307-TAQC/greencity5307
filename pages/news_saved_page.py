"""News Saved Page class"""

from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.news_filter_component import NewsFilterComponent
from utils.types import Locators

class NewsPage(BasePage):
    """News Page class."""
    tag_filter_root: Locators = (By.CSS_SELECTOR, "app-tag-filter")

    def __init__(self, driver):
        super().__init__(driver)
        root = self.driver.find_element(*self.tag_filter_root)
        self.tag_filter = NewsFilterComponent(root)

    def news_filter_component(self) -> NewsFilterComponent:
        """Retue NewsFilterComponent instance."""
        return self.tag_filter
