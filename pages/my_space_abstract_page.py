"""This module contains the MySpaceAbstractPage class,
which represents the layout of My Space page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from components.calendar_component import CalendarComponent
from components.my_profile_data_banner_component import MyProfileDataBannerComponent
from components.to_do_list_component import ToDoListComponent
from pages.base_page import BasePage


class MySpaceAbstractPage(BasePage):
    """Class for the layout of My Space page."""

    locators = {
        "profile_root": (By.CSS_SELECTOR, "div.profile-container"),
        "my_habits_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[1]"),
        "my_news_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[2]"),
        "my_events_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[3]")
    }

    # Type hints для IDE
    profile_root: WebElement
    my_habits_tab: WebElement
    my_news_tab: WebElement
    my_events_tab: WebElement

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.profile_banner: MyProfileDataBannerComponent = \
            MyProfileDataBannerComponent(self.profile_root)

        self.calendar: CalendarComponent = \
            CalendarComponent(self.profile_root)

        self.to_do_list: ToDoListComponent = \
            ToDoListComponent(self.profile_root)

    @allure.step("Click on My habits tab on My Space page")
    def click_my_habits_tab(self):
        """Click on My habits tab."""
        self.my_habits_tab.wait_and_click()

    @allure.step("Click on My news tab on My Space page")
    def click_my_news_tab(self):
        """Click on My news tab."""
        self.my_news_tab.wait_and_click()

    @allure.step("Click on My events tab on My Space page")
    def click_my_events_tab(self):
        """Click on My events tab."""
        self.my_events_tab.wait_and_click()
