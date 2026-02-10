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
    if browser == "firefox":
        opts = FirefoxOptions()
        if headless_flag:
            opts.headless = True
        service = FirefoxService(GeckoDriverManager().install())
        drv = webdriver.Firefox(service=service, options=opts)
    elif browser == "chrome":
        opts = ChromeOptions()
        if headless_flag:
            # use new headless mode when available
            try:
                opts.add_argument("--headless=new")
            except TypeError:
                opts.add_argument("--headless")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service, options=opts)

    drv.get(Config.BASE_UI_URL)

    yield drv

    drv.quit()
