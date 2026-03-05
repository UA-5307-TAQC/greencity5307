"""This module provides a Singleton logger configuration with Allure step mirroring."""

import logging
import sys

from allure_commons import plugin_manager
from allure_commons._hooks import hookimpl


class _AllureStepLogger:
    """
    Allure lifecycle listener that mirrors every step start to the standard
    Python logger so that CI/CD logs show real-time progress without needing
    to open the Allure HTML report.

    Methods are decorated with ``@hookimpl`` so that pluggy correctly routes
    Allure lifecycle events to this plugin.
    """

    name = "GreenCityAllureStepLogger"

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    # -----------------------------------------------------------------
    # Allure plugin interface (AllureUserHooks)
    # -----------------------------------------------------------------

    @hookimpl
    def start_step(self, uuid, title, params):  # pylint: disable=unused-argument
        """Log the step title when an Allure step begins.

        ``uuid`` matches the Allure hookspec signature and cannot be renamed.
        """
        self._logger.info("[ALLURE STEP] %s", title)

    @hookimpl
    def stop_step(self, uuid, exc_type, exc_val, exc_tb):  # pylint: disable=unused-argument
        """Log a failure message when a step ends with an exception.

        ``uuid`` matches the Allure hookspec signature and cannot be renamed.
        """
        if exc_type is not None:
            self._logger.warning("[ALLURE STEP FAILED] %s: %s", exc_type.__name__, exc_val)


def _register_step_listener(listener: _AllureStepLogger) -> None:
    """
    Register the listener with Allure's plugin manager, guarding against
    duplicate registration (important when the module is reloaded in tests).
    """
    if not plugin_manager.is_registered(listener):
        plugin_manager.register(listener)


class Logger:
    """Singleton class for logger configuration."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._configure_logger()
        return cls._instance

    def _configure_logger(self):
        """Configures the logger format, level and handler."""
        # pylint: disable=attribute-defined-outside-init
        self.logger = logging.getLogger('GreenCityLogger')

        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s'
            ' - %(filename)s  - %(funcName)s'
            ' - %(message)s'
        )

        if not self.logger.handlers:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        # Register the Allure step listener so that every @allure.step execution
        # is also written to the console handler above.
        _register_step_listener(_AllureStepLogger(self.logger))

    def get_logger(self):
        """Returns the configured logger instance."""
        return self.logger

logger: logging.Logger = Logger().get_logger()
