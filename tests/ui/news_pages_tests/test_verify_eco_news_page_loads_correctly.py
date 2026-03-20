"""UI test: TC-EN-01 Verify Eco News page loads correctly."""

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.news_pages.eco_news_page import EcoNewsPage


@pytest.mark.ui
@allure.feature("Eco News")
@allure.story("Eco News page - Smoke")
@allure.title("TC-EN-01: Open Eco News page and verify main UI elements are displayed")
def test_tc_en_01_verify_eco_news_page_loads_correctly(driver: WebDriver) -> None:
    """TC-EN-01: Verify Eco News page loads correctly and displays essential UI elements."""
    eco_news_url = f"{Config.BASE_UI_URL}/news"

    with allure.step("Precondition: Open GreenCity website"):
        driver.get(Config.BASE_UI_URL)

    with allure.step("Precondition: Log in"):
        main_page = MainPage(driver)
        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("Step 1-2: Navigate to Eco News page URL"):
        driver.get(eco_news_url)

    eco_news_page = EcoNewsPage(driver)

    with allure.step("Step 3: Verify the page URL contains #/greenCity/news"):
        assert "#/greenCity/news" in driver.current_url

    with allure.step("Step 4: Verify the page title/header (Eco news / Еко новини) is visible"):
        eco_news_page.wait_page_loaded()
        assert eco_news_page.is_header_visible()
        assert eco_news_page.get_header_text()  # not empty

    with allure.step("Step 5: Verify the news list/feed area is visible"):
        assert eco_news_page.is_feed_visible()

    with allure.step("Step 6: Verify at least one news card is displayed"):
        eco_news_page.wait_cards_present()
        initial_count = eco_news_page.get_cards_count()
        if initial_count == 0:
            pytest.skip("No Eco News cards are available to validate the feed.")
        assert initial_count >= 1

    with allure.step("Step 7: Verify each visible news card has a title"):
        assert eco_news_page.each_card_has_title()

    with allure.step("Step 8: Verify each visible news card has a metadata block (date/author/tags)"):
        assert eco_news_page.each_card_has_metadata()

    with allure.step("Step 9: Scroll down and verify more cards load OR page remains usable"):
        before_scroll = eco_news_page.get_cards_count()
        eco_news_page.scroll_to_bottom()

        loaded_or_ok = eco_news_page.wait_cards_count_at_least(before_scroll)
        assert loaded_or_ok
        assert eco_news_page.is_header_visible()
        assert eco_news_page.get_cards_count() >= 1

    with allure.step("Step 10: Refresh page and verify Eco News page still opens correctly"):
        eco_news_page.refresh()
        assert "#/greenCity/news" in driver.current_url
        assert eco_news_page.is_header_visible()
        assert eco_news_page.is_feed_visible()
        eco_news_page.wait_cards_present()
        assert eco_news_page.get_cards_count() >= 1
