""" OneHabitPage elements"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    list_container: Locators = (By.CSS_SELECTOR, ".to-do-list-container > .list-container")
    list_items_loc = (By.CSS_SELECTOR, ".list-container li.list-item span")

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

    def press_to_do_list_edit_button(self):
        """start edit to do list"""
        self.click(self.to_do_list_edit_button)
        return self

    def add_element_into_list(self, message: str):
        """write element in list and add it"""
        self.find(self.custom_item_input).send_keys(message)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.custom_item_add)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.list_items_loc, message)
        )
        return self

    def save_element(self):
        """save element"""
        self.click(self.save_button)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.save_button)
        )
        return self

    def check_added_element(self):
        """check added element"""
        saved_items = self.wait.until(EC.presence_of_all_elements_located(self.list_items_loc))
        return [item.text.strip() for item in saved_items]
