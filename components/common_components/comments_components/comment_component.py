"""Comment component."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class CommentComponent(BaseComponent):
    """Comment component class."""
    author_locator: Locators = (By.CSS_SELECTOR,
                                ".comment-details > .author-name")
    date_locator: Locators = (By.CSS_SELECTOR,
                              ".comment-date > .comment-date-month")
    text_locator: Locators = (By.CSS_SELECTOR,
                              ".comment-main-text > .comment-text")
    # likes
    like_button_locator: Locators = (By.CSS_SELECTOR,
                                     ".comment-main-text > .comment-text")
    likes_count_locator: Locators = (By.CSS_SELECTOR,
                                     ".comment-likes > .like-amount")
    dislike_button_locator: Locators = (By.XPATH,
                                        "//div[contains(concat("
                                        "' ', "
                                        "normalize-space(@class), ' '), "
                                        "' comment-likes '"
                                        ")]/img[@alt='like']")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.author = self.root.find_element(*self.author_locator)
        self.date = self.root.find_element(*self.date_locator)
        self.text = self.root.find_element(*self.text_locator)
        self.like_button = self.root.find_element(*self.like_button_locator)
        self.likes_count = self.root.find_element(*self.likes_count_locator)
        self.dislike_button = self.root.find_element(
            *self.dislike_button_locator)

    def get_likes_count(self) -> int:
        """Get int count of likes."""
        return int(self.likes_count.text)
