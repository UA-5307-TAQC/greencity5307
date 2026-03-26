"""Steps for TC-FF-01."""
from behave import given, when, then

from clients.friends_client import FriendsClient
from clients.own_security_client import OwnSecurityClient

from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.abstract_pages.friends_abstract.find_friend_page import FindFriendPage

from data.config import Config


@given('a target user with "{friend_id}" has no friend request')
def step_target_user_has_no_friend_request(context, friend_id):  # pylint: disable=unused-argument
    """Given a target user with "<friend_id>" has no friend request."""
    own_client = OwnSecurityClient(base_url=Config.BASE_USER_API_URL)
    response = own_client.sign_in(
        email=Config.USER_EMAIL,
        password=Config.USER_PASSWORD
    )

    assert response.status_code == 200, f"Login failed: {response.text}"
    access_token = response.json().get("accessToken")

    client = FriendsClient(
        base_url=Config.BASE_API_URL,
        access_token=access_token
    )
    response = client.cancel_request(friend_id=friend_id)
    assert response.status_code in {200, 404}, \
        (f"Failed to prep state. "
         f"Status: {response.status_code}, "
         f"Body: {response.text}")


@given('the user is on the "Find Friend" page')
def step_user_is_on_find_friend_page(context):
    """And the user is on the "Find Friend" page."""
    main_page = MySpaceAbstractPage(context.browser).header.click_logo()
    assert main_page.is_loaded()

    user_name_from_header = main_page.header.get_signed_in_user_name()
    assert user_name_from_header in [Config.USER_NAME, "Hlib", "Oleksandr"], \
        f"The expected user is not signed in. Found user: '{user_name_from_header}'"

    my_habit_page = main_page.header.click_my_space_link()
    assert my_habit_page.wait_page_loaded(), "'My Space' page did not load successfully."

    my_friends_page = my_habit_page.profile_banner.click_view_all_friends()
    assert my_friends_page.is_page_loaded(), "'My Friends' page did not load successfully"

    my_friends_page.select_tab("Find a friend")

    find_friend_page = FindFriendPage(context.browser)
    assert find_friend_page.is_page_loaded(), "'Find Friend' page did not load successfully"
    context.current_page = find_friend_page


@when('the user searches for "{target_user}"')
@when('searches for "{target_user}" again')
def step_user_searches_for_target_user(context, target_user):
    """When the user searches for target_user."""
    find_friend_page = context.current_page
    find_friend_page.search_friend(target_user)

    user_friend_card = find_friend_page.get_friend_card_by_name(target_user)
    assert user_friend_card.get_friend_info()["name"] == target_user, \
        f"The target user '{target_user}' was not found."

    context.target_user = target_user
    context.user_friend_card = user_friend_card


@when('clicks the "Add Friend" button on the user card')
def step_click_add_friend_button(context):
    """And clicks the "Add Friend" button on the user card."""
    find_friend_page = context.current_page

    user_friend_card = find_friend_page.get_friend_card_by_name(context.target_user)
    user_friend_card.click_add_friend_btn()

    context.user_friend_card = user_friend_card


@then('the notification "{expected_msg}" should appear')
def step_notification_should_appear(context, expected_msg):
    """Then the notification as expected should appear."""
    page = context.current_page

    actual_msg = page.get_alert_msg()
    assert actual_msg == expected_msg, \
        f"Expected notification '{expected_msg}', but got '{actual_msg}'."


@then('the button on the user card should change to "{expected_text}"')
@then('the button on the user card should still be "{expected_text}"')
@then('the button on the user card should be "{expected_text}"')
def step_button_on_the_user_card_should_change(context, expected_text):
    """And the button on the user card should change to expected."""
    actual_text = context.user_friend_card.add_friend_btn.text
    assert actual_text == expected_text, \
        (f"The label of button should be {expected_text}. "
         f"Got: {actual_text}")


@when('the user refreshes the "Find a friend" page')
def step_user_refreshes_the_page(context):
    """When the user refreshes the "Find a friend" page."""
    find_friend_page = context.current_page
    find_friend_page.refresh_page()
    assert find_friend_page.is_page_loaded(), "'Find Friend' page did not load successfully."


@when('the user opens the profile of "{target_user}"')
def step_user_opens_profile_of_target_user(context, target_user):
    """When the user opens the profile of "<target_user>"."""
    find_friend_page = context.current_page
    friend_card = find_friend_page.get_friend_card_by_name(target_user)
    user_all_habits_page = friend_card.click_friend_card()

    assert user_all_habits_page.user_info_banner.is_loaded(), \
        "'All Habits' page of the User Profile page was not loaded."
    context.user_all_habits_page = user_all_habits_page
    context.current_page = user_all_habits_page


@then('the button on the profile page should be "{expected_text}"')
@then('the button on the profile page should change to "{expected_text}"')
def step_button_on_profile_should_be_cancel(context, expected_text):
    """Then the button on the profile page should be as expected."""
    assert context.current_page.user_info_banner.friend_btn.text == expected_text, \
        (f"The label of button should be {expected_text}. "
         f"Got: {context.current_page.user_info_banner.friend_btn.text}")


@when('the user clicks the "Cancel request" button on the profile page')
def step_user_clicks_cancel_request(context):
    """When the user clicks the "Cancel request" button on the profile page."""
    context.current_page.user_info_banner.click_cancel_request()


@when('the user navigates back to the "Find Friend" page')
def step_user_navigates_back_to_find_friend_page(context):
    """When the user navigates back to the "Find Friend" page."""
    context.current_page.go_back()

    find_friend_page = FindFriendPage(context.browser)
    assert find_friend_page.is_page_loaded(), \
        "'Find Friend' page did not load successfully."
    context.current_page = find_friend_page
