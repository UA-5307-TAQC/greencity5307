"""Likes component"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class LikesComponent(BaseComponent):
    """Likes component class"""
    like_button_locator: Locators = (By.XPATH,
                                     "//img[contains(@class, '_like')"
                                     "and contains(@class, 'ng-star-inserted']")
    likes_count_locator: Locators = (By.CSS_SELECTOR,
                                     ".like_wr > .numerosity_likes")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.like_button = self.root.find_element(*self.like_button_locator)
        self.likes_count = self.root.find_element(*self.likes_count_locator)

    def click_like_button(self):
        """Like something"""
        self.like_button.click()

    def get_likes_count(self) -> int:
        """Get int value of likes count"""
        return int(self.likes_count.text)
