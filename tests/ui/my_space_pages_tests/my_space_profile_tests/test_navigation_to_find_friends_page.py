import allure
import pytest

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@allure.title("Check that user is redirected to Find Friends page")
def test_navigation_to_find_friends_page(driver_with_login):
    """Test correct navigation to Find Friends page."""

    with allure.step("Go to My Space page"):
        driver = driver_with_login
        my_habit_page = MyHabitPage(driver)

    profile_banner = my_habit_page.profile_banner
    if profile_banner.friends_images_exist():
        pytest.skip("Skip test because there is no [Add friends]")

    with allure.step("Click [Add friends] if user has no friends"):
        profile_banner.click_add_friends_btn()

    with allure.step("Check if user is redirected to Find Friend page"):
        url = driver.current_url
        assert "/friends/recommended" in url, f"Expected to be on Find Friend page, but was at: {url}"
