"""Conftest file with fixtures for FindFriend tests."""
from pytest import fixture

from pages.common_pages.main_page import MainPage


@fixture(scope="function")
def target_user_not_added_to_friends(driver_with_login):  # pylint: disable=redefined-outer-name
    """Fixture that verifies, that the user was not added to the friends list."""
    def _verify_is_added_friend(name):
        main_page = MainPage(driver_with_login)
        my_habit_page = main_page.header.click_my_space_link()
        find_friend_page = my_habit_page.profile_banner.click_add_friends_btn()
        find_friend_page.search_friend(name)
        friend_card = find_friend_page.get_friend_card_by_name(name)

        if friend_card.add_friend_btn.text == "Cancel request":
            friend_card.click_add_friend_btn()
            find_friend_page.wait_for_snack_bar_disappear()

        find_friend_page.header.click_main_page_link()

    return _verify_is_added_friend
