"""Comments form component."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class CommentsSectionComponent(BaseComponent):
    """Comments section component class."""
    comments_count_locator: Locators = (By.ID, "#total-count")
    comments_form_locator: Locators = (By.CSS_SELECTOR,
                                       ".main-wrapper.wrapper-comment"
                                       ".ng-untouched.ng-pristine.ng-submitted"
                                       ".ng-invalid")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.comments_count = self.root.find_element(
            *self.comments_count_locator)
        self.comments_form = self.root.find_element(
            *self.comments_form_locator)

    def get_comments_count(self) -> int:
        """Get int count of comments."""
        return int(self.comments_count.text)
