"""Comments form component."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from components.common_components.comments_components.comments_form_component import \
    CommentsFormComponent
from utils.custom_web_element import CustomWebElement


class CommentsSectionComponent(BaseComponent):
    """Comments section component class."""

    locators = {
        "comments_count": (By.ID, "total-count"),
        "comments_form": (By.CSS_SELECTOR,
                          ".main-wrapper.wrapper-comment"
                          ".ng-untouched.ng-pristine.ng-submitted"
                          ".ng-invalid",
                          CommentsFormComponent),
    }

    comments_count: CustomWebElement
    comments_form: CommentsFormComponent

    def get_comments_count(self) -> int:
        """Get int count of comments."""
        return int(self.comments_count.text)
