""" OneHabitPage elements"""


from selenium.webdriver.common.by import By

from components.header_component import HeaderComponent
from pages.base_page import BasePage, WebDriver
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
    edit_habit_button: Locators = (By.XPATH, "//button[normalize-space()='Edit Habit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # Header = HeaderComponent  # need to rewrite
        self.header = HeaderComponent(driver)

    def get_tags_text(self) -> list[str]:
        """
        Return text tags['Resource saving', 'Reusable']
        """
        elements = self.driver.find_elements(*self.tags_list)
        return [element.text.strip() for element in elements]
