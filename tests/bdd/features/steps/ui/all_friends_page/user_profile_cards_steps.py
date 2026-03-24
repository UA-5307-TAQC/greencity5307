# pylint: disable=not-callable, unused-argument
"""
.. module:: Header navigation
    :platform: Unix
    :synopsis: """
from behave import given, when, then

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


def navigate_to_all_friends_page(profile_banner):
    """Navigate to the 'All Friends' page"""
    if profile_banner.friends_images_exist():
        my_friends_page = profile_banner.click_view_all_friends()
        find_friend_page = my_friends_page.select_tab("find a friend")
    else:
        find_friend_page = profile_banner.click_add_friends_btn()
    return find_friend_page


@given('a target user has no friend cards on the "All Friends" page')
def find_user_without_friend_cards(context):
    """Finds an AllFriendsPage object for a user who has no friends."""
    my_habit_page = MyHabitPage(context.browser)
    profile_banner = my_habit_page.profile_banner
    find_friend_page = navigate_to_all_friends_page(profile_banner)
    all_friends_page = find_user_by_friend_count(find_friend_page, context.browser)

    if not all_friends_page:
        raise AssertionError("Could not find a user without friends.")
    context.all_friends_page = all_friends_page


@given('a target user has friend cards on the "All Friends" page')
def find_user_with_friend_cards(context):
    """Finds an AllFriendsPage object for a user who has friends."""
    my_habit_page = MyHabitPage(context.browser)
    profile_banner = my_habit_page.profile_banner
    find_friend_page = navigate_to_all_friends_page(profile_banner)
    all_friends_page = find_user_by_friend_count(find_friend_page, context.browser, expect_empty=False)

    if not all_friends_page:
        raise AssertionError("Could not find a user with friends.")
    context.all_friends_page = all_friends_page


@then('I should see the "{text}" text')
def check_no_friends_text(context, text):
    "Check if the text on the empty 'All friends' tab on the Friend page is correct"
    all_friends_page = context.all_friends_page
    default_text = all_friends_page.get_default_text()
    assert default_text == text, "The default text is wrong"


@then('the friend card should display the following elements')
def check_friend_card_elements(context):
    "Check if the user card has all elements"
    all_friends_page = context.all_friends_page
    cards = all_friends_page.get_cards_list()
    first_card = cards[0]

    for row in context.table:
        element_name = row['Element']

        if element_name == "Username":
            assert first_card.has_username(), "Username is missing"

        elif element_name == "User City":
            assert first_card.has_user_city(), "User city is missing"

        elif element_name == "Add Friend Button":
            assert first_card.has_add_friend_btn(), "[Add friend] button is missing"


@when('I click on the first friend card in the list')
def click_first_friend_card(context):
    "Click first friend card"
    all_friends_page = context.all_friends_page
    all_habits_page = all_friends_page.cards[0].click_friend_card()
    context.all_habits_page = all_habits_page


@then('the URL should contain "/friends"')
def check_friend_profile_page_rediretcion(context):
    "Check if URL matches the expected friends list path"
    url = context.browser.current_url
    assert "/friends" in url, (
            f"Expected to be on other user profile page, but was at: {url}"
    )


@then('a user banner should be displayed on the page')
def check_user_banner_is_displayed(context):
    "Check if the user banner is displayed"
    all_habits_page = context.all_habits_page
    assert all_habits_page.has_user_banner(), "User banner is not found"
