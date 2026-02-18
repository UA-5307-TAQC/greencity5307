"""Page object for the Eco News page."""

from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.news_components.news_card_base_component import NewsCardBaseComponent
from pages.base_page import BasePage

class EcoNewsPage(BasePage):
    """Page object for the Eco News page."""

    locators = {
        "main_header": (By.CSS_SELECTOR, ".cont >.main-header", WebElement),
        "_news_card_item": (By.CSS_SELECTOR,
                            ".ng-star-inserted .gallery-view-li-active", NewsCardBaseComponent)
    }

    main_header: WebElement

    @property
    def news_cards(self) -> list[NewsCardBaseComponent]:
        """ Return the list of news cards """
        return self.resolve_list("_news_card_item")

    def get_news_count(self) -> int:
        """Example method using the lazy list."""
        return len(self.news_cards)
