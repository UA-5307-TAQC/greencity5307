"""Allure step decorator that also writes step boundaries to the live console logger.

Drop-in replacement for ``@allure.step``:

    from utils.allure_step import step

    @step("Click login button")
    def click_login(self) -> None:
        ...
"""
from __future__ import annotations

import functools
import logging
import os
from collections.abc import Callable
from typing import Any

import allure

_log = logging.getLogger("GreenCityLogger.step")


def step(title: str) -> Callable:
    """Decorator: record an Allure step *and* log it to the console in real time.

    Args:
        title: Human-readable step name, forwarded verbatim to ``@allure.step``.

    Returns:
        A decorator that wraps the target function with Allure reporting and
        structured console logging.
    """
    def decorator(fn: Callable) -> Callable:
        allure_wrapped = allure.step(title)(fn)

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            worker = os.environ.get("PYTEST_XDIST_WORKER", "main")
            _log.info(">> [%s] STEP: %s", worker, title)
            try:
                result = allure_wrapped(*args, **kwargs)
                _log.info("<< [%s] DONE: %s", worker, title)
                return result
            except Exception:
                _log.exception("!! [%s] FAIL: %s", worker, title)
                raise

        return wrapper
    return decorator
