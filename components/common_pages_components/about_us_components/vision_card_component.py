"""This module contains the Vision Card Component class,
 which represents the vision card from the About Us Page on a web page."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class VisionCardComponent(BaseComponent):
    """Component class for the vision card on a web page."""
    locators = {
        "vision_card_picture": (By.CSS_SELECTOR, "img"),
        "vision_card_title": (By.CSS_SELECTOR, ".vision-card__title"),
        "vision_card_description": (By.CSS_SELECTOR, ".vision-card__info > p"),
        "vision_card_button":  (By.CSS_SELECTOR, ".vision-card__info > a")
    }

    vision_card_title: CustomWebElement
    vision_card_description: CustomWebElement
    vision_card_button: CustomWebElement
    vision_card_picture: CustomWebElement

    def click_button(self):
        """Click the button on the vision card."""
        self.vision_card_button.wait_and_click()

    def get_vision_card_info(self) -> dict:
        """Get extracted information from the vision card."""
        vision_card_info = {"picture": self.vision_card_picture,
                            "title": self.vision_card_title,
                            "description": self.vision_card}
        return vision_card_info

    def get_title(self) -> str:
        """Get the title of the vision card."""
        return self.vision_card_title.text.strip()

    def get_description(self) -> str:
        """Get the description of the vision card."""
        return self.vision_card_description.text.strip()
