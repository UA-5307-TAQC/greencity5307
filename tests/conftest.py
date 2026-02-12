"""Pytest fixture for Selenium WebDriver setup and teardown."""

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data.config import Config


@fixture(params=["chrome"], scope="function")
def driver(request):
    """
    Parametrized pytest fixture that returns a Selenium WebDriver for Chrome and Firefox.
    - Param values: "chrome" or "firefox"
    - Set `HEADLESS` env var to `1` or `true` to enable headless mode.
    """
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
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--window-size=1920,1080")
            drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(Config.DEFAULT_TIMEOUT)
    drv.get(Config.BASE_UI_URL)

    yield drv

    drv.quit()
