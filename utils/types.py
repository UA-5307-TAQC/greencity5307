"""This module defines custom type aliases for commonly used data structures
in Selenium-based web automation."""

from selenium.webdriver.common.by import By

Locators = tuple[By, str]
