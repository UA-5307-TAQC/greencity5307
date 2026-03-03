"""File to test if changing language button works correctly."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.common_pages.main_page import MainPage


@allure.epic("GreenCity Main Functionality")
@allure.feature("Localization")
@allure.story("User can switch site language from Header")
@allure.testcase("https://github.com/ita-social-projects/GreenCity/issues/42")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify language switching (UA <-> EN) in Header")
def test_change_language(driver: WebDriver):
    """Change language test for main page."""
    main_page = MainPage(driver)

    with allure.step("Pre-condition: Ensure site is loaded in Ukrainian (UA)"):
        if main_page.there_are.text != "Нас і сьогодні ми":
            main_page.header.switch_language()

        main_page.get_wait().until(lambda d: main_page.there_are.text == "Нас і сьогодні ми")
        assert main_page.there_are.text == "Нас і сьогодні ми", \
            f"Expected 'Нас і сьогодні ми', but got '{main_page.there_are.text}'"

    with allure.step("Step 1: Switch language to English (EN) and ensure the main text"
                     "translated to 'There are of us and today we'"):
        main_page.header.switch_language()
        main_page.get_wait().until(lambda d: main_page.there_are.text == "There are of us and today we")

        assert main_page.there_are.text == "There are of us and today we", \
            f"Expected 'There are of us and today we', but got '{main_page.there_are.text}'"

    with allure.step("Step 2: Switch language back to Ukrainian (UA) and ensure the main text"
                     "translated to 'Нас і сьогодні ми'"):
        main_page.header.switch_language()
        main_page.get_wait().until(lambda d: main_page.there_are.text == "Нас і сьогодні ми")

        assert main_page.there_are.text == "Нас і сьогодні ми", \
            f"Expected 'Нас і сьогодні ми', but got '{main_page.there_are.text}'"
