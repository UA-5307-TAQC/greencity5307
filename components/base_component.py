"""Base component class for web elements using Selenium WebDriver."""
from utils.page_factory import Factory

class BaseComponent(Factory):
    """Base component class for web elements using Selenium WebDriver."""


    def is_displayed(self) -> bool:
        """Check if the component is displayed."""
        return self.root.is_displayed()

    def is_enabled(self) -> bool:
        """Check if the component is enabled."""
        return self.root.is_enabled()

    def get_text(self) -> str:
        """Get text from the element specified by the locator."""
        return self.root.text.strip()
