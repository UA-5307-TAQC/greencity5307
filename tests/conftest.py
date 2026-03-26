"""Pytest fixture for Selenium WebDriver setup and teardown."""
import io
import logging
from datetime import datetime

import allure
from allure_commons.types import AttachmentType

from pytest import fixture, hookimpl

from utils.logger import logger


@hookimpl(hookwrapper=True)
# pylint: disable=redefined-outer-name
def pytest_runtest_makereport(item):
    """Hook to make screenshots and attach them to allure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        web_driver = item.funcargs.get("driver")

        if web_driver:
            try:
                test_name = item.name_schema
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name=f"failed_{test_name}_{timestamp}",
                    attachment_type=AttachmentType.PNG
                )
            except Exception:  # pylint: disable=broad-except
                # Ignore screenshot capture errors to avoid masking the original test failure
                pass


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
