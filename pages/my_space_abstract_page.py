"""This module contains the MySpaceAbstractPage class,
which represents the layout of My Space page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from components.calendar_component import CalendarComponent
from components.my_profile_data_banner_component import MyProfileDataBannerComponent
from components.to_do_list_component import ToDoListComponent
from pages.base_page import BasePage
from utils.types import Locators


class MySpaceAbstractPage(BasePage):
    """Class for the layout of My Space page."""
    profile_root_locator: Locators = (By.CLASS_NAME, "profile-container")
    my_habits_tab_locator: Locators = (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[1]")
    my_news_tab_locator: Locators = (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[2]")
    my_events_tab_locator: Locators = (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[3]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.my_habits_tab: WebElement = self.driver.find_element(*self.my_habits_tab_locator)
        self.my_news_tab: WebElement = self.driver.find_element(*self.my_news_tab_locator)
        self.my_events_tab: WebElement = self.driver.find_element(*self.my_events_tab_locator)
        profile_root = self.driver.find_element(*self.profile_root_locator)
        self.profile_banner: MyProfileDataBannerComponent = \
            MyProfileDataBannerComponent(profile_root)
        self.calendar: CalendarComponent = CalendarComponent(profile_root)
        self.to_do_list: ToDoListComponent = ToDoListComponent(profile_root)

    def click_my_habits_tab(self):
        """Click on My habits tab."""
        self.my_habits_tab.click()

    def click_my_news_tab(self):
        """Click on My news tab."""
        self.my_news_tab.click()

    def click_my_events_tab(self):
        """Click on My events tab."""
        self.my_events_tab.click()
