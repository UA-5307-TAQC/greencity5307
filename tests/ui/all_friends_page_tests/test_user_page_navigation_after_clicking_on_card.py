import allure

@allure.title("Check that a user is redirected to another Friend page after clicking on a friend card on the 'All friends' tab on the Friend page")
def test_user_page_navigation_after_clicking_on_card(page_of_user_with_friends):
    """Check a user is redirected to another Friend page after clicking a friend card"""
    all_friends_page = page_of_user_with_friends

    with allure.step("Capture current URL before navigation"):
        initial_url = all_friends_page.driver.current_url

    with allure.step("Click first friend card"):
        all_habits_page = all_friends_page.cards[0].click_friend_card()

    with allure.step("Check if URL matches the expected friends list path and has changed"):
        new_url = all_habits_page.driver.current_url
        assert new_url != initial_url, (
            f"Expected to be redirected to another user profile page, but URL did not change: {new_url}"
        )
        assert "/friends" in new_url, (
            f"Expected to be on other user profile page, but was at: {new_url}"
        )

    with allure.step("Check if the user banner is displayed"):
        assert all_habits_page.has_user_banner(), f"User banner is not found"
