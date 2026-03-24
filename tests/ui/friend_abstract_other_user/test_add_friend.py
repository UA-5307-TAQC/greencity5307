"""Module for testing button "Add friend" on other user's page."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.base_page import BasePage


@allure.title("Add friend by clicking on button")
@allure.description("This test verifies that the user can successfully send "
                    "friend request to the other user. ")
@allure.severity(allure.severity_level.NORMAL)
def test_add_friend_by_clicking_on_button(driver_with_login: WebDriver):
    """TC-8"""

    base_page = BasePage(driver_with_login)

    with allure.step("User opens Friends search page"):
        my_space_page = MySpaceAbstractPage(driver_with_login)
        friends_page = my_space_page.profile_banner.click_add_friends_btn()

    with allure.step("User opens friend's page"):
        friend_card = friends_page.get_friend_card_by_name("BohdanTest")
        friend_page = friend_card.click_friend_card()

    with allure.step("User clicks add friend button"):
        button_text = friend_page.user_info_banner.click_add_friend()
        assert isinstance(button_text, str) and button_text.lower() == "cancel request", (
            'After sending friend request, button text should be "Cancel request"'
        )

