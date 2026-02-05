"""This module contains the HeaderComponent class,
 which represents the header section of a web page."""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class HeaderComponent(BaseComponent):
    """Component class for the header section of a web page."""
    new_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/news']")
    event_link_locator: Locators = (By.XPATH, ".//a[@href='#/greenCity/events']")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.new_link = self.root.find_element(*self.new_link_locator)
        self.event_link = self.root.find_element(*self.event_link_locator)

    def click_new_link(self) -> "EcoNewsPage":
        """Click the news link in the header and return an instance of the EcoNewsPage."""
        from pages.eco_news_page import EcoNewsPage  # pylint: disable=import-outside-toplevel
        self.new_link.click()
        return EcoNewsPage(self.root.parent)

    def click_event_link(self) -> "EventPage":
        """Click the event link in the header and return an instance of the EventPage."""
        from pages.event_page import EventPage  # pylint: disable=import-outside-toplevel
        self.event_link.click()
        return EventPage(self.root.parent)
