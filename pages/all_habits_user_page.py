"""This module contains AllHabitsUsersPage that represent
'All habits' page on the user's page."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.friend_abstract_page import FriendAbstractPage


class AllHabitsUsersPage(FriendAbstractPage):
    """AllHabitsUsersPage class."""
    _snack_bar_message = (By.CSS_SELECTOR, "div[matsnackbarlabel]")

    def get_alert_msg(self):
        """Gets text from snack bar message."""
        try:
            snack_bar_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self._snack_bar_message)
            )
            return snack_bar_element.text.strip()
        except TimeoutException:
            return ""
