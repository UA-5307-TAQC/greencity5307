"""This module provides a Singleton logger configuration."""

import logging
import os
import sys


class _WorkerFilter(logging.Filter):
    """Logging filter that injects the current xdist worker ID into every record.

    Using a Filter instead of embedding the worker_id in the format string at
    logger-creation time ensures that the correct worker is reported even if the
    singleton is somehow reused across different execution contexts.
    """

    def filter(self, record: logging.LogRecord) -> bool:
        record.worker_id = os.environ.get("PYTEST_XDIST_WORKER", "main")
        return True


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
            '%(asctime)s [%(worker_id)s] %(name)s %(levelname)s'
            ' - %(filename)s  - %(funcName)s'
            ' - %(message)s'
        )

        if not self.logger.handlers:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            console_handler.addFilter(_WorkerFilter())
            self.logger.addHandler(console_handler)

    def get_logger(self):
        """Returns the configured logger instance."""
        return self.logger

logger: logging.Logger = Logger().get_logger()
