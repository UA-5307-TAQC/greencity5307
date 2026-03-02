import allure
from selenium.webdriver.remote.webdriver import WebDriver
from utils.logger import logger
from pages.common_pages.main_page import MainPage


@allure.title("Smoke test for the main page")
def test_example_smoke(driver: WebDriver):
    """A simple smoke test that always passes."""

    logger.info("Starting Smoke Test")
    main_page = MainPage(driver)

    with allure.step("Verify Main Page content"):
        logger.info("Checking 'There are' text on Main Page")
        assert (main_page.there_are.text == "There are of us and today we" or
                main_page.there_are.text == "Нас і сьогодні ми")

    with allure.step("Navigate to Eco News"):
        logger.info("Clicking 'News' link in header")
        news_page = main_page.header.click_new_link()
        assert (news_page.main_header.text == "Eco news" or
                news_page.main_header.text == "Еко новини")

    with allure.step("Navigate to Events"):
        logger.info("Clicking 'Events' link in header (from News page context)")
        event_page = news_page.header.click_event_link()
        assert (event_page.main_header.text == "Events" or
                event_page.main_header.text == "Події")

    logger.info("Smoke Test finished successfully")
