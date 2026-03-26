from types import SimpleNamespace

import pytest
import allure

from pages.abstract_pages.friends_abstract.find_friend_page import FindFriendPage
from pages.abstract_pages.friend_abstract_users.all_friends_page import AllFriendsPage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage


def find_user_by_friend_count(page: FindFriendPage, driver, expect_empty: bool = True) ->  AllFriendsPage | None:
    """Iterates through friend cards on the Find Friend page
    to find a user with a specific friend count state."""
    num_of_cards = len(page.get_all_friend_cards())
    for i in range(num_of_cards):
        card = page.get_all_friend_cards()[i]
        all_habits_page = card.click_friend_card()
        all_friends_page = all_habits_page.click_all_friends_tab()

        is_currently_empty = len(all_friends_page.get_cards_list()) == 0

        if is_currently_empty == expect_empty:
            return all_friends_page
        driver.back()
        page.wait_for_list_to_load()

    return None


@pytest.fixture(scope="function")
def find_friend_page_context(driver_with_login):
    """Fixture for navigation to Find Friend page."""
    driver = driver_with_login

    with allure.step("Navigate to Find Friend page"):
        my_habit_page = MyHabitPage(driver)
        profile_banner = my_habit_page.profile_banner
        if profile_banner.friends_images_exist():
            my_friends_page = profile_banner.click_view_all_friends()
            find_friend_page = my_friends_page.select_tab("find a friend")
        else:
            find_friend_page = profile_banner.click_add_friends_btn()
    return SimpleNamespace(page = find_friend_page, driver = driver_with_login)


@pytest.fixture(scope="function")
def page_of_user_without_friends(find_friend_page_context):
    """Provides an AllFriendsPage object for a user who has no friends."""
    find_friend_page = find_friend_page_context.page
    driver = find_friend_page_context.driver

    with allure.step("Pre-condition: Locate a user with an empty friends list"):
        all_friends_page = find_user_by_friend_count(find_friend_page, driver)
        if not all_friends_page:
            pytest.fail("Could not find a user without friends.")
        return all_friends_page


@pytest.fixture(scope="function")
def page_of_user_with_friends(find_friend_page_context):
    """Provides an AllFriendsPage object for a user who has friends."""
    find_friend_page = find_friend_page_context.page
    driver = find_friend_page_context.driver

    with allure.step("Pre-condition: Locate a user with non-empty friends list"):
        all_friends_page = find_user_by_friend_count(find_friend_page, driver, expect_empty=False)
        if not all_friends_page:
            pytest.fail("Could not find a user with friends.")
        return all_friends_page
