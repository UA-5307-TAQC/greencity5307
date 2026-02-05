from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainPage


def test_example_smoke(driver: WebDriver):
    """A simple smoke test that always passes."""
    main_page = MainPage(driver)
    assert main_page.there_are.text == "There are of us and today we"
    news_page = main_page.header.click_new_link()
    assert news_page.main_header.text == "Eco news"
    event_page = news_page.header.click_event_link()
    assert event_page.main_header.text == "Events"
