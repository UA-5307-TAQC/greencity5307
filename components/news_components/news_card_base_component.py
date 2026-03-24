"""Base news card class component module"""

import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from pages.news_pages.one_news_page import OneNewsPage
from utils.custom_web_element import CustomWebElement


class NewsCardBaseComponent(BaseComponent):
    """Base news card class component

    Base class for vertical and horizontal news card components"""

    locators = {
        "link": (By.CSS_SELECTOR, "li > a"),
    }

    link: CustomWebElement

    @allure.step("Navigate to OneNewsPage")
    def navigate_to_one_news_page(self) -> OneNewsPage:
        """Navigate to OneNewsPage"""
        self.root.click()
        return OneNewsPage(self.root.parent)
