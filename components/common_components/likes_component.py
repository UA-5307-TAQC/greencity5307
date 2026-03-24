"""Likes component"""
import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement
from utils.logger import logger


class LikesComponent(BaseComponent):
    """Likes component class"""
    locators = {
        "like_button": (By.TAG_NAME, "img"),
        "likes_count": (By.CSS_SELECTOR, ".like_wr > .numerosity_likes")
    }

    like_button: CustomWebElement
    likes_count: CustomWebElement

    __liked_img_src = "assets/img/comments/like.png"

    @allure.step("Click like button")
    def click_like_button(self):
        """Like something"""
        self.like_button.click()

    @allure.step("Check if object is liked")
    def check_like_status(self) -> bool:
        """Check if object is liked"""
        status = self.like_button.get_attribute('src') == self.__liked_img_src
        logger.info("Like status: %s", status)
        return status

    @allure.step("Get likes count")
    def get_likes_count(self) -> int:
        """Get int value of likes count"""
        likes_count = int(self.likes_count.text)
        logger.info("Current likes: %s", likes_count)
        return likes_count
