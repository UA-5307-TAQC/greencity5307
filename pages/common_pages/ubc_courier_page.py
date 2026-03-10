"""This module contains the MainPage class, which represents the main page of the application.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the main page elements."""
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.types import Locators


class UBSCourierPage(BasePage):
    """Page object for the UBSCourier page."""

    nowaste_shop_locator: Locators = (
        By.CSS_SELECTOR,
        "section.our-partners-section a[href*='shop.nowaste']"
    )

    nowaste_locator: Locators = (
        By.CSS_SELECTOR,
        "section.our-partners-section a[href='https://nowaste.com.ua/']"
    )

    goto_locator: Locators = (
        By.CSS_SELECTOR,
        "section.our-partners-section a[href*='goto.recycling']"
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.nowaste_shop_button: WebElement = self.driver.find_element(*self.nowaste_shop_locator)
        self.nowaste_button: WebElement = self.driver.find_element(*self.nowaste_locator)
        self.goto_button: WebElement = self.driver.find_element(*self.goto_locator)

    @allure.step("Click Nowaste shop partner")
    def click_nowaste_shop(self):
        """Open Nowaste shop."""
        self.nowaste_shop_button.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Click Nowaste partner")
    def click_nowaste(self):
        """Open Nowaste website."""
        self.nowaste_button.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Click GoTo Recycling partner")
    def click_goto(self):
        """Open GoTo Recycling Instagram."""
        self.goto_button.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])