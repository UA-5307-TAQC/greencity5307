"""Likes component"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class LikesComponent(BaseComponent):
    """Likes component class"""
    like_button_locator: Locators = (By.TAG_NAME, "img")
    likes_count_locator: Locators = (By.CSS_SELECTOR,
                                     ".like_wr > .numerosity_likes")

    __liked_img_src = "assets/img/comments/like.png"

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.like_button = self.root.find_element(*self.like_button_locator)
        self.likes_count = self.root.find_element(*self.likes_count_locator)

    @allure.step("Click like button")
    def click_like_button(self):
        """Like something"""
        self.like_button.click()

    @allure.step("Check if object is liked")
    def check_like_status(self) -> bool:
        """Check if object is liked"""
        return self.like_button.get_attribute('src') == self.__liked_img_src

    @allure.step("Get likes count")
    def get_likes_count(self) -> int:
        """Get int value of likes count"""
        return int(self.likes_count.text)
