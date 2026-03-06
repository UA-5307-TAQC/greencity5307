"""UI test for empty Requests tab state persistence after refresh (TC-FR-02)."""

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.abstract_pages.friends_abstract.friend_requests_page import FriendRequestsPage


@pytest.mark.ui
@allure.feature("Friends")
@allure.story("Friend requests")
@allure.title("TC-FR-02: Requests tab is empty and stays empty after refresh")
def test_fr_requests_empty_after_refresh(driver: WebDriver) -> None:
    """
    TC-FR-02:
    Verify Requests tab shows empty state when user has no pending requests,
    and it remains after page refresh.
    """
    try:
        with allure.step("Step 1: Open GreenCity website"):
            driver.get(Config.BASE_UI_URL)

        with allure.step("Precondition: Login"):
            main_page = MainPage(driver)
            sign_in_modal = main_page.header.click_sign_in_link()
            sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

        friends_page = FriendRequestsPage(driver)

        with allure.step("Step 2: Open My Space"):
            friends_page.click_my_space_tab()

        with allure.step("Step 3: Navigate to Friends section"):
            friends_page.click_plus_friends()

        with allure.step("Step 4: Open Requests tab"):
            friends_page.open_requests_tab()
            assert friends_page.is_requests_tab_opened(), (
                f"Requests tab was not opened. Current URL: {driver.current_url}"
            )

        with allure.step("Step 5: Verify requests list is empty"):
            assert friends_page.get_requests_count() == 0, (
                f"Expected 0 request cards, but got {friends_page.get_requests_count()}."
            )

        allure.attach(driver.current_url, "URL on Requests tab", attachment_type=AttachmentType.TEXT)
        allure.attach(driver.get_screenshot_as_png(), "Requests empty state", attachment_type=AttachmentType.PNG)

        with allure.step("Step 7: Refresh the page"):
            driver.refresh()

        with allure.step("Step 8: Open Requests tab again (after refresh)"):
            friends_page.open_requests_tab()
            assert friends_page.is_requests_tab_opened(), (
                f"Requests tab was not opened after refresh. Current URL: {driver.current_url}"
            )

        with allure.step("Step 9: Verify requests list is empty after refresh"):
            assert friends_page.get_requests_count() == 0, (
                f"After refresh expected 0 request cards, but got {friends_page.get_requests_count()}."
            )

        allure.attach(driver.get_screenshot_as_png(), "Requests empty after refresh", attachment_type=AttachmentType.PNG)

    except Exception:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on failure",
            attachment_type=AttachmentType.PNG,
        )
        raise
