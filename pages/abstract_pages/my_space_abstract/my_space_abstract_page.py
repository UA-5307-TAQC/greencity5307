"""This module contains the MySpaceAbstractPage class,
which represents the layout of My Space page."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.abstract_pages_components.my_space_components \
    .abstract_page_components.calendar_component import CalendarComponent
from components.abstract_pages_components.my_space_components \
    .abstract_page_components.my_profile_data_banner_component \
    import MyProfileDataBannerComponent
from components.abstract_pages_components.my_space_components \
    .abstract_page_components.to_do_list_component import ToDoListComponent
from pages.abstract_pages.friends_abstract.friends_abstract_page import FriendsAbstractPage
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class MySpaceAbstractPage(BasePage):
    """Class for the layout of My Space page."""

    locators = {
        "profile_banner": (By.CSS_SELECTOR, "div.left-column",
                           MyProfileDataBannerComponent),
        "calendar": (By.CSS_SELECTOR, "div.calendar", CalendarComponent),
        "to_do_list": (By.XPATH, "(.//div[@class='to-do-list-block'])[2]", ToDoListComponent),
        "my_habits_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[1]"),
        "my_news_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[2]"),
        "my_events_tab": (By.XPATH, ".//div[@class='mat-mdc-tab-labels']/div[3]"),
        "content": (By.CSS_SELECTOR, "div.mat-mdc-tab-body-wrapper:nth-child(2)"),
        "user_name": (By.XPATH, "//app-profile-header/div/div/p[1]")
    }

    profile_banner: MyProfileDataBannerComponent
    calendar: CalendarComponent
    to_do_list: ToDoListComponent
    my_habits_tab: CustomWebElement
    my_news_tab: CustomWebElement
    my_events_tab: CustomWebElement
    content: CustomWebElement
    user_name: CustomWebElement

    @allure.step("Click on My habits tab on My Space page")
    def click_my_habits_tab(self) -> "MyHabitPage":
        """Click on My habits tab."""
        from pages.abstract_pages.my_space_abstract.my_habit_page import \
            MyHabitPage  # pylint: disable=import-outside-toplevel
        self.my_habits_tab.wait_and_click()
        self.get_wait().until(EC.visibility_of(self.content))
        return MyHabitPage(self.driver)

    @allure.step("Click on My news tab on My Space page")
    def click_my_news_tab(self) -> "MyNewsPage":
        """Click on My news tab."""
        from pages.abstract_pages.my_space_abstract.my_news_page import \
            MyNewsPage  # pylint: disable=import-outside-toplevel
        self.my_news_tab.wait_and_click()
        self.get_wait().until(EC.visibility_of(self.content))
        return MyNewsPage(self.driver)

    @allure.step("Click on My events tab on My Space page")
    def click_my_events_tab(self) -> "MyEventsPage":
        """Click on My events tab."""
        from pages.abstract_pages.my_space_abstract.my_events import MyEventsPage # pylint: disable=import-outside-toplevel
        self.my_events_tab.wait_and_click()
        self.get_wait().until(EC.visibility_of(self.content))
        return MyEventsPage(self.driver)

    def click_friends_tab(self):
        """Click on Friends tab."""
        self.profile_banner.click_add_friends_btn()
        return FriendsAbstractPage(self.driver)
