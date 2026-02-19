"""Pytest fixture for Selenium WebDriver setup and teardown."""
import io
import logging
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data.config import Config
from utils.logger import logger


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to make screenshots and attach them to allure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        web_driver = item.funcargs.get("driver")

        if web_driver:
            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            allure.attach(web_driver.get_screenshot_as_png(),
                          name=f"failed_{test_name}_{timestamp}",
                          attachment_type=AttachmentType.PNG, )


@fixture(scope='function', autouse=True)
def capture_logs_to_allure():
    """Capture logs to allure."""
    log_capture_string = io.StringIO()

    ch = logging.StreamHandler(log_capture_string)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    yield

    log_contents = log_capture_string.getvalue()

    if log_contents:
        allure.attach(log_contents, name='Test logs', attachment_type=allure.attachment_type.TEXT)

    logger.removeHandler(ch)
    log_capture_string.close()
