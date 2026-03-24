"""UI test for creating Eco News and verifying it appears in the feed (TC-EN-03)."""

import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.news_pages.eco_news_page import EcoNewsPage


@pytest.mark.ui
@allure.feature("Eco News")
@allure.story("Create Eco News")
@allure.title("TC-EN-03: Create Eco News and verify it appears in the feed")
def test_create_eco_news_and_verify_it_appears_in_feed(
    driver: WebDriver,
) -> None:
    """TC-EN-03: Create Eco News and verify it appears in the news feed."""
    news_title = f"Auto Eco News {int(time.time())}"
    news_content = (
        "This is automated Eco News content for UI testing. "
        "It contains more than twenty characters."
    )
    news_tags = ("news",)

    try:
        with allure.step("Step 1: Open GreenCity website"):
            driver.get(Config.BASE_UI_URL)

        with allure.step("Step 2: Log in"):
            main_page = MainPage(driver)
            sign_in_modal = main_page.header.click_sign_in_link()
            sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

        with allure.step("Step 3: Navigate to Eco News page"):
            driver.get(f"{Config.BASE_UI_URL}/news")
            eco_news_page = EcoNewsPage(driver)
            eco_news_page.wait_page_loaded()

        with allure.step("Step 4: Click 'Create news' button"):
            create_news_page = eco_news_page.click_create_button()
            create_news_page.wait_page_loaded()

        with allure.step("Step 5: Fill in mandatory fields"):
            create_news_page.fill_mandatory_news_form(
                news_title,
                news_tags,
                news_content,
            )

            allure.attach(
                news_title,
                name="Created news title",
                attachment_type=AttachmentType.TEXT,
            )
            allure.attach(
                news_content,
                name="Created news content",
                attachment_type=AttachmentType.TEXT,
            )

        with allure.step("Step 6: Click 'Publish/Save' (submit)"):
            create_news_page.click_submit()

        with allure.step("Step 7: Verify redirect to Eco News page"):
            eco_news_page = create_news_page.wait_redirect_to_news()
            eco_news_page.wait_page_loaded()

            allure.attach(
                driver.current_url,
                name="URL after publish",
                attachment_type=AttachmentType.TEXT,
            )

            assert "news" in driver.current_url, (
                f"User was not redirected to Eco News page. "
                f"Current URL: {driver.current_url}"
            )

        with allure.step("Step 8: Scroll through the news feed"):
            assert eco_news_page.scroll_until_news_found(news_title), (
                f"Created news '{news_title}' was not found in the feed."
            )

        with allure.step("Step 9: Find the created news title in the list"):
            assert eco_news_page.is_news_present_in_feed(news_title), (
                f"Created news '{news_title}' is not visible in the feed."
            )

        with allure.step("Step 10: Click the created news item"):
            one_news_page = eco_news_page.open_news_by_title(news_title)
            one_news_page.wait_page_loaded()

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Created One News page",
                attachment_type=AttachmentType.PNG,
            )

        with allure.step("Step 11: Verify created news article page opens"):
            assert "/news/" in driver.current_url, (
                f"Created news article page did not open. "
                f"Current URL: {driver.current_url}"
            )
            assert one_news_page.title.text.strip() == news_title, (
                "Opened article title does not match created news title."
            )
            assert one_news_page.main_text.text.strip(), (
                "Opened article main text is empty."
            )
            assert one_news_page.creation_date.text.strip(), (
                "Opened article creation date is empty."
            )

    except Exception:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on failure",
            attachment_type=AttachmentType.PNG,
        )
        raise