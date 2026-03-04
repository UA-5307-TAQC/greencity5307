import allure

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@allure.title("Check that user is redirected to Edit Profile page "
"after clicking on the [Edit] button")
def test_navigation_to_edit_profile_page(driver_with_login):
    """Test correct navigation to Edit Profile page."""

    with allure.step("Go to My Space page"):
        driver = driver_with_login
        my_habit_page = MyHabitPage(driver)

    with allure.step("Click [Edit] button"):
        profile_banner = my_habit_page.profile_banner
        profile_banner.click_edit_btn()

    with allure.step("Check if user is redirected to Edit Profile page"):
        url = driver.current_url
        assert "edit" in url, f"Expected to be on friends page, but was at: {url}"
        