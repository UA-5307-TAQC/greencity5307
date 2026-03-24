"""Comment component."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class CommentComponent(BaseComponent):
    """Comment component class."""
    locators = {
        "author": (By.CSS_SELECTOR, ".comment-details > .author-name"),
        "date": (By.CSS_SELECTOR,
                 ".mat-mdc-menu-trigger.custom-chip.global-tag"),
        "text": (By.CSS_SELECTOR, ".comment-main-text > .comment-text"),
        "like_button": (By.CSS_SELECTOR, ".comment-main-text > .comment-text"),
        "likes_count": (By.CSS_SELECTOR, ".comment-likes > .like-amount"),
        "dislike_button": (By.XPATH, "//div[contains(concat(' ', "
                                     "normalize-space(@class), ' '), ' comment-likes '"
                                     ")]/img[@alt='like']"),
    }

    author: CustomWebElement
    date: CustomWebElement
    text: CustomWebElement
    like_button: CustomWebElement
    likes_count: CustomWebElement
    dislike_button: CustomWebElement


    def get_likes_count(self) -> int:
        """Get int count of likes."""
        return int(self.likes_count.text)
