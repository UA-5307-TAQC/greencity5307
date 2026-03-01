"""This module contains the HabitBasicInfoFormComponent class,
 which represents the basic form of the Create Habit page."""
from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class HabitBasicInfoFormComponent(BaseComponent):
    """Component class for the habit basic form of the Create Habit page."""

    locators = {
        "title": (By.XPATH, ".//input[@placeholder='Enter name for the habit']"),
        "stars": (By.CSS_SELECTOR, "li.star-button", List[CustomWebElement]),
        "tags": (By.CSS_SELECTOR, "app-tags-select button", List[CustomWebElement]),
        "description": (By.XPATH, ".//div[@data-placeholder='Describe the habit']"),
        "submit_img_btn": (By.CSS_SELECTOR, "div.cropper-buttons button.primary-global-button"),
        "dropzone": (By.CSS_SELECTOR, "div.dropzone"),
        "images": (By.CSS_SELECTOR, "app-select-images button", List[CustomWebElement]),
        "add_habit_btn": (By.CSS_SELECTOR, "div.add-habit-container button.primary-global-button"),
        "title_validation_msg": (By.CSS_SELECTOR, "div.validation"),
        "description_validation_msg": (By.CSS_SELECTOR, "p.habit-tooltip ")
    }

    title: CustomWebElement
    stars: list[CustomWebElement]
    tags: list[CustomWebElement]
    description: CustomWebElement
    submit_img_btn: CustomWebElement
    dropzone: CustomWebElement
    images: list[CustomWebElement]
    add_habit_btn: CustomWebElement
    title_validation_msg: CustomWebElement
    description_validation_msg: CustomWebElement


    @allure.step("Enter text into title field on Create Habit form")
    def enter_title(self, text: str):
        """Enter text into title field."""
        self.get_wait().until(EC.visibility_of(self.title)).send_keys(text)


    @allure.step("Enter text into description field on Create Habit form")
    def enter_description(self, text: str):
        """Enter text into description textarea."""
        self.get_wait().until(EC.visibility_of(self.description)).send_keys(text)


    def get_title_validation_msg(self):
        """Get title validation message."""
        return self.get_wait().until(
            EC.visibility_of(self.title_validation_msg)
            ).text


    def get_description_validation_msg(self):
        """Get description validation message."""
        return self.get_wait().until(
            EC.visibility_of(self.description_validation_msg)
            ).text


    @allure.step("Choose difficulty")
    def choose_difficulty(self, difficulty: str):
        """Choose easy, medium or hard habit difficulty."""
        levels = {'easy': 0,
                  'medium': 1,
                  'hard': 2}

        index = levels.get(difficulty.lower())

        if index is None:
            raise ValueError(f"Invalid difficulty: {difficulty}.")

        self.stars[index].wait_and_click()


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

        for tag in chosen_tags:
            index = list_of_tags.get(tag)
            if index is None:
                raise ValueError(f"Invalid tag: {tag}.")
            indexes.append(index)

        resolved_tags = self.tags

        for i in indexes:
            resolved_tags[i].wait_and_click()


    @allure.step("Choose an image")
    def choose_image(self, driver: WebDriver, image_num: int):
        """Choose image for habit and submit it."""
        if image_num > 3 or image_num < 1:
            raise ValueError(f"Invalid image number: {image_num}.")

        actions = ActionChains(driver)
        image = self.images[image_num - 1]
        actions.drag_and_drop(image, self.dropzone).perform()
        self.submit_img_btn.wait_and_click()


    @allure.step("Clicking the Add Habit button on Create Habit form")
    def submit_form(self) -> "AllHabitPage":
        """Submit habit form."""
        from pages.habit_pages.all_habits_page import AllHabitPage # pylint: disable=import-outside-toplevel

        self.add_habit_btn.wait_and_click()
        self.get_wait().until(EC.url_contains("allhabits"))
        return AllHabitPage(self.root.parent)
