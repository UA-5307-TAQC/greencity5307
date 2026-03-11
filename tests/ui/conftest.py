import pytest
import allure

from data.config import Config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.common_pages.main_page import MainPage


@pytest.fixture(params=["chrome"], scope="function")
def driver(request):
    """
    Parametrized pytest fixture that returns a Selenium WebDriver for Chrome and Firefox.
    - Param values: "chrome" or "firefox"
    - Set `HEADLESS` env var to `1` or `true` to enable headless mode.
    """
    allure.dynamic.parameter("browser", request.param)
    browser = request.param
    headless_flag = Config.HEADLESS

    drv = None
    match browser:
        case "firefox":
            opts = FirefoxOptions()
            if headless_flag:
                opts.headless = True
            drv = webdriver.Firefox(options=opts)
        case "chrome":
            opts = ChromeOptions()
            if headless_flag:
                opts.add_argument("--headless=new")
            opts.add_argument(f"--lang={Config.BROWSER_LANG}")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--window-size=1920,1080")
            drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(Config.IMPLICITLY_WAIT)
    drv.get(Config.BASE_UI_URL)

    yield drv

    drv.quit()


@pytest.fixture(scope="function")
# pylint: disable=redefined-outer-name
def driver_with_login(driver):
    """Fixture that logs in the user before yielding the WebDriver."""

    with allure.step(f"Logging in the user with email: {Config.USER_EMAIL}"):
        main_page = MainPage(driver)
        sign_in_form = main_page.header.click_sign_in_link()
        sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()
    yield driver
