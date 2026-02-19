"""Component for button to create new for EcoNews page."""
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class CreateNewButtonComponent(BaseComponent):
    """Component representing the button to create new for EcoNews page."""
    Locators = Tuple[str, str]
    button_create_news_locator: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/a")

    def get_button(self) -> WebElement:
        """Get the locator for the create news button."""
        return self.root.find_element(*self.button_create_news_locator)

    @allure.step("Clicking the create new link in the page")
    def click_create_new_button(self):
        """Click the create news link in the page and return an instance of the
        CreateUpdateEcoNews."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.button_create_news_locator)
        ).click()
