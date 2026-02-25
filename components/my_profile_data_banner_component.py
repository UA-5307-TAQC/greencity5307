"""This module contains the MyProfileDataBannerComponent class,
 which represents the user data banner of the My Space page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.types import Locators


class MyProfileDataBannerComponent(BaseComponent):
    """Component class for the  user data banner of the My Space page."""
    edit_btn_locator: Locators = (By.CSS_SELECTOR, "a.edit-icon")
    username_locator: Locators = (By.CSS_SELECTOR, "p.name")
    acquired_habits_locator: Locators = (By.XPATH, ".//div[@class='chain'][1]/p[1]")
    habits_in_prog_locator: Locators = (By.XPATH, ".//div[@class='chain'][2]/p[1]")
    news_locator: Locators = (By.XPATH, ".//div[@class='chain'][3]/p[1]")
    events_locator: Locators = (By.XPATH, ".//div[@class='chain'][4]/p[1]")


    @allure.step("Click on Edit profile button on Profile Banner component")
    def click_edit_btn(self, driver):
        """Click on edit profile button."""
        self.edit_btn.click()

        WebDriverWait(driver, 10).until(EC.url_contains("edit"))

    @allure.step("Get username from Profile Banner component")
    def get_username(self) -> str:
        """Get username."""
        return self.username.text

    @allure.step("Get profile progress from Profile Banner component")
    def get_profile_progress(self) -> dict:
        """Get profile progress."""
        progress = {"acquired habits": self.acquired_habits.text,
                    "habits in progress": self.habits_in_prog.text,
                    "published news": self.news.text,
                    "organized and attended events": self.events.text}
        return progress
