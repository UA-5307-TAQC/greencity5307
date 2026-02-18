import logging
import sys

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._configure_logger()
        return cls._instance

    def _configure_logger(self):
        self.logger = logging.getLogger('GreenCityLogger')

        self.logger.setLevel(logging.DEBUG)

        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not self.logger.handlers:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formater)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

logger = Logger().get_logger()
