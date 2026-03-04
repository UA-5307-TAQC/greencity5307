"""UI test for accepting a friend request (TC-FR-03)."""

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.friend_requests_page import FriendRequestsPage


@pytest.mark.ui
@allure.feature("Friends")
@allure.story("Friend requests")
@allure.title("TC-FR-03: Accept friend request")
def test_fr_accept_friend_request(driver: WebDriver) -> None:
    """TC-FR-03: Accept friend request and verify it appears in My Friends after refresh."""
    try:
        with allure.step("Step 1: Open GreenCity website"):
            driver.get(Config.BASE_UI_URL)

        with allure.step("Precondition: Login"):
            main_page = MainPage(driver)
            sign_in_modal = main_page.header.click_sign_in_link()
            sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

        with allure.step("Step 2: Open My Space"):
            friends_page = FriendRequestsPage(driver)
            friends_page.click_my_space_tab()

        with allure.step("Step 3: Navigate to Friends section"):
            friends_page.click_plus_friends()

        with allure.step("Step 4: Open Requests tab"):
            friends_page.open_requests_tab()

        with allure.step("Step 5: Verify at least one friend request card is shown"):
            assert friends_page.get_request_cards(), "No friend request cards are visible."

        with allure.step("Step 6: Verify Accept button is visible on request card"):
            assert friends_page.is_accept_button_visible_on_first_card(), \
                "Accept button is not visible on the first card."

        with allure.step("Step 7: Click Accept button for first request"):
            username = friends_page.get_first_request_username()
            allure.attach(username, name="Accepted username", attachment_type=AttachmentType.TEXT)
            friends_page.accept_request_for_user(username)

        with allure.step("Step 8: Open My Friends tab"):
            friends_page.open_my_friends_tab()
            assert "/friends" in driver.current_url and "/requests" not in driver.current_url, (
                f"Still not in My Friends tab. Current URL: {driver.current_url}"
            )
        allure.attach(driver.current_url, "URL after opening My Friends", attachment_type=AttachmentType.TEXT)
        allure.attach(driver.get_screenshot_as_png(), "My Friends screen", attachment_type=AttachmentType.PNG)

        with allure.step("Step 10: Verify accepted user appears in My Friends list"):
            assert friends_page.is_user_present_in_my_friends(username), \
                f"Accepted user '{username}' not found in My Friends."

        with allure.step("Step 11: Refresh the page"):
            driver.refresh()

        with allure.step("Step 12: Verify friend is still present after refresh"):
            assert friends_page.is_user_present_in_my_friends(username), \
                f"After refresh, user '{username}' is not present in My Friends."

    except Exception:
        # screenshot on fail
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on failure",
            attachment_type=AttachmentType.PNG,
        )
        raise
