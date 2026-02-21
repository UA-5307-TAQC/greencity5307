"""This module contains the AboutUsPage class,which represents the about_us page of a website."""
from selenium.webdriver.common.by import By

from components.about_us_buttons_component import AboutUsPageHabitButtonOneComponent, \
    AboutUsPageHabitButtonTwoComponent
from pages.base_page import BasePage
from pages.my_habit_page import MyHabitPage
from utils.types import Locators


class AboutUsPage(BasePage):
    """Page object for the about_us page."""

    section_header_one: Locators = (By.XPATH, "//*[@id='main-content']/div[1]/div/h2")
    section_description_one: Locators = (By.XPATH, "//*[@id='main-content']/div[1]/div/p")
    section_button_form_habit_one: Locators = (By.CSS_SELECTOR,
        "#main-content > div.about-section.section > div > button")

    section_header_two: Locators = (By.XPATH, "//*[@id='main-content']/div[2]/div/div/h2")
    section_description_two: Locators = (By.XPATH, "//*[@id='main-content']/div[2]/div/div/p")
    section_button_form_habit_two: Locators = (By.XPATH,
                                               "//*[@id='main-content']/div[2]/div/div/button")

    vision_section_header: Locators = (By.XPATH, "//*[@id='main-content']/div[3]/div/h2")

    vision_cards: Locators = (By.CSS_SELECTOR, ".container > .vision-card")

    def get_button_one_component(self):
        """Get the locator for the create news button."""
        return AboutUsPageHabitButtonOneComponent(self.find(self.section_button_form_habit_one))
    def get_button_two_component(self):
        """Get the locator for the create news button."""
        return AboutUsPageHabitButtonTwoComponent(self.find(self.section_button_form_habit_two))

    def click_section_button_form_habit_one(self):
        """Click the form habit button one and return my habits page."""
        self.get_button_one_component().click_form_habit_button_one()
        return MyHabitPage(self.driver)

    def click_section_button_form_habit_two(self):
        """Click the form habit button two and return my habits page."""
        self.get_button_two_component().click_form_habit_button_two()
        return MyHabitPage(self.driver)

    def get_vision_cards_count(self):
        """Gets the number of vision cards present in the section."""
        return len(self.find_all(self.vision_cards))

    def is_page_loaded(self):
        """Checks if the page is loaded."""
        return self.driver.find_element(*self.vision_cards).is_displayed()
