import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.main_page import MainPage

@allure.title('Change language test for main page.')
def test_change_language(driver: WebDriver):
    """Change language test for main page."""
    main_page = MainPage(driver)

    assert main_page.header.get_new_link_text() == "Еко Новини", "Text of news link in header is not 'Еко Новини' by default"

    main_page.switch_language()
    assert main_page.header.get_new_link_text() == "Eco News", "Text of news link in header is not 'Eco News' after switching language"

    main_page.switch_language()
    assert main_page.header.get_new_link_text() == "Еко Новини", "Text of news link in header is not 'Еко Новини' after switching language back"
