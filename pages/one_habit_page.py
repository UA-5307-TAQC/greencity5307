""" OneHabitPage elements"""

import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.types import Locators

class OneHabitPage(BasePage):
    """ OneHabitPage"""

    #Button
    back_to_my_habits_button: Locators = (By.CSS_SELECTOR, ".button-arrow div")


    #habit-title
    tags_list: Locators = (By.CSS_SELECTOR, ".tags span")
    acquired_by: Locators  = (By.CSS_SELECTOR, ".habit-info .acquired-by")
    difficulty_stars : Locators = (By.CSS_SELECTOR, ".stars")
    habit_title: Locators = (By.CSS_SELECTOR, ".habit-info .habit-title")
    description: Locators = (By.CSS_SELECTOR, ".habit-info .description")


    #habit-info
    calendar: Locators = (By.CSS_SELECTOR, ".calendar .calendar ")


    #Duration
    duration_day_slider: Locators = (By.CSS_SELECTOR, "mat-slider > input")
    private_switch: Locators = (By.CSS_SELECTOR, ".switch")


    #To-do list
    to_do_list_edit_button: Locators = (By.CSS_SELECTOR, "app-habit-edit-to-do-list > div > a")
    list_container: Locators = (By.CSS_SELECTOR, "div.list-container.ng-star-inserted")

    ##After press edit_button
    del_button: Locators = (By.CSS_SELECTOR, ".del-btn")
    custom_item_input: Locators = (By.CSS_SELECTOR, ".add-field")
    custom_item_add: Locators = (By.CSS_SELECTOR, ".add-item-form .add-btn")

    cancel_button: Locators = (By.XPATH,
                               "//app-habit-edit-to-do-list//button[contains(text(), 'Cancel')]"
                               )

    save_button: Locators = (By.XPATH,
                            "//app-habit-edit-to-do-list//button[contains(text(), 'Save')]"
                            )

    ##Invite friends
    invite_friends_icon: Locators = (By.CSS_SELECTOR, ".icon-plus-grey")


    #Del, Add, Edit  Habit buttons
    delete_habit_button: Locators = (By.XPATH, "//button[normalize-space()='Delete']")
    add_habit_button: Locators = (By.XPATH, "//button[normalize-space()='Add Habit']")
    edit_habit_button: Locators = (By.XPATH,
                                   "//button[normalize-space()='Edit Habit']"
                                    )


    def get_tags_text(self) -> list[str]:
        """
        Return text tags['Resource saving', 'Reusable']
        """
        elements = self.driver.find_elements(*self.tags_list)
        return [element.text.strip() for element in elements]


    @allure.step("Clicking on the Delete button on OneHabitPage")
    def click_delete_button(self):
        """Clicking the Delete button on OneHabitPage."""
        from pages.all_habits_page import AllHabitPage # pylint: disable=import-outside-toplevel
        delete_btn = self.driver.find_element(*self.delete_habit_button)
        delete_btn.click()
        return AllHabitPage(self.driver)
