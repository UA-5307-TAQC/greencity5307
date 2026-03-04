"""Component representing event header section (Title + Duration)."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class EventHeaderComponent(BaseComponent):
    """Component for event title and duration section."""

    title_input: Locators = (By.CSS_SELECTOR, "input[formcontrolname='title']")

    duration_select: Locators = (By.CSS_SELECTOR, "mat-select[formcontrolname='duration']")

    duration_options: Locators = (By.CSS_SELECTOR, "mat-option")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.title = self.root.find_element(*self.title_input)
        self.duration = self.root.find_element(*self.duration_select)

    def set_title(self, text: str):
        """Set event title."""
        self.title.clear()
        self.title.send_keys(text)

    def get_title(self) -> str:
        """Get event title."""
        return self.title.get_attribute("value")

    def open_duration_dropdown(self):
        """Open duration dropdown."""
        self.duration.click()

    def select_duration(self, value: str):
        """Select duration."""
        self.open_duration_dropdown()

        option = self.duration.parent.find_element(
            By.XPATH,
            f"//mat-option//span[text()='{value}']"
        )
        option.click()

    def get_selected_duration(self) -> str:
        """Get selected duration."""
        return self.duration.text.strip()
