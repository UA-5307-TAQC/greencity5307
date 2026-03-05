"""Module for testing button "Add friend" on other user's page."""

from selenium.webdriver.remote.webdriver import WebDriver
import allure

from data.config import Config
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.base_page import BasePage


@allure.title("Add friend by clicking on button")
@allure.description(
    "This test verifies that the user can successfully send "
    "friend request to the other user. "
)
@allure.severity(allure.severity_level.NORMAL)
def test_add_friend_by_clicking_on_button(driver: WebDriver):
    """TC-8"""

    base_page = BasePage(driver)

    with allure.step("User signs in with valid credentials"):
        sign_in_component = base_page.header.click_sign_in_link()
        sign_in_component.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("User opens Friends search page"):
        my_space_page = MySpaceAbstractPage(driver)
        friends_page = my_space_page.profile_banner.click_add_friends_btn()

    with allure.step("User opens friend's page"):
        friend_card = friends_page.get_friend_card_by_name("BohdanTest")
        friend_page = friend_card.click_friend_card()

    with allure.step("User clicks add friend button"):
        friend_page.user_info_banner.click_add_friend()











""""

@allure.title("Add friend by clicking on button")
@allure.description("This test verifies that the user can successfully send "
                    "friend request to the other user. ")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "SidorovAI-224")
@allure.testcase("TC-8")
def test_add_friend_by_clicking_on_button(driver: WebDriver):

    main_page = MainPage(driver)

    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(driver, Config.USER_EMAIL, Config.USER_PASSWORD)

    my_space_page = main_page.go_to_my_space()
    time.sleep(3)

    friends_page = my_space_page.click_add_friend_plus()
    time.sleep(3)
    assert friends_page.is_page_opened(), "Friends page not opened"

    friends_page.search_friend("BohdanTest")
    time.sleep(3)

    friend_card = friends_page.get_friend_card_by_name("BohdanTest")
    time.sleep(3)
    assert friend_card is not None, "Friend not found"

    friend_page = friend_card.click_friend_card()
    time.sleep(3)

    assert friend_page.click_add_friend().lower() == "cancel request", "Button does not work"
"""