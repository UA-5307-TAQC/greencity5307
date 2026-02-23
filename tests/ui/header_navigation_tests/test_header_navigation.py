"""File to test header navigation."""

import allure
from selenium.common import NoSuchElementException

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.common_components.auth_components.signin_modal_component import \
    SignInComponent
from data.config import Config

from pages.main_page import MainPage
from pages.my_space_abstract_page import MySpaceAbstractPage
from utils.logger import logger


@allure.epic("GreenCity header functionality.")
@allure.feature("Header navigation.")
@allure.story("User can be navigated to correct pages.")
@allure.testcase("https://github.com/ita-social-projects/GreenCity/issues/44")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Header navigation test.")
def test_header_navigation(driver: WebDriver):
    """Function to test header navigation."""

    main_page = MainPage(driver)

    with allure.step("Pre-condition: ensure site is loaded, sign in, and land on My Space page."):
        initial_url = driver.current_url


        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        try:
            sign_in_modal.sign_in(driver, Config.USER_EMAIL, Config.USER_PASSWORD)
        except NoSuchElementException:
            logger.warning(
                "Caught NoSuchElementException from eager initialization in MyHabitPage. Ignoring and proceeding...")

        WebDriverWait(driver, 10).until(
            EC.url_changes(initial_url),
            message="URL did not change after login. Login might have failed."
        )

        my_space_page = MySpaceAbstractPage(driver)
        assert ("profile" in driver.current_url and
                my_space_page.my_habits_tab.text in
                ("My habits", "Мої звички")), "This is not my space page."

    with allure.step("Step 1: Click on 'Eco News', and ensure the site loaded on eco news page."):
        eco_news_page = main_page.go_to_eco_news()
        assert ("news" in driver.current_url
                and eco_news_page.main_header.text in ("Eco news", "Еко новини")), "This is not Eco News page."

    with allure.step("Step 2: Click on 'Events', and ensure the site loaded on events page."):
        event_page = eco_news_page.go_to_events()
        assert ("events" in driver.current_url
                and event_page.main_header.text in ("Events", "Події")), "This is not Events page."

    with allure.step("Step 3: Click on 'Places', and ensure the site loaded on places page."):
        places_page = event_page.go_to_places()
        assert ("places" in driver.current_url and
                places_page.add_place_button.text in ("Add place", "Додати місце")), "This is not places page."


    with allure.step("Step 4: Click on 'About us', and ensure the site loaded on about us page."):
        about_us_page = places_page.go_to_about_us()
        assert ("about" in driver.current_url and
                about_us_page.header_one.text in ("About Us", "Про Нас")), "This is not about us page."


    with allure.step("Step 5: Click on 'Main page', and ensure the site loaded on my space page."):
        main_page = about_us_page.go_to_main_page()
        assert ("greenCity" in driver.current_url and
                main_page.there_are.text in
                ("Нас і сьогодні ми", "There are of us and today we")), "This is not main page."