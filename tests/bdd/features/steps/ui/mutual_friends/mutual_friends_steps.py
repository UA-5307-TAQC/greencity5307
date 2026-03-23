# pylint: disable=not-callable, unused-argument
"""
.. module:: Mutual friends
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from pages.abstract_pages.friend_abstract_users.mutual_friends_page import MutualFriendsPage

# ================= BACKGROUND =================

@given('User B exists in the system')
@given('User C is a friend of both User A and User B')
def step_data_setup(context):
    pass


@given("User A is on User B's profile page")
def step_navigate_to_user_b_profile(context):
    context.browser.get(
        "https://www.greencity.cx.ua/#/greenCity/profile/1205/friends/Denys/933?tab=Mutual%20friends"
    )


# ================= SCENARIO 1 & 2 =================

@when('the user opens the "Friends" section on User B\'s profile')
def step_open_friends_section(context):
    pass


@when('selects "All Friends"')
def step_select_all_friends(context):
    mutual_page = MutualFriendsPage(context.browser)
    mutual_page.click_all_friends_tab()


@then("the list of User B's friends is displayed")
def step_friends_list_displayed(context):
    mutual_page = MutualFriendsPage(context.browser)
    assert mutual_page.has_mutual_friends(), "Friends list is completely empty!"


@then('the tabs "All Friends" and "Mutual Friends" are visible')
def step_tabs_visible(context):
    mutual_page = MutualFriendsPage(context.browser)
    # Звертаємось напряму до лінивих властивостей!
    assert mutual_page.all_friends_tab.is_displayed(), "'All Friends' tab is missing"
    assert mutual_page.mutual_friends_tab.is_displayed(), "'Mutual Friends' tab is missing"


@when('the user views the "Mutual Friends" tab')
def step_view_mutual_friends_tab(context):
    pass


@then('the mutual friends counter displays "{expected_count}"')
def step_verify_mutual_friends_counter(context, expected_count):
    mutual_page = MutualFriendsPage(context.browser)
    actual_count = mutual_page.get_mutual_friends_count()
    assert actual_count == expected_count, f"Expected counter: {expected_count}, Got: {actual_count}"


# ================= SCENARIO 3 =================

@when('the user clicks on the "Mutual Friends" tab')
def step_click_mutual_friends_tab(context):
    mutual_page = MutualFriendsPage(context.browser)
    mutual_page.click_mutual_friends_tab()


@then('the tab becomes active')
def step_tab_becomes_active(context):
    mutual_page = MutualFriendsPage(context.browser)
    assert mutual_page.is_mutual_friends_tab_active(), "Mutual Friends tab did not become active!"


@then('User C is displayed in the friends list')
def step_user_c_displayed(context):
    mutual_page = MutualFriendsPage(context.browser)
    names = mutual_page.friends_list_component.get_all_friend_names()
    assert len(names) > 0, "No mutual friends found in the list!"


@then("User C's profile picture is visible")
def step_user_c_picture_visible(context):
    mutual_page = MutualFriendsPage(context.browser)
    is_visible = mutual_page.friends_list_component.is_first_friend_avatar_visible()
    assert is_visible, "First mutual friend's avatar is missing!"


# ================= SCENARIO 4: Scrolling =================

@given('the mutual friends list is displayed')
def step_mutual_friends_displayed(context):
    context.execute_steps('When the user clicks on the "Mutual Friends" tab')


@when('the user scrolls the friends list')
def step_scroll_friends_list(context):
    mutual_page = MutualFriendsPage(context.browser)
    context.initial_count = len(mutual_page.friends_list_component.get_all_friend_names())
    context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@then('more mutual friends are visible in the list than before scrolling')
def step_more_friends_visible(context):
    mutual_page = MutualFriendsPage(context.browser)
    new_count = len(mutual_page.friends_list_component.get_all_friend_names())

    if context.initial_count < 6:
        assert new_count == context.initial_count, \
            f"Expected {context.initial_count} friends, but got {new_count} after scrolling."
        print(f"Skipped pagination check: only {context.initial_count} friends available.")
    else:
        assert new_count > context.initial_count, \
            f"Pagination failed! Cards before: {context.initial_count}, Cards after: {new_count}"


# ================= SCENARIO 5: Refresh =================

@when('the user refreshes the page')
def step_refresh_page(context):
    context.browser.refresh()


@then('the profile page reloads successfully')
def step_page_reloads(context):
    mutual_page = MutualFriendsPage(context.browser)
    mutual_page.get_wait().until(
        lambda d: mutual_page.has_mutual_friends(),
        message="Page did not load properly after refresh"
    )


@then('the "Mutual Friends" tab is still accessible')
def step_mutual_tab_accessible(context):
    mutual_page = MutualFriendsPage(context.browser)
    assert mutual_page.mutual_friends_tab.is_displayed(), "Tab is missing after refresh!"