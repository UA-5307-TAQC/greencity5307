"""This module contains the MainPage class, which represents the main page of the application.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the main page elements."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class MainPage(BasePage):
    """Page object for the main page."""
    locators = {
        "there_are": (By.CSS_SELECTOR, "#stats > h2", WebElement)
    }

    there_are: WebElement
