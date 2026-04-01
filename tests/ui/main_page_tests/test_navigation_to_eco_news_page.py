"""UI test for verifying navigation from Main Page to Eco News page."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage


@allure.feature("Main Page")
@allure.story("Navigation to Eco News")
@allure.title("TC-MP-02: Verify navigation from Main Page to Eco News page")
def test_navigation_to_eco_news_page(driver: WebDriver) -> None:
    """TC-MP-02: Verify navigation from Main Page to Eco News page."""

    with allure.step("Step 1: Open browser"):
        assert driver is not None, "Browser was not opened"

    with allure.step("Step 2: Open GreenCity website"):
        driver.get(Config.BASE_UI_URL)
        main_page = MainPage(driver)

    with allure.step("Step 3: Verify main page is opened"):
        assert main_page.is_loaded(), "Main page is not displayed"

    with allure.step("Step 4: Locate navigation menu/header links"):
        assert main_page.is_header_visible(), "Header is not visible"
        assert main_page.is_navigation_menu_visible(), "Navigation elements are not visible"

    with allure.step("Step 5: Find 'Eco News' link"):
        assert main_page.header.new_link.is_displayed(), "Eco News link is not visible"

    with allure.step("Step 6: Click 'Eco News' link"):
        eco_news_page = main_page.go_to_eco_news()

    with allure.step("Step 7: Wait until Eco News page is loaded"):
        assert eco_news_page.is_loaded(), "Eco News page is not displayed"

    with allure.step("Step 8: Verify Eco News URL"):
        assert "#/greenCity/news" in eco_news_page.get_current_url(), (
            f"Unexpected URL: {eco_news_page.get_current_url()}"
        )

    with allure.step("Step 9: Verify Eco News page header/title is visible"):
        assert eco_news_page.is_title_visible(), "Eco News page title is not visible"

    with allure.step("Step 10: Verify news feed is visible"):
        eco_news_page.wait_cards_present()
        assert eco_news_page.get_cards_count() > 0, "Eco News content is not visible"
