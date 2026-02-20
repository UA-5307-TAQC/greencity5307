"""This module contains AllHabitsUsersPage that represent
'All habits' page on the other user's page."""
from selenium.webdriver.common.by import By

from pages.friend_abstract_page import FriendAbstractPage


class AllHabitsUsersPage(FriendAbstractPage):
    """AllHabitsUsersPage class."""
    all_habits_area_locator = (By.XPATH, "//h3[normalize-space(text())='All habits']")
