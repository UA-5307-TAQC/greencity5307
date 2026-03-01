"""Component for button to create new for EcoNews page."""
import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class CreateNewButtonComponent(BaseComponent):
    """Component representing the button to create new for EcoNews page."""
    locators ={
        "button_create_news_locator" : (By.XPATH, "//*[@id='main-content']/div/div[1]/div/a")
    }

    button_create_news_locator: CustomWebElement

    @allure.step("Clicking the create new link on the page")
    def click_create_new_button(self):
        """Clicks the create button."""
        self.button_create_news_locator.wait_and_click()
