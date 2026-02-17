"""Base component class for web elements using Selenium WebDriver."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BaseComponent:
    """Base component class for web elements using Selenium WebDriver."""

    def __init__(self, root: WebElement):
        """Initialize BaseComponent object."""
        self.root = root
        self.driver = root.parent

        self.wait = WebDriverWait(self.driver, 10)

    def is_displayed(self) -> bool:
        """Check if the component is displayed."""
        return self.root.is_displayed()

    def is_enabled(self) -> bool:
        """Check if the component is enabled."""
        return self.root.is_enabled()

    def find(self, locator):
        """Find element by locator."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Click on the element specified by the locator."""
        self.find(locator).click()
    def get_text(self) -> str:
        """Get text from the element specified by the locator."""
        return self.root.text.strip()
