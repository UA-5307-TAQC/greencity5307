"""Likes component"""
import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class LikesComponent(BaseComponent):
    """Likes component class"""
    locators = {
        "like_button": (By.TAG_NAME, "img"),
        "likes_count": (By.CSS_SELECTOR, ".like_wr > .numerosity_likes")
    }

    __liked_img_src = "assets/img/comments/like.png"

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
