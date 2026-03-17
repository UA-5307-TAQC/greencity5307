"""Module that contains test case TC-FF-2."""
import allure

from data.config import Config

from pages.common_pages.main_page import MainPage


@allure.title("Verify Friend Request Persistence After User Logout and Login")
def test_find_friend_verify_persistence_after_logout(driver_with_login, target_user_not_added_to_friends):
    """Test case that verifies a sent friend request remains active after the user logs out and logs back in."""
    target_user_name = "Liubomyr Halamaha"

    with allure.step(f"Precondition: A target user '{target_user_name}' exists in the system "
                     f"who is not yet in the user's friend list."):
        target_user_not_added_to_friends(target_user_name)

    with allure.step("Step 1: "
                     "Navigate to the Greencity URL."):
        main_page = MainPage(driver_with_login)
        user_name_from_header = main_page.header.get_signed_in_user_name()

        # Expected result: The Home page loads successfully.
        assert main_page.is_loaded()
        assert user_name_from_header in [Config.USER_NAME, "Hlib", "Oleksandr"], \
            f"The expected user is not signed in. Found user: '{user_name_from_header}'"

    with allure.step("Step 2: "
                     "Click on the 'My Space' section in the header."):
        my_habit_page = main_page.header.click_my_space_link()

        # Expected result:
        # The "My Space" page loads successfully.
        assert my_habit_page.wait_page_loaded(), "'My Space' page did not load successfully."

    with allure.step("Step 3: "
                     "Click on the '+' (plus) icon in the 'My friends' section "
                     "within the profile information block."):
        find_friend_page = my_habit_page.profile_banner.click_add_friends_btn()

        # Expected result:
        # The "Find Friend" page loads successfully.
        assert find_friend_page.is_page_loaded(), "'Find Friend' page did not load successfully"

    with allure.step("Step 4: "
                     "Enter the target user name into the Search input field."):
        find_friend_page.search_friend(target_user_name)

        # Expected result:
        # The user list updates to display only the specific user matching the input
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        assert user_friend_card.get_friend_info()["name"] == target_user_name, \
            "The target user was not found."

    with allure.step("Step 5: "
                     "Click the 'Add Friend' button on the found user's card."):
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        user_friend_card.click_add_friend_btn()

        # Expected result:
        # The button label changes to "Cancel Request".
        # A notification message "Friend request sent" appears at the top of the page.
        assert find_friend_page.get_alert_msg() == "Friend request sent", \
            "A notification message did not appear."
        assert user_friend_card.add_friend_btn.text == "Cancel request", \
            "The label of the button did not change."

    with allure.step("Step 6: "
                     "Click on the User Profile icon (dropdown) in the header."):
        find_friend_page.header.click_user_menu()

        # Expected result: The user menu dropdown opens. The "Sign out" option is visible.
        assert find_friend_page.header.is_user_menu_present()

    with allure.step("Step 7: "
                     "Click the 'Sign out' button."):
        find_friend_page.header.click_user_menu_sign_out_link()

        # Expected result: The user is logged out successfully.
        # The application redirects user to the Main page.
        main_page = MainPage(driver_with_login)
        assert main_page.is_loaded()

    with allure.step("Step 8:"
                     "Click the 'Sign in' button in the header."):
        sign_in_window = main_page.header.click_sign_in_link()

        # Expected result: The "Sign in" modal window appears.
        assert sign_in_window.is_displayed()

    with allure.step("Step 9:"
                     "Enter the valid email address and password "
                     "into the Sign In fields, and click the 'Sign in' button."):
        profile_page = sign_in_window.sign_in(
            email=Config.USER_EMAIL,
            password=Config.USER_PASSWORD
        )

        # Expected result: The user is successfully logged in. The Profile page loads successfully.
        assert profile_page.wait_page_loaded()

    with allure.step("Step 10:"
                     "Click on the '+' (plus) icon in the 'My friends'"
                     " section within the profile information block."):
        find_friend_page = profile_page.profile_banner.click_add_friends_btn()

        # Expected result: The "Find Friend" page loads successfully.
        assert find_friend_page.is_page_loaded()

    with allure.step("Step 11: "
                     "Enter the same target user name into the Search input field."):
        find_friend_page.search_friend(target_user_name)

        # Expected result:
        # The user list updates to display only the specific user matching the input
        user_friend_card = find_friend_page.get_friend_card_by_name(target_user_name)
        assert user_friend_card.get_friend_info()["name"] == target_user_name, \
            "The target user was not found."
        assert user_friend_card.add_friend_btn.text == "Cancel request", \
            f"The label of the button should be 'Cancel request'"
