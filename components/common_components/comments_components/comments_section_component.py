"""Comments form component."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class CommentsSectionComponent(BaseComponent):
    """Comments section component class."""

    locators = {
        "input": (By.ID, "#total-count"),
        "submit_button": (By.CSS_SELECTOR,
                          ".main-wrapper.wrapper-comment"
                          ".ng-untouched.ng-pristine.ng-submitted"
                          ".ng-invalid"),
    }

    comments_count: CustomWebElement
    comments_form: CustomWebElement

    def get_comments_count(self) -> int:
        """Get int count of comments."""
        return int(self.comments_count.text)
