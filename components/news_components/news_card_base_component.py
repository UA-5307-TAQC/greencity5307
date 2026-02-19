"""Base news card class component module"""
import allure
from components.base_component import BaseComponent
from pages.news_pages.one_news_page import OneNewsPage


class NewsCardBaseComponent(BaseComponent):
    """Base news card class component"""

    locators = {}

    @allure.step("Navigate to one news page")
    def navigate_to_one_news_page(self) -> "OneNewsPage":
        """Navigate to one news page"""

        self.wait_and_click("root")

        return OneNewsPage(self.driver)
