"""This module contains the SavedAbstract class,
which represents the saved_abstract page of a website."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators


class SavedAbstract(BasePage):
    """Page object for the saved_abstract page."""

    main_header_locator: Locators = (By.CSS_SELECTOR, ".top-header>.main-header")
    main_footer_locator: Locators = (By.XPATH, "///app-footer")

    section_heading= (By.XPATH, "//*[@id='main-content']/div/app-saved-section/div/p")
    tabs = (By.CSS_SELECTOR, ".tabs")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)
        self.main_footer = self.driver.find_element(*self.main_footer_locator)

    def open_tab(self, index: int):
        self.find_all(self.tabs)[index].click()

    def get_section_heading(self):
        return self.find(self.section_heading).text

    def is_loaded(self):
        return self.find_all(self.tabs)[0].is_displayed()