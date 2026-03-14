import allure

allure.title("Check that friend card has username, city, and [Add friend] button "
"on the 'All friends' tab on the Friend page for a user with friends")
def test_user_card_ui_elements_presence(page_of_user_with_friends):
    """Check if a user card has username, user city, and [Add friend] button"""
    all_friends_page = page_of_user_with_friends

    with allure.step("Check if the user card has username"):
        first_card = all_friends_page.cards[0]
        assert first_card.has_username(), "Username is missing on a user card"

    with allure.step("Check if the user card has user city"):
        assert first_card.has_user_city(), "User city is missing on a user card"

    with allure.step("Check if the user card has username"):
        assert first_card.has_add_user_btn(), "[Add friend] button is missing on a user card"
