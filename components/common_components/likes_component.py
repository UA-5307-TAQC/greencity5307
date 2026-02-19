"""Likes component"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class LikesComponent(BaseComponent):
    """Likes component class"""

    locators = {
        "like_button": (By.TAG_NAME, "img", WebElement),
        "likes_count": (By.CSS_SELECTOR, ".like_wr > .numerosity_likes", WebElement)
    }

    like_button: WebElement
    likes_count: WebElement

    __liked_img_src = "assets/img/comments/liked.png"

    # pylint: disable=useless-parent-delegation
    def __init__(self, driver: WebDriver, root: WebElement):
        super().__init__(driver, root)

    @allure.step("Click like button and wait for update")
    def click_like_button(self):
        """Likes the item and waits for the counter to change."""
        initial_count = self.get_likes_count()
        self.like_button.click()

        WebDriverWait(self.driver, 10).until(
            lambda _: self.get_likes_count() != initial_count,
            message=f"Count did not change from {initial_count}"
        )

    @allure.step("Check if object is liked")
    def check_like_status(self) -> bool:
        """Check if object is liked"""
        actual_src = self.like_button.get_attribute('src')
        return actual_src is not None and self.__liked_img_src in actual_src

    @allure.step("Get likes count")
    def get_likes_count(self) -> int:
        """Get int value of likes count"""
        text = self.likes_count.text.strip()
        return int(text) if text.isdigit() else 0
