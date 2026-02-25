"""This module contains the MySpaceAbstractPage class,
which represents the layout of My Space page."""

import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.types import Locators


class MySpaceAbstractPage(BasePage):
    """Class for the layout of My Space page."""
    profile_root_locator: Locators = (By.CSS_SELECTOR, "div.profile-container")
    my_habits_tab_locator: Locators = (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[1]")
    my_news_tab_locator: Locators = (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[2]")
    my_events_tab_locator: Locators = (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[3]")


    @allure.step("Click on My habits tab on My Space page")
    def click_my_habits_tab(self):
        """Click on My habits tab."""
        self.my_habits_tab.click()

    @allure.step("Click on My news tab on My Space page")
    def click_my_news_tab(self):
        """Click on My news tab."""
        self.my_news_tab.click()

    @allure.step("Click on My events tab on My Space page")
    def click_my_events_tab(self):
        """Click on My events tab."""
        self.my_events_tab.click()
