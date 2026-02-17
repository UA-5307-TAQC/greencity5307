import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.main_page import MainPage

@allure.title('Change language test for main page.')
def test_change_language(driver: WebDriver):
    """Change language test for main page."""
    main_page = MainPage(driver)

    if main_page.header.get_new_link_text() != "Еко Новини":
        main_page.header.switch_language_to("ua")

    assert main_page.header.get_new_link_text() == "Еко Новини", "Text is not in Ukrainian."

    main_page.header.switch_language_to("en")
    assert main_page.header.get_new_link_text() == "Eco News", "Text did not switch to English."

    main_page.header.switch_language_to("ua")
    assert main_page.header.get_new_link_text() == "Еко Новини", "Text did not switch back to Ukrainian ."