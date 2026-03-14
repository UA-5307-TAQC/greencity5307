import allure

allure.title("Check that the 'This user has no friends' message is shown "
"on the 'All friends' tab on the Friend page for a user without friends")
def test_user_without_friends_shows_placeholder_message(page_of_user_without_friends):
    """Check message on the empty 'All friends' tab on the Friend page"""
    all_friends_page = page_of_user_without_friends

    with allure.step("Check if there is an empty 'All friends' tab on the Friend page"):
        assert all_friends_page is not None, "Could not find any empty all friends page in the list"

    with allure.step("Check if the message on the empty 'All friends' tab on the Friend page is correct"):
        default_text = all_friends_page.get_default_text()
        assert default_text == "This user has no friends", "The default text is wrong"
