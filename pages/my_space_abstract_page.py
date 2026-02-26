"""This module contains the MySpaceAbstractPage class,
which represents the layout of My Space page."""

import allure

from selenium.webdriver.common.by import By

from components.calendar_component import CalendarComponent
from components.my_profile_data_banner_component import MyProfileDataBannerComponent
from components.to_do_list_component import ToDoListComponent
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class MySpaceAbstractPage(BasePage):
    """Class for the layout of My Space page."""

    locators = {
        "profile_banner": (By.CSS_SELECTOR, "div.left-column", MyProfileDataBannerComponent),
        "calendar": (By.CSS_SELECTOR, "div.calendar", CalendarComponent),
        "to_do_list": (By.CSS_SELECTOR, "div.profile-container", ToDoListComponent),
        "my_habits_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[1]"),
        "my_news_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[2]"),
        "my_events_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[3]"),
        "content": (By.CSS_SELECTOR, "div.mat-mdc-tab-body-wrapper:nth-child(2)")
    }

    profile_banner: MyProfileDataBannerComponent
    calendar: CalendarComponent
    to_do_list: ToDoListComponent
    my_habits_tab: CustomWebElement
    my_news_tab: CustomWebElement
    my_events_tab: CustomWebElement
    content: CustomWebElement

    @allure.step("Click on My habits tab on My Space page")
    def click_my_habits_tab(self) -> "MyHabitPage":
        """Click on My habits tab."""
        from pages.my_habit_page import MyHabitPage # pylint: disable=import-outside-toplevel
        self.my_habits_tab.wait_and_click()
        self.find(self.locators["content"][:2])
        return MyHabitPage(self.driver)

    @allure.step("Click on My news tab on My Space page")
    def click_my_news_tab(self) -> "MyNewsPage":
        """Click on My news tab."""
        from pages.my_news_page import MyNewsPage # pylint: disable=import-outside-toplevel
        self.my_news_tab.wait_and_click()
        self.find(self.locators["content"][:2])
        return MyNewsPage(self.driver)

    @allure.step("Click on My events tab on My Space page")
    def click_my_events_tab(self):
        """Click on My events tab."""
        self.my_events_tab.wait_and_click()
