"""This module provides a Singleton logger configuration."""

import logging
import os
import sys
import threading


class _WorkerAwareFormatter(logging.Formatter):
    """Formatter that injects the pytest-xdist worker ID and OS thread ID
    into every log record so parallel runs are trivially distinguishable."""

    def format(self, record: logging.LogRecord) -> str:
        record.worker_id = os.environ.get("PYTEST_XDIST_WORKER", "main")
        record.thread_id = threading.get_ident()
        return super().format(record)


class Logger:
    """Thread-safe Singleton class for logger configuration."""
    _instance: "Logger | None" = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls) -> "Logger":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._configure_logger()
                    cls._instance = instance
        return cls._instance

    def _configure_logger(self) -> None:
        """Configures the logger format, level and handler."""
        # pylint: disable=attribute-defined-outside-init
        self.logger = logging.getLogger('GreenCityLogger')

        self.logger.setLevel(logging.DEBUG)

        formatter = _WorkerAwareFormatter(
            '%(asctime)s [%(worker_id)s/tid=%(thread_id)s] %(name)s %(levelname)s'
            ' - %(filename)s::%(funcName)s - %(message)s'
        )

        if not self.logger.handlers:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        """Returns the configured logger instance."""
        return self.logger


logger: logging.Logger = Logger().get_logger()
