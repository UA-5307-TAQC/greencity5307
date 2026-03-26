"""This module contains the UBSCourierPage class representing the UBS Courier page.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the UBS Courier page elements."""
import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class UBSCourierPage(BasePage):
    """Page object for the UBSCourier page."""

    locators = {
        "nowaste_shop_button": (
            By.CSS_SELECTOR,
            "section.our-partners-section a[href*='shop.nowaste']",
        ),
        "nowaste_button": (
            By.CSS_SELECTOR,
            "section.our-partners-section a[href='https://nowaste.com.ua/']",
        ),
        "goto_button": (
            By.CSS_SELECTOR,
            "section.our-partners-section a[href*='goto.recycling']",
        ),
    }

    # Type annotations only – elements are resolved lazily by the Factory.
    nowaste_shop_button: CustomWebElement
    nowaste_button: CustomWebElement
    goto_button: CustomWebElement

    @allure.step("Click Nowaste shop partner")
    def click_nowaste_shop(self):
        """Open Nowaste shop."""
        self.nowaste_shop_button.wait_and_click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Click Nowaste partner")
    def click_nowaste(self):
        """Open Nowaste website."""
        self.nowaste_button.wait_and_click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Click GoTo Recycling partner")
    def click_goto(self):
        """Open GoTo Recycling Instagram."""
        self.goto_button.wait_and_click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
