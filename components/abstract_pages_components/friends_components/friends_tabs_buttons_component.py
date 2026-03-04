"""Friends tabs buttons component."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class FriendsTabsButtonsComponent(BaseComponent):
    """Component representing the friends tabs buttons on the friends abstract page."""
    locators = {
        "my_friends_tab": (By.XPATH, "/html/body/app-root/app-main/div/div[2]/"
                                     "app-greencity-main/app-user-component/"
                                     "app-friend-dashboard/div/div/div/div/a[1]"),
        "find_friend_tab": (By.XPATH, "/html/body/app-root/app-main/div/div[2]/"
                                      "app-greencity-main/app-user-component/"
                                      "app-friend-dashboard/div/div/div/div/a[2]"),
        "friend_requests_tab": (By.XPATH, "/html/body/app-root/app-main/div/div[2]/"
                                          "app-greencity-main/app-user-component/"
                                          "app-friend-dashboard/div/div/div/div/a[3]")
    }
    my_friends_tab: CustomWebElement
    find_friend_tab: CustomWebElement
    friend_requests_tab: CustomWebElement

    def click_my_friends_tab(self):
        """Clicks the friends tab."""
        self.my_friends_tab.wait_and_click()

    def click_find_friend_tab(self):
        """Clicks the find friend tab."""
        self.find_friend_tab.wait_and_click()

    def click_friend_requests_tab(self):
        """Clicks the friend requests tab."""
        self.friend_requests_tab.wait_and_click()
