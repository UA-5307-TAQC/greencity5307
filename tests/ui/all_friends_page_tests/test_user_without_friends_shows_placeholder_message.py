import allure


@allure.title("Empty State")
@allure.description("Check that the 'This user has no friends' message is shown "
                    "on the 'All friends' tab on the Friend page for a user without friends")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Liubov Titova")
@allure.testcase("https://github.com/UA-5307-TAQC/greencity5307/issues/32", "TC-007")
def test_user_without_friends_shows_placeholder_message(page_of_user_without_friends):
    """Check message on the empty 'All friends' tab on the Friend page"""
    all_friends_page = page_of_user_without_friends

    with allure.step("Check if the message on the empty 'All friends' tab on the Friend page is correct"):
        default_text = all_friends_page.get_default_text()
        assert default_text == "This user has no friends", "The default text is wrong"
