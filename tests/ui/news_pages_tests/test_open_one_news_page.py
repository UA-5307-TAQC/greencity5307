"""UI test for opening Eco News article and verifying One News page details (TC-EN-02)."""

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.news_pages.eco_news_page import EcoNewsPage
from pages.news_pages.one_news_page import OneNewsPage


@pytest.mark.ui
@allure.feature("Eco News")
@allure.story("Open One News page")
@allure.title("TC-EN-02: Open Eco News article and verify details")
def test_open_eco_news_article_and_verify_details(driver_with_login: WebDriver) -> None:
    """TC-EN-02: Open Eco News article and verify One News page details are displayed."""
    driver = driver_with_login

    with allure.step("Step 2: Navigate to Eco News page"):
        driver.get(f"{Config.BASE_UI_URL}/news")
        eco_news_page = EcoNewsPage(driver)
        eco_news_page.wait_page_loaded()

    with allure.step("Step 3: Wait until at least one news card is visible"):
        eco_news_page.wait_cards_present()
        assert eco_news_page.get_cards_count() > 0, \
            "No news cards are displayed on Eco News page."

    with allure.step("Step 4: Save first news card title"):
        first_card_title = eco_news_page.get_first_card_title()
        allure.attach(
            first_card_title,
            name="First news card title",
            attachment_type=AttachmentType.TEXT,
        )
        assert first_card_title.strip(), "First news card title is empty."

    with allure.step("Step 5: Click the first news card"):
        one_news_page = eco_news_page.open_first_news_card()
        one_news_page.wait_page_loaded()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="One News screen",
            attachment_type=AttachmentType.PNG
        )

    with allure.step("Step 6: Verify the URL changes to a single news page"):
        one_news_page = OneNewsPage(driver)
        one_news_page.wait_page_loaded()
        current_url = driver.current_url
        allure.attach(
            current_url,
            name="Current URL after opening article",
            attachment_type=AttachmentType.TEXT,
        )
        assert "/news/" in current_url, \
            f"URL does not indicate One News page. Current URL: {current_url}"

    with allure.step("Step 7: Verify the news title is displayed"):
        title_text = one_news_page.get_title()
        allure.attach(
            title_text,
            name="News title",
            attachment_type=AttachmentType.TEXT,
        )
        assert title_text.strip(), "News title is not displayed or empty."

    with allure.step("Step 8: Verify the news main content/body text is displayed"):
        main_text = one_news_page.main_text.root.text
        allure.attach(
            main_text,
            name="News main text",
            attachment_type=AttachmentType.TEXT,
        )
        assert main_text.strip(), "News main content is not displayed or empty."

    with allure.step("Step 9: Verify the publication date is displayed"):
        creation_date = one_news_page.creation_date.root.text
        allure.attach(
            creation_date,
            name="Publication date",
            attachment_type=AttachmentType.TEXT,
        )
        assert creation_date.strip(), "Publication date is not displayed or empty."

    with allure.step("Step 10: Use browser Back button"):
        driver.back()

    with allure.step("Step 11: Verify Eco News page is restored"):
        eco_news_page.wait_page_loaded()
        eco_news_page.wait_cards_present()

        assert eco_news_page.is_header_visible(), \
            "Eco News page header is not visible after returning back."
        assert eco_news_page.get_cards_count() > 0, \
            "Eco News cards are not visible after returning back."

        allure.attach(
            driver.current_url,
            name="URL after returning back",
            attachment_type=AttachmentType.TEXT,
        )
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Eco News page after return",
            attachment_type=AttachmentType.PNG,
        )
