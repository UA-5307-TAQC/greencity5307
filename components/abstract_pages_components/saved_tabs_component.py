"""Saved tabs component"""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class SavedTabsComponent(BaseComponent):
    """Saved tabs component."""
    locators = {
        "eco_news_tab": (By.XPATH, "//*[@id='main-content']/"
                                   "div/app-saved-section/div/div/button[1]"),
        "events_tab": (By.XPATH, "//*[@id='main-content']/div/app-saved-section/div/div/button[2]"),
        "places_tab": (By.XPATH, "//*[@id='main-content']/div/app-saved-section/div/div/button[3]")
    }
    eco_news_tab: CustomWebElement
    events_tab: CustomWebElement
    places_tab: CustomWebElement

    def click_tab_by_name(self, name: str):
        """Click on a tab by its name."""
        tab = self.root.find_element(
            By.XPATH,
            f".//button[normalize-space()='{name}']"
        )
        tab.click()
