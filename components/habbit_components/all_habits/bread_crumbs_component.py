"""This module contains the BreadCrumbsComponent class."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class BreadCrumbsComponent(BaseComponent):
    """Component class for navigation breadcrumbs."""

    back_link_locator: Locators = (By.CLASS_NAME, "back-button")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.back_link = self.root.find_element(*self.back_link_locator)

    def click_back(self):
        """Click the back link to return to the previous page."""
        self.back_link.click()
