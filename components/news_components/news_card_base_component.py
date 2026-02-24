"""Base news card class component module"""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from components.base_component import BaseComponent
from pages.news_pages.one_news_page import OneNewsPage


class NewsCardBaseComponent(BaseComponent):
    """Base news card class component

    Base class for vertical and horizontal news card components"""

    @allure.step("Navigate to OneNewsPage")
    def navigate_to_one_news_page(self, driver: WebDriver) -> OneNewsPage:
        """Navigate to OneNewsPage"""
        self.root.click()
        return OneNewsPage(driver)
