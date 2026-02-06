"""This module contains the AboutUsPage class,which represents the about_us page of a website."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators


class AboutUsPage(BasePage):
    """Page object for the about_us page."""

    main_header_locator: Locators = (By.CSS_SELECTOR, ".top-header>.main-header")
    main_footer_locator: Locators = (By.XPATH, "//app-footer")

    section_header_one = (By.XPATH, "//*[@id='main-content']/div[1]/div/h2")
    section_description_one = (By.XPATH, "//*[@id='main-content']/div[1]/div/p")
    section_button_form_habit_one = (By.XPATH, "//*[@id='main-content']/div[1]/div/button")

    section_header_two = (By.XPATH, "//*[@id='main-content']/div[2]/div/div/h2")
    section_description_two = (By.XPATH, "//*[@id='main-content']/div[2]/div/div/p")
    section_button_form_habit_two = (By.XPATH, "//*[@id='main-content']/div[2]/div/div/button")

    vision_section_header = (By.XPATH, "//*[@id='main-content']/div[3]/div/h2")

    vision_cards = (By.CSS_SELECTOR, ".vision-gallery")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)
        self.main_footer = self.driver.find_element(*self.main_footer_locator)

    def click_section_button_form_habit_one(self):
        """Clicks the section button form habit."""
        self.click(self.section_button_form_habit_one)

    def get_vision_cards_count(self):
        """Gets the number of vision cards present in the section."""
        return len(self.find_all(self.vision_cards))

    def is_page_loaded(self):
        return self.is_visible(self.vision_cards)
