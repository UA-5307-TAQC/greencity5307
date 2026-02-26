"""This module contains the MyProfileDataBannerComponent class,
 which represents the user data banner of the My Space page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from pages.edit_profile_page import ProfileEditPage
from pages.all_friends_page import AllFriendsPage
from utils.custom_web_element import CustomWebElement


class MyProfileDataBannerComponent(BaseComponent):
    """Component class for the user data banner of the My Space page."""

    locators = {
        "edit_btn": (By.CSS_SELECTOR, "a.edit-icon"),
        "username": (By.CSS_SELECTOR, "p.name"),
        "acquired_habits": (By.XPATH, ".//div[@class='chain'][1]/p[1]"),
        "habits_in_prog": (By.XPATH, ".//div[@class='chain'][2]/p[1]"),
        "news": (By.XPATH, ".//div[@class='chain'][3]/p[1]"),
        "events": (By.XPATH, ".//div[@class='chain'][4]/p[1]"),
        "add_friends_btn": (By.CSS_SELECTOR, "div.add-friends")
    }

    edit_btn: CustomWebElement
    username: CustomWebElement
    acquired_habits: CustomWebElement
    habits_in_prog: CustomWebElement
    news: CustomWebElement
    events: CustomWebElement
    add_friends_btn: CustomWebElement

    @allure.step("Click on Edit profile button on Profile Banner component")
    def click_edit_btn(self) -> ProfileEditPage:
        """Click on edit profile button."""
        self.edit_btn.wait_and_click()
        WebDriverWait(self.root.parent, 10).until(EC.url_contains("edit"))
        return ProfileEditPage(self.root.parent)


    @allure.step("Click on Add friends button on Profile Banner component")
    def click_add_friends_btn(self) -> AllFriendsPage:
        """Click on Add friends button."""
        self.add_friends_btn.wait_and_click()
        WebDriverWait(self.root.parent, 10).until(EC.url_contains("friends"))
        return AllFriendsPage(self.root.parent)

    @allure.step("Get username from Profile Banner component")
    def get_username(self) -> str:
        """Get username."""
        return self.username.text

    @allure.step("Get profile progress from Profile Banner component")
    def get_profile_progress(self) -> dict:
        """Get profile progress."""
        return {
            "acquired habits": self.acquired_habits.text,
            "habits in progress": self.habits_in_prog.text,
            "published news": self.news.text,
            "organized and attended events": self.events.text
        }
