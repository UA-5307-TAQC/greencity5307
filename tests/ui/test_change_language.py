import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.main_page import MainPage

@allure.title('Change language test for main page.')
def test_change_language(driver: WebDriver):
    """Change language test for main page."""
    main_page = MainPage(driver)

    assert main_page.is_header_text_correct("Еко Новини"), "Текст не змінився на 'Еко Новини' після перемикання"

    main_page.switch_language()
    assert main_page.is_header_text_correct("Eco News"), "Текст не змінився на 'Eco News' після перемикання"

    main_page.switch_language()
    assert main_page.is_header_text_correct("Еко Новини"), "Текст не змінився на 'Еко Новини' після перемикання"
