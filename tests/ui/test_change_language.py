import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.main_page import MainPage

@allure.title('Change language test for main page.')
def test_change_language(driver: WebDriver):
    """Change language test for main page."""
    main_page = MainPage(driver)

    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element(main_page.eco_news_locator, "Еко Новини"),
        message="Текст не змінився на 'Еко Новини' після перемикання"
    )
    assert main_page.eco_news.text == "Еко Новини"

    main_page.change_language_button.click()
    main_page.language_option_en.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element(main_page.eco_news_locator, "Eco News"),
        message="Текст не змінився на 'Eco News' після перемикання"
    )
    assert main_page.eco_news.text == "Eco News"

    main_page.change_language_button.click()
    main_page.language_option_en.click()

    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element(main_page.eco_news_locator, "Еко Новини"),
        message="Текст не змінився на 'Еко Новини' №2 після перемикання"
    )
    assert main_page.eco_news.text == "Еко Новини"
