"""This module contains the Vision Card Component class,
 which represents the vision card from the About As Page on a web page."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class VisionCardComponent(BaseComponent):
    """Component class for the friend card on a web page."""
    vision_card_picture_locator = (By.CSS_SELECTOR,'img')
    vision_card_title_locator: Locators = (By.CSS_SELECTOR,'.vision-card__title')
    vision_card_description_locator: Locators = (By.CSS_SELECTOR,"vision-card__info > p")
    vision_card_btn_locator: Locators = (By.CSS_SELECTOR, "vision-card__info > a")

    def get_vision_card_info(self) -> dict:
        """Get an info from a vision card."""
        friend_info = {
            "picture": self.vision_card_picture_locator,
            "title": self.vision_card_title_locator,
            "description": self.vision_card_description_locator,
            }
        return friend_info

    def get_title(self) -> str:
        """Get the title of the vision card."""
        return self.root.find_element(*self.vision_card_title_locator).text.strip()

    def get_description(self) -> str:
        """Get the description of the vision card."""
        return self.root.find_element(*self.vision_card_description_locator).text.strip()