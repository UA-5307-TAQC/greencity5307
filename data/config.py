"""Configuration module to load environment variables."""

import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)


class Config: # pylint: disable=too-few-public-methods
    """Configuration class to hold environment variables."""

    BASE_UI_URL = os.getenv("BASE_UI_URL")
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
    HEADLESS = os.getenv("HEADLESS", "true").lower() in ("1", "true", "True")
    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")
