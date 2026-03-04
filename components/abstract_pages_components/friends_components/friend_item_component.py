"""Friend Item Component"""

from selenium.webdriver.common.by import By
from components.base_component import BaseComponent


class FriendItemComponent(BaseComponent):
    """Friend Item Component"""

    name = (By.CSS_SELECTOR, ".friend-name")
    rate = (By.CSS_SELECTOR, ".friend-rate")
    mutual_friends = (By.CSS_SELECTOR, ".friend-mutual-link")
    city = (By.CSS_SELECTOR, ".friend-city")
    btn_unfriend = (By.ID, "deleteFriend")

    def get_name(self):
        """Get friend's name."""
        return self.root.find_element(*self.name).text

    def get_rate(self):
        """Get friend's rate."""
        text = self.root.find_element(*self.rate).text
        return int(text.replace("Rate: ", ""))

    def get_mutual_friends(self):
        """Get friend's mutual friends."""
        text = self.root.find_element(*self.mutual_friends).text
        return int(text.split()[0])  # "0 mutual friends" -> 0

    def get_city(self):
        """Get friend's city."""
        return self.root.find_element(*self.city).text

    def click_unfriend(self):
        """Click unfriend"""
        self.root.find_element(*self.btn_unfriend).click()
