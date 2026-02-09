"""Update habit components."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class HabitBasicInfoComponent(BaseComponent):
    """
    Component that edit main information.
    """

    title_field = (By.CSS_SELECTOR, "formcontrolname='title'")

    description_field = (By.CSS_SELECTOR, "[formcontrolname='description']")

    difficulty_stars = (By.CSS_SELECTOR, "#complexityList")
    tags = (By.CLASS_NAME, "tag-button ng-star-inserted")

    def set_title(self, title: str):
        """Set new title."""
        self.input_text(self.title_field, title)

    def get_title_value(self) -> str:
        """Get title value."""
        return self.find_element(self.title_field).get_attribute("value")

    def set_description(self, description: str):
        """Set description."""
        self.input_text(self.description_field, description)

    def get_description_value(self) -> str:
        """Get current description value."""
        return self.find_element(self.description_field).get_attribute("value")

    def set_difficulty(self, level: int):
        """
        Set difficulty level.
        """
        stars = self.find_elements(self.difficulty_stars)

        if 1 <= level <= len(stars):
            stars[level - 1].click()
        else:
            print(f"Error: difficulty {level} unavailable. Maximum: {len(stars)}")

    def select_tag(self, tag_name: str):
        """
        Select tag by his name.
        """
        tags = self.find_elements(self.tags)

        tag_found = False
        for tag in tags:
            if tag.text.strip() == tag_name:
                tag.click()
                tag_found = True
                break

        if not tag_found:
            print(f"Tag '{tag_name}' hasn\'t been found.")


class HabitProgressComponent(BaseComponent):
    """
    Component for progress bar block,
    """
    progress_block = (By.CSS_SELECTOR, ".duration")

    calendar_block = (By.CSS_SELECTOR, ".habit-progress")

    def is_progress_available(self):
        """Check if progress bar is available."""
        elements = self.find_elements(self.progress_block)
        return len(elements) > 0 and elements[0].is_displayed()

    def is_calendar_visible(self) -> bool:
        """Check if calendar block is visible"""
        elements = self.find_elements(self.calendar_block)
        return len(elements) > 0 and elements[0].is_displayed()
