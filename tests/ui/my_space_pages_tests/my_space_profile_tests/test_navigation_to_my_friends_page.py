import allure
import pytest

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@allure.title("Check that user is redirected to My Friends page")
def test_navigation_to_friends_page(driver_with_login):
    """Test correct navigation to My Friends page."""

    with allure.step("Go to My Space page"):
        driver = driver_with_login
        my_habit_page = MyHabitPage(driver)

    profile_banner = my_habit_page.profile_banner
    if profile_banner.friends_images_exist():
        with allure.step("Click 'See all' link if user has friends"):
            profile_banner.click_view_all_friends()

        with allure.step("Check if user is redirected to My Friends page"):
            url = driver.current_url
            assert "/friends" in url, f"Expected to be on My Friends page, but was at: {url}"
    else:
        pytest.skip("Skip test because there is no 'See all' link")
