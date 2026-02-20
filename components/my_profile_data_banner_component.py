"""This module contains the MyProfileDataBannerComponent class,
 which represents the user data banner of the My Space page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.types import Locators


class MyProfileDataBannerComponent(BaseComponent):
    """Component class for the  user data banner of the My Space page."""
    edit_btn_locator: Locators = (By.CSS_SELECTOR, "a.edit-icon")
    username_locator: Locators = (By.CSS_SELECTOR, "p.name")
    add_friends_btn_locator: Locators = (By.CSS_SELECTOR, "div.add-friends")

    acquired_habits_locator: Locators = (By.XPATH, ".//div[@class='chain'][1]/p[1]")
    habits_in_prog_locator: Locators = (By.XPATH, ".//div[@class='chain'][2]/p[1]")
    news_locator: Locators = (By.XPATH, ".//div[@class='chain'][3]/p[1]")
    events_locator: Locators = (By.XPATH, ".//div[@class='chain'][4]/p[1]")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.edit_btn = self.root.find_element(*self.edit_btn_locator)
        self.username = self.root.find_element(*self.username_locator)
        self.add_friends_btn = self.root.find_element(*self.add_friends_btn_locator)

        self.acquired_habits = self.root.find_element(*self.acquired_habits_locator)
        self.habits_in_prog = self.root.find_element(*self.habits_in_prog_locator)
        self.news = self.root.find_element(*self.news_locator)
        self.events = self.root.find_element(*self.events_locator)

    @allure.step("Click on Edit profile button on Profile Banner component")
    def click_edit_btn(self, driver):
        """Click on edit profile button."""
        self.edit_btn.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("edit")
        )

    @allure.step("Get username from Profile Banner component")
    def get_username(self) -> str:
        """Get username."""
        return self.username.text

    @allure.step("Click on Add friends button on Profile Banner component")
    def click_add_friends_btn(self):
        """Click on add friends button."""
        self.add_friends_btn.click()
        from pages.find_friend_page import FindFriendPage  # pylint: disable=import-outside-toplevel
        return FindFriendPage(self.root.parent)


    @allure.step("Get profile progress from Profile Banner component")
    def get_profile_progress(self) -> dict:
        """Get profile progress."""
        progress = {
            "acquired habits": self.acquired_habits.text,
            "habits in progress": self.habits_in_prog.text,
            "published news": self.news.text,
            "organized and attended events": self.events.text
        }
        return progress
