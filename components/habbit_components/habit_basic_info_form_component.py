"""This module contains the HabitBasicInfoFormComponent class,
 which represents the basic form of the Create Habit page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class HabitBasicInfoFormComponent(BaseComponent):
    """Component class for the habit basic form of the Create Habit page."""

    locators = {
        "title": (By.XPATH, ".//input[@placeholder='Enter name for the habit']"),
        "stars": (By.CSS_SELECTOR, "li.star-button"),
        "tags": (By.CSS_SELECTOR, "app-tags-select button"),
        "description": (By.XPATH, ".//div[@data-placeholder='Describe the habit']"),
        "submit_img_btn": (By.CSS_SELECTOR, "div.cropper-buttons button.primary-global-button"),
        "dropzone": (By.CSS_SELECTOR, "div.dropzone"),
        "images": (By.CSS_SELECTOR, "app-select-images button"),
        "add_habit_btn": (By.CSS_SELECTOR, "div.add-habit-container button.primary-global-button")
    }

    title: CustomWebElement
    stars: list
    tags: list
    description: CustomWebElement
    submit_img_btn: CustomWebElement
    dropzone: CustomWebElement
    images: list
    add_habit_btn: CustomWebElement


    @allure.step("Enter text into title field on Create Habit form")
    def enter_title(self, text: str):
        """Enter text into title field."""
        self.wait.until(EC.visibility_of(self.title)).send_keys(text)


    @allure.step("Enter text into description field on Create Habit form")
    def enter_description(self, text: str):
        """Enter text into description textarea."""
        self.wait.until(EC.visibility_of(self.description)).send_keys(text)


    @allure.step("Choose difficulty")
    def choose_difficulty(self, difficulty: str):
        """Choose easy, medium or hard habit difficulty."""
        levels = {'easy': 0,
                  'medium': 1,
                  'hard': 2}
        found_stars = self.resolve_list("stars")

        index = levels.get(difficulty.lower())

        if index is None:
            raise ValueError(f"Invalid difficulty: {difficulty}.")

        found_stars[index].wait_and_click()


    @allure.step("Choose tags for habit on Create Habit form")
    def choose_tags(self, chosen_tags: list):
        """Choose tags for habit."""
        list_of_tags = {
            'testing': 0,
            'reusable': 1,
            'resource saving': 2,
            'smart consuming': 3,
            'transportation': 4,
            'recycling/waste sorting': 5
            }
        indexes = []
        found_tags = self.resolve_list("tags")

        for tag in chosen_tags:
            index = list_of_tags.get(tag)
            if index is None:
                raise ValueError(f"Invalid tag: {tag}.")
            indexes.append(index)

        for i in indexes:
            found_tags[i].wait_and_click()


    @allure.step("Choose an image")
    def choose_image(self, driver: WebDriver, image_num: int):
        """Choose image for habit and submit it."""
        if image_num > 3 or image_num < 1:
            raise ValueError(f"Invalid image number: {image_num}.")

        found_images = self.resolve_list("images")
        actions = ActionChains(driver)
        image = found_images[image_num - 1]
        actions.drag_and_drop(image, self.dropzone).perform()

        self.submit_img_btn.wait_and_click()


    @allure.step("Clicking the Add Habit button on Create Habit form")
    def submit_form(self) -> "AllHabitPage":
        """Submit habit form."""
        from pages.habit_pages.all_habits_page import AllHabitPage # pylint: disable=import-outside-toplevel
        self.add_habit_btn.wait_and_click()

        WebDriverWait(self.root.parent, 10).until(
            EC.url_contains("allhabits")
        )
        return AllHabitPage(self.root.parent)
