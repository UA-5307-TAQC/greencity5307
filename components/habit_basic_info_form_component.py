"""This module contains the HabitBasicInfoFormComponent class,
 which represents the basic form of the Create Habit page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from utils.types import Locators


class HabitBasicInfoFormComponent(BaseComponent):
    """Component class for the habit basic form of the Create Habit page."""
    title_locator: Locators = (By.XPATH, ".//input[@placeholder='Enter name for the habit']")
    stars_locator: Locators = (By.CSS_SELECTOR, "li.star-button")
    tags_locator: Locators = (By.CSS_SELECTOR, "app-tags-select button")
    description_locator: Locators = (By.XPATH, ".//div[@data-placeholder='Describe the habit']")
    submit_locator: Locators = \
        (By.XPATH, ".//div[@class='habit-block']//button[text()[contains(., 'Submit')]]")
    dropzone_locator: Locators = (By.CSS_SELECTOR, "div.dropzone")
    images_locator: Locators = (By.CSS_SELECTOR, "app-select-images button")

    add_habit_btn_locator: Locators = (By.XPATH, ".//button[text() [contains(.,'Add Habit')]]")


    def __init__(self, root: WebElement):
        super().__init__(root)
        self.title = self.root.find_element(*self.title_locator)
        self.stars = self.root.find_elements(*self.stars_locator)
        self.tags = self.root.find_elements(*self.tags_locator)
        self.submit_img_btn = self.root.find_element(*self.submit_locator)
        self.images = self.root.find_elements(*self.images_locator)
        self.add_habit_btn = self.root.find_element(*self.add_habit_btn_locator)


    @allure.step("Enter text into title field on Create Habit form")
    def enter_title(self, text: str):
        """Enter text into title field."""
        self.title.send_keys(text)


    @allure.step("Enter text into description field on Create Habit form")
    def enter_description(self, text: str):
        """Enter text into description textarea."""
        description = self.root.find_element(*self.description_locator)
        description.send_keys(text)


    @allure.step("Choose difficulty")
    def choose_difficulty(self, difficulty: str):
        """Choose easy, medium or hard habit difficulty."""
        levels = {'easy': 0,
                  'medium': 1,
                  'hard': 2}
        index = levels.get(difficulty.lower())

        if index is None:
            raise ValueError(f"Invalid difficulty: {difficulty}.")

        self.stars[index].click()


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

        for i in indexes:
            self.tags[i].click()


    @allure.step("Choose an image")
    def choose_image(self, driver: WebDriver, image_num: int):
        """Choose image for habit and submit it."""
        if image_num > 3 or image_num < 1:
            raise ValueError(f"Invalid image number: {image_num}.")

        actions = ActionChains(driver)
        image = self.images[image_num - 1]
        dropzone = self.root.find_element(*self.dropzone_locator)
        actions.drag_and_drop(image, dropzone).perform()

        self.submit_img_btn.click()


    @allure.step("Clicking the Add Habit button on Create Habit form")
    def submit_form(self, driver):
        """Submit habit form."""
        self.add_habit_btn.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("allhabits")
        )
