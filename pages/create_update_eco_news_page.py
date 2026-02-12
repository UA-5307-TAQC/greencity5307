"""This module contains the CreateUpdateEcoNewsPage class,
which represents the create_update_eco_news page of a website."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from pages.base_page import BasePage
from utils.types import Locators


class CreateUpdateEcoNewsPage(BasePage):
    """Page object for the create_update_eco_news page."""

    section_header = (By.XPATH, "//*[@id='main-content']/div/div[1]/h2")
    section_description = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/p")
    title = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[1]")
    tags = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[2]")
    source = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[3]")
    picture = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]")
    content = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[2]")

    date = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[3]")
    submit = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[4]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)
        self.main_footer = self.driver.find_element(*self.main_footer_locator)

    def fill_form(self, title_text, tags_list, source_text, image_path, content_text):
        """Fills the form with the given parameters."""
        self.find(self.title).send_keys(title_text)
        self.find(self.tags).send_keys(tags_list)
        self.find(self.source).send_keys(source_text)
        self.find(self.picture).send_keys(image_path)
        self.find(self.content).send_keys(content_text)

    def submit_form(self):
        """Submits the form by clicking the submit button."""
        self.click(self.submit)

