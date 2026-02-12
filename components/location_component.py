"""Component for Place / Online checkboxes."""

from selenium.webdriver.common.by import By
from components.base_component import BaseComponent

class LocationComponent(BaseComponent):
    """Component for Place / Online checkboxes."""

    checkbox_place = (
        By.XPATH,
        ".//mat-checkbox//label[contains(text(),'Place')]/preceding-sibling::input"
    )
    checkbox_online = (
        By.XPATH,
        ".//mat-checkbox//label[contains(text(),'Online')]/preceding-sibling::input"
    )

    def set_place(self, value: bool = True):
        """Set the 'Place' checkbox to the given value."""
        checkbox = self.root.find_element(*self.checkbox_place)
        if checkbox.is_selected() != value:
            checkbox.click()

    def set_online(self, value: bool = True):
        """Set the 'Online' checkbox to the given value."""
        checkbox = self.root.find_element(*self.checkbox_online)
        if checkbox.is_selected() != value:
            checkbox.click()

    def is_place(self) -> bool:
        """Return True if the 'Place' checkbox is selected."""
        return self.root.find_element(*self.checkbox_place).is_selected()

    def is_online(self) -> bool:
        """Return True if the 'Online' checkbox is selected."""
        return self.root.find_element(*self.checkbox_online).is_selected()
