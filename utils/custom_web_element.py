"""Custom WebElement"""
from typing import Any
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class CustomWebElement:
    """
    A wrapper for the standard WebElement that adds smart waits
    and nested element resolution.
    """
    def __init__(self, driver: WebDriver, element: WebElement):
        self.driver = driver
        self.root = element

    def __getattr__(self, name: str) -> Any:
        """
        Proxies all standard methods (e.g., .text, .send_keys, .is_displayed)
        to the original Selenium WebElement.
        """
        return getattr(self.root, name)

    def resolve_list(self, by: str, value: str) -> list[Any]:
        """
        Locates child elements within THIS specific element.
        """
        # self.root here is the currently located element
        elements = self.root.find_elements(by, value)

        # Returns a list of wrapped child elements
        return [CustomWebElement(self.driver, el) for el in elements]

    def wait_and_click(self, timeout: int = 10) -> None:
        """
        Waits until the element (self.root) becomes visible and clickable, then performs a click.
        """

        def _clickable_condition(_):
            try:
                # Directly checking the state of our element
                if self.root.is_displayed() and self.root.is_enabled():
                    return self.root
                return False

            except (NoSuchElementException, StaleElementReferenceException):
                # Allow the system to wait and retry
                return False

        # Wait loop until the element is ready for interaction
        ready_element = WebDriverWait(self.driver, timeout).until(
            _clickable_condition,
            message=f"Element was not clickable after {timeout} seconds"
        )
        ready_element.click()
