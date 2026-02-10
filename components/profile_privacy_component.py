"""Profile privacy component"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class ProfilePrivacyComponent(BaseComponent):
    """Component for the 'Profile privacy' block."""

    root_locator = (By.CSS_SELECTOR, "div.privacy-wrapper")
    setting_item_locator = (By.CSS_SELECTOR, "li.ng-star-inserted")
    mat_select_locator = (By.CSS_SELECTOR, "mat-select.state-select")
    mat_option_locator = (By.CSS_SELECTOR, "mat-option")

    def __init__(self, parent: WebElement):
        super().__init__(parent)
        self.root: WebElement = parent.find_element(*self.root_locator)

    def get_setting_value(self, index: int) -> str:
        """Return the currently selected value of a setting by index (0-based)."""
        mat_selects = self.root.find_elements(*self.mat_select_locator)
        return mat_selects[index].text

    def set_setting_value(self, index: int, value: str):
        """Set a new value for a setting by index (0-based)."""
        mat_selects = self.root.find_elements(*self.mat_select_locator)
        select = mat_selects[index]
        select.click()  # відкриваємо список опцій

        # чекаємо поки з'являться опції
        options = WebDriverWait(self.root.parent, 5).until(
            EC.presence_of_all_elements_located(self.mat_option_locator)
        )

        for option in options:
            if option.text.strip() == value:
                option.click()
                break
