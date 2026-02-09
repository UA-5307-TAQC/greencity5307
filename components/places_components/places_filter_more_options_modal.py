"""Places filter more options modal"""
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent


class PlacesFilterMoreOptionsModalComponent(BaseComponent):
    """Places filter more options modal component class"""

    def __init__(self, root: WebElement):
        super().__init__(root)
