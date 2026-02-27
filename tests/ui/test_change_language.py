import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.common_pages.main_page import MainPage

@allure.epic("GreenCity Main Functionality")
@allure.feature("Localization")
@allure.story("User can switch site language from Header")
@allure.testcase("[Test Case]: BasePage change language #42")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify language switching (UA <-> EN) in Header")
def test_change_language(driver: WebDriver):
    """Change language test for main page."""
    main_page = MainPage(driver)

    with allure.step("Pre-condition: Ensure site is loaded in Ukrainian (UA)"):
        if main_page.header.get_new_link_text() != "Еко Новини":
            main_page.header.switch_language_to("ua")
            main_page.header.wait_for_text("Еко Новини")

        assert main_page.header.get_new_link_text() == "Еко Новини", "Text is not in Ukrainian."

    with allure.step("Step 1: Switch language to English (EN)"):
        main_page.header.switch_language_to("en")

    with allure.step("Step 2: Verify Navigation Menu text is translated to 'Eco News'"):
        main_page.header.wait_for_text("Eco News")
        assert main_page.header.get_new_link_text() == "Eco News", "Text did not switch to English."

    with allure.step("Step 3: Switch language back to Ukrainian (UA)"):
        main_page.header.switch_language_to("ua")

    with allure.step("Step 4: Verify Navigation Menu text reverted to 'Еко Новини'"):
        main_page.header.wait_for_text("Еко Новини")
        assert main_page.header.get_new_link_text() == "Еко Новини", "Text did not switch back to Ukrainian."
