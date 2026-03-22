from types import SimpleNamespace

import allure
from behave import use_fixture
from behave.fixture import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@fixture
def browser(context):
    """Behave fixture: provide a Selenium Chrome WebDriver.

    The fixture configures ChromeOptions using values from ``Config`` (for
    headless mode, language, window size, etc.), creates a WebDriver, sets
    an implicit wait, navigates to the configured base URL, then yields the
    WebDriver to the scenario. The driver is quit after the scenario ends.

    Args:
        context: Behave context object used to store the created driver on
            ``context.browser``.

    Yields:
        selenium.webdriver.Chrome: the configured Chrome WebDriver instance.
    """
    opts = ChromeOptions()
    if Config.HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument(f"--lang={Config.BROWSER_LANG}")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    context.browser = webdriver.Chrome(options=opts)
    context.browser.implicitly_wait(Config.IMPLICITLY_WAIT)
    context.browser.get(Config.BASE_UI_URL)

    yield context.browser

    context.browser.quit()


@fixture
def driver_with_login(context):
    """Behave fixture: provide a WebDriver with a logged-in user.

    This fixture reuses the ``browser`` fixture to obtain a WebDriver,
    performs a sign-in interaction using the application's MainPage and the
    ``Config`` credentials, waits until the post-login page is loaded, and
    yields the authenticated driver for scenario use. The driver is later
    cleaned up by the standard fixture teardown.

    Args:
        context: Behave context object.

    Yields:
        selenium.webdriver.Chrome: an authenticated WebDriver instance.
    """
    driver = use_fixture(browser, context)
    with allure.step(f"Logging in the user with email: {Config.USER_EMAIL}"):
        main_page = MainPage(driver)
        sign_in_form = main_page.header.click_sign_in_link()
        sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()
    yield driver


@fixture
def create_habit_page_context(context):
    """Fixture for navigation to Create Habit page."""
    driver = use_fixture(driver_with_login, context)

    with allure.step("Go to Create Habit page"):
        my_habit_page = MyHabitPage(driver)
        habits_page = my_habit_page.click_add_new_habit_button()

        create_habit_button = habits_page.get_create_habit_button()
        create_habit_page = create_habit_button.click_create_habit_btn()
    context.habit_data = SimpleNamespace(
        driver=driver,
        create_page=create_habit_page,
        all_habits_page=habits_page
    )

    yield context.habit_data


fixture_registry = {
    "fixture.browser": browser,
    "fixture.driver_with_login": driver_with_login,
    "fixture.create_habit": create_habit_page_context,
}
