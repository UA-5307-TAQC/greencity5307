import allure

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@allure.title("Check that user is redirected to Find Friend page "
"after clicking on the [Add friends] button")
def test_navigation_to_find_friend_page(driver_with_login):
    """Test correct navigation to Find Friend page."""

    with allure.step("Go to My Space page"):
        driver = driver_with_login
        my_habit_page = MyHabitPage(driver)

    with allure.step("Click [Add friends] button"):
        profile_banner = my_habit_page.profile_banner
        profile_banner.click_add_friends_btn()

    with allure.step("Check if user is redirected to Find Friend page"):
        url = driver.current_url
        assert "/friends/recommended" in url, f"Expected to be on Fiend Friend page, but was at: {url}"
