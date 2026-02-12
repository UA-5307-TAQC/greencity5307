"""This module contains the CreateUpdateEcoNewsPage class,
which represents the create_update_eco_news page of a website."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.types import Locators


class CreateUpdateEcoNewsPage(BasePage):
    """Page object for the create_update_eco_news page."""

    section_header: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/h2")
    section_description: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/p")
    title: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[1]")
    tags: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[2]")
    source: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[3]")
    picture: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]")
    content: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[2]")

    date: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[3]")
    submit: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[4]")

    def fill_form(self, title_text, tags_list, source_text, image_path, content_text):  # pylint: disable=too-many-positional-arguments
        """Fills the form with the given parameters."""
        self.find(self.title).send_keys(title_text)
        self.find(self.tags).send_keys(tags_list)
        self.find(self.source).send_keys(source_text)
        self.find(self.picture).send_keys(image_path)
        self.find(self.content).send_keys(content_text)

    def submit_form(self):
        """Submits the form by clicking the submit button."""
        self.click(self.submit)
