"""Pytest fixture for Selenium WebDriver setup and teardown."""
import allure
import logging
from utils.logger import logger
import io
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


from data.config import Config

@fixture(params=["chrome"], scope="function")
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
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--window-size=1920,1080")
            drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(Config.DEFAULT_TIMEOUT)
    drv.get(Config.BASE_UI_URL)

    yield drv

    drv.quit()


@fixture(scope='function', autouse=True)
def capture_logs_to_allure():
    log_capture_string = io.StringIO()

    ch = logging.StreamHandler(log_capture_string)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    yield

    log_contents = log_capture_string.getvalue()

    if log_contents:
        allure.attach(
            log_contents,
            name='Test logs',
            attachment_type=allure.attachment_type.TEXT
        )

    logger.removeHandler(ch)
    log_capture_string.close()
