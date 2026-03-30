""" OneHabitPage elements"""

import allure
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    NoSuchElementException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OneHabitPage(BasePage):
    """ OneHabitPage"""

    locators = {
        # Button
        "back_to_my_habits_button": (By.CSS_SELECTOR, ".button-arrow div"),

        # habit-title
        "tags_list": (By.CSS_SELECTOR, ".tags span"),
        "acquired_by": (By.CSS_SELECTOR, ".habit-info .acquired-by"),
        "difficulty_stars": (By.CSS_SELECTOR, ".stars"),
        "habit_title": (By.CSS_SELECTOR, ".habit-info .habit-title"),
        "description": (By.CSS_SELECTOR, ".habit-info .description"),

        # habit-info
        "calendar": (By.CSS_SELECTOR, ".calendar .calendar "),
        "mark_as_done_button_undone": (By.CSS_SELECTOR, "div.mark-done button.undone"),
        "mark_as_done_button_done": (By.CSS_SELECTOR, "div.mark-done button.done"),
        "status_text": (By.XPATH, "//div[contains(@class, 'mark-done')]/div[contains(@class, 'ng-star-inserted')]"),

        # Duration
        "duration_day_slider": (By.CSS_SELECTOR, "mat-slider > input"),
        "private_switch": (By.CSS_SELECTOR, ".switch"),

        # To-do list
        "to_do_list_edit_button": (By.CSS_SELECTOR, "app-habit-edit-to-do-list > div > a"),
        "list_container": (By.CSS_SELECTOR, ".to-do-list-container > .list-container"),
        "list_items_loc": (By.CSS_SELECTOR, ".list-container li.list-item span"),

        # After press edit_button
        "del_button": (By.CSS_SELECTOR, ".del-btn"),
        "custom_item_input": (By.CSS_SELECTOR, ".add-field"),
        "custom_item_add": (By.CSS_SELECTOR, ".add-item-form .add-btn"),
        "cancel_button": (By.XPATH,
                          "//app-habit-edit-to-do-list//button[contains(text(), 'Відмінити') "
                          "or contains(text(), 'Cancel')]"),
        "save_button": (By.XPATH,
                          "//app-habit-edit-to-do-list//button[contains(text(), 'Зберегти') "
                          "or contains(text(), 'Save')]"),

        # Invite friends
        "invite_friends_icon": (By.CSS_SELECTOR, ".icon-plus-grey"),

        # Del, Add, Edit Habit buttons
        "delete_habit_button": (By.XPATH, "//button[normalize-space()='Delete']"),
        "add_habit_button": (By.XPATH, "//button[normalize-space()='Add Habit']"),
        "edit_habit_button": (By.XPATH, "//button[normalize-space()='Edit Habit']")
    }
    back_to_my_habits_button: WebElement
    acquired_by: WebElement
    difficulty_stars: WebElement
    habit_title: WebElement
    description: WebElement
    calendar: WebElement
    duration_day_slider: WebElement
    private_switch: WebElement
    to_do_list_edit_button: WebElement
    list_container: WebElement
    del_button: WebElement
    custom_item_input: WebElement
    custom_item_add: WebElement
    cancel_button: WebElement
    save_button: WebElement
    invite_friends_icon: WebElement
    delete_habit_button: WebElement
    add_habit_button: WebElement
    edit_habit_button: WebElement
    mark_as_done_button_undone : WebElement
    mark_as_done_button_done : WebElement
    status_text: WebElement

    def get_tags_text(self) -> list[str]:
        """
        Return text tags['Resource saving', 'Reusable']
        """
        # Використовуємо метод фабрики resolve_list для отримання списку елементів
        elements = self.resolve_list("tags_list")
        return [element.text.strip() for element in elements]

    @allure.step("Click To-Do List edit button")
    def press_to_do_list_edit_button(self):
        """start edit to do list"""
        self.to_do_list_edit_button.wait_and_click()
        return self

    @allure.step("Enter and add item '{message}' to the list")
    def add_element_into_list(self, message: str):
        """write element in list and add it"""
        self.custom_item_input.send_keys(message)
        self.custom_item_add.wait_and_click()
        list_items_locator = self.locators["list_items_loc"][:2]
        self.get_wait().until(
            EC.text_to_be_present_in_element(list_items_locator, message)
        )
        return self

    @allure.step("Save changes")
    def save_element(self):
        """save element"""
        self.save_button.wait_and_click()

        save_btn_locator = self.locators["save_button"][:2]
        self.get_wait().until(
            EC.invisibility_of_element_located(save_btn_locator)
        )
        return self

    @allure.step("Get added elements list")
    def check_added_element(self):
        """check added element"""
        list_items_locator = self.locators["list_items_loc"][:2]
        saved_items = self.get_wait().until(EC.presence_of_all_elements_located(list_items_locator))
        return [item.text.strip() for item in saved_items]

    @allure.step("Clicking on the Delete button on OneHabitPage")
    def click_delete_button(self):
        """Clicking the Delete button on OneHabitPage."""
        from pages.habit_pages.all_habits_page import AllHabitPage # pylint: disable=import-outside-toplevel

        self.delete_habit_button.wait_and_click()
        return AllHabitPage(self.driver)

    @allure.step("Move slider to the right")
    def move_slider_right(self, value: int):
        """Move slider using keyboard arrows"""
        for _ in range(value):
            self.duration_day_slider.send_keys(Keys.ARROW_RIGHT)
        return self
    @allure.step("Move slider to the left")
    def move_slider_left(self,value: int):
        """Move slider using keyboard arrows"""
        for _ in range(value):
            self.duration_day_slider.send_keys(Keys.ARROW_LEFT)
        return self

    @allure.step("Get current slider value")
    def get_slider_value(self) -> int:
        """Returns the current numeric value of the slider"""
        value_str = self.duration_day_slider.get_attribute("aria-valuetext")
        return int(value_str)

    @allure.step("Press 'Mark as done' button (undone state)")
    def press_mark_as_done_button(self):
        """Press button to mark as done"""
        try:
            self.mark_as_done_button_undone.wait_and_click()

        except (TimeoutException, NoSuchElementException) as exception:
            raise AssertionError(
                "Failed to find or wait for the 'Mark as done' button. "
                "The component might be missing, or the habit has already been completed."
            ) from exception
        except StaleElementReferenceException as exception:
            raise AssertionError(
                "The page structure was updated (DOM changed) while attempting to click "
                "the 'Mark as done' button."
            ) from exception
        except Exception as e:
            raise AssertionError(
                f"An unknown error occurred while interacting with the 'Mark as done' button: {str(e)}"
            ) from e

    @allure.step("Check if habit is marked as done")
    def is_habit_marked_as_done(self, timeout=5):
        """Wait for habit is marked as done"""
        try:
            self.get_wait(timeout).until(
                EC.visibility_of(self.mark_as_done_button_done)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Get progress streak text next to the button")
    def get_progress_text(self, timeout=5):
        """Display text of progress streak"""
        element = self.get_wait(timeout).until(
            EC.visibility_of(self.status_text)
        )
        return element.text
