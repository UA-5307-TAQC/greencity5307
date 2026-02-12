"""Configuration module to load environment variables."""

import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).parent / ".env.example"
load_dotenv(dotenv_path=ENV_PATH)


class Config: # pylint: disable=too-few-public-methods
    """Configuration class to hold environment variables."""

    BASE_UI_URL = os.getenv("BASE_UI_URL")
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
    HEADLESS = os.getenv("HEADLESS", "True") != "False"
