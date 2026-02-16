import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainPage


@allure.title("Smoke test for the main page")
def test_example_smoke(driver: WebDriver):
    """A simple smoke test that always passes."""
    main_page = MainPage(driver)
    assert (main_page.there_are.text == "There are of us and today we" or
            main_page.there_are.text == "Нас і сьогодні ми")
    news_page = main_page.header.click_new_link()
    assert (news_page.main_header.text == "Eco news" or
            news_page.main_header.text == "Еко новини")
    event_page = news_page.header.click_event_link()
    assert (event_page.main_header.text == "Events" or
            event_page.main_header.text == "Події")
