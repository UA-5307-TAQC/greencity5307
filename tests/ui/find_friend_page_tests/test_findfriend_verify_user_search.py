import allure

from data.config import Config

from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.abstract_pages.friends_abstract.find_friend_page import FindFriendPage


@allure.title("Verify user search, friend request sending, persistence, and cancellation")
def test_find_friend_verify_user_search_friend_request(driver_with_login, target_user_not_added_to_friends):
    target_user_name = "Liubomyr Halamaha"

    with allure.step("Step 1: Navigate to the GreenCity URL"):
        main_page = MySpaceAbstractPage(driver_with_login).header.click_logo()

        # Expected result:
        # The main page loads successfully. The user is logged in.
        assert main_page.is_loaded()

        user_name_from_header = main_page.header.get_signed_in_user_name()
        assert user_name_from_header in [Config.USER_NAME, "Hlib", "Oleksandr"], \
            f"The expected user is not signed in. Found user: '{user_name_from_header}'"

    with allure.step("Step 2: Click on the 'My Space' section in the header"):
        my_habit_page = main_page.header.click_my_space_link()

        # Expected result:
        # The "My Space" page loads successfully.
        assert my_habit_page.wait_page_loaded(), "'My Space' page did not load successfully."

    with allure.step("Step 3: Click on the 'See all' link in the 'My Friends' section "
                     "within the profile information banner"):
        my_friends_page = my_habit_page.profile_banner.click_view_all_friends()

        # Expected result:
        # The "My Friends" page loads successfully.
        assert my_friends_page.is_page_loaded(), "'My Friends' page did not load successfully"

    with allure.step("Step 4: Click on 'Find a friend' tab on 'My Friends' page."):
        my_friends_page.select_tab("Find a friend")
        find_friend_page = FindFriendPage(driver_with_login)

        # Expected result:
        # The "Find a friend" page loads successfully.
        assert find_friend_page.is_page_loaded()

    with allure.step("Step 5: Enter the target username into the Search input field"):
        find_friend_page.search_friend(target_user_name)

        # Expected result:
        # The user list updates to display only the specific user matching the input
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        assert user_friend_card.get_friend_info()["name"] == target_user_name, \
            "The target user was not found."

    with allure.step("Step 6: Click the 'Add Friend' button on the found user's card"):
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        user_friend_card.click_add_friend_btn()

        # Expected result:
        # The button label changes to "Cancel Request".
        # A notification message "Friend request sent" appears at the top of the page.
        assert find_friend_page.get_alert_msg() == "Friend request sent", \
            "A notification message did not appear."
        assert user_friend_card.add_friend_btn.text == "Cancel request", \
            "The label of the button did not change."

    with allure.step("Step 7: Refresh the page."):
        find_friend_page.refresh_page()

        # Expected result:
        # The "Find Friend" page reloads successfully.
        # The Search input field is cleared, and the full list of users is displayed.
        assert find_friend_page.is_page_loaded(), "'Find Friend' page did not load successfully."

    with allure.step("Step 8: Enter the same target username into the Search input field."):
        find_friend_page.search_friend(target_user_name)

        # Expected result:
        # The user list updates to display only the specific user.
        # The "Cancel Request" button is displayed on the user card.
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        assert user_friend_card.get_friend_info()["name"] == target_user_name, \
            "The target user was not found."
        assert user_friend_card.add_friend_btn.text == "Cancel request", \
            "The label of the button was changed after reloading of the page."

    with allure.step("Step 9: Click on the user card."):
        friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        user_all_habits_page = friend_card.click_friend_card()

        # Expected result:
        # The specific User Profile page loads successfully.
        # The "Cancel Request" button is displayed in the profile information block.
        assert user_all_habits_page.user_info_banner.is_loaded(), \
            "'All Habits' page of the User Profile page was not loaded."
        assert user_all_habits_page.user_info_banner.friend_btn.text == "Cancel request"

    with allure.step("Step 10: Click on the 'Cancel Request' button."):
        user_all_habits_page.user_info_banner.click_cancel_request()

        # Expected result:
        # The button label changes to "Add Friend".
        # A notification message "Your friend request has been canceled" appears at the top of the page.
        assert user_all_habits_page.get_alert_msg() == "Your friend request has been canceled", \
            "The notification message did not appear"
        assert user_all_habits_page.user_info_banner.friend_btn.text == "Add friend"

    with allure.step("Step 11: Navigate back to the previous page ('Find Friend' page)."):
        user_all_habits_page.go_back()
        find_friend_page = FindFriendPage(driver_with_login)

        # Expected result:
        # The "Find Friend" page loads successfully.
        # The Search input field is cleared, and the full list of users is displayed.
        assert find_friend_page.is_page_loaded(), \
            "'Find Friend' page did not load successfully."

    with allure.step("Step 12: Enter the same target username into the Search input field."):
        find_friend_page.search_friend(target_user_name)
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)

        # Expected result:
        # The user list updates to display only the specific user.
        # The "Add Friend" button is displayed on the user card.
        assert user_friend_card.get_friend_info()["name"] == target_user_name, \
            "The target user was not found."
        assert user_friend_card.add_friend_btn.text == "Add friend"
