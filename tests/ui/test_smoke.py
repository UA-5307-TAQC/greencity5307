"""A simple smoke test for the main page."""
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainPage


@allure.title("Smoke test for the main page")
def test_example_smoke(driver: WebDriver):
    """A simple smoke test that always passes."""
    main_page = MainPage(driver)
    assert main_page.there_are.text in ("There are of us and today we", "Нас і сьогодні ми")
    news_page = main_page.go_to_eco_news()
    assert news_page.main_header.text in ("Eco news","Еко новини")
    event_page = news_page.go_to_events()
    assert event_page.main_header.text in ("Events","Події")
