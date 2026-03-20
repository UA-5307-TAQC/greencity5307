"""UI test for verifying that Main Page loads correctly."""

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage


@allure.feature("Main Page")
@allure.story("Main page loading")
@allure.title("TC-MP-01: Verify Main Page loads correctly")
def test_main_page_loads_correctly(driver: WebDriver) -> None:
    """TC-MP-01: Verify Main Page loads correctly."""

    with allure.step("Step 1: Open browser"):
        assert driver is not None, "Browser was not opened"

    with allure.step("Step 2: Open GreenCity website"):
        driver.get(Config.BASE_UI_URL)
        main_page = MainPage(driver)

    with allure.step("Step 3: Wait until page is fully loaded"):
        assert main_page.is_loaded(), "Main page did not load"

    with allure.step("Step 4: Verify URL"):
        current_url = main_page.get_current_url()
        assert "#/greenCity" in current_url, (
            f"Unexpected URL: {current_url}"
        )

    with allure.step("Step 5: Verify page header is visible"):
        assert main_page.is_header_visible(), "Header is not visible"

    with allure.step("Step 6: Verify navigation menu is visible"):
        assert main_page.is_navigation_menu_visible(), "Navigation menu is not visible"

    with allure.step("Step 7: Verify main banner or main content section is visible"):
        assert main_page.is_page_opened(), "Main content section is not visible"

    with allure.step("Step 8: Verify page logo is visible"):
        assert main_page.is_logo_visible(), "Logo is not visible"

    with allure.step("Step 9: Scroll down the page"):
        initial_scroll = main_page.get_scroll_position()
        main_page.scroll_down_page()
        scrolled_position = main_page.get_scroll_position()

        allure.attach(
            f"Initial scroll: {initial_scroll}\nScrolled position: {scrolled_position}",
            name="Scroll positions",
            attachment_type=AttachmentType.TEXT
        )

        assert scrolled_position > initial_scroll, "Page did not scroll down"

    with allure.step("Step 10: Refresh the page"):
        main_page.refresh_page()
        refreshed_main_page = MainPage(driver)

        assert refreshed_main_page.is_loaded(), "Main page did not reload successfully"
        assert "#/greenCity" in refreshed_main_page.get_current_url(), (
            "Incorrect URL after refresh"
        )