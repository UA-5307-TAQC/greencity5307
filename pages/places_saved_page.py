"""Module contains PlacesSavedPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators


class PlacesSavedPage(BasePage):
    """Page Object for Map -> Saved Places (PlacesSaved)."""

    saved_places_chip_locator: Locators = (
        By.XPATH, 
        "//*[contains(.,'Збережені місця') or contains(.,'Saved places')]"
        )

    search_place_input_locator: Locators = (
        By.CSS_SELECTOR, 
        "input[placeholder*='Пошук місця'], input[placeholder*='Search place']"
        )
    choose_place_input_locator: Locators = (
        By.XPATH, 
        "//input[contains(@placeholder,'Оберіть місце') or contains(@placeholder,'Choose place')]"
        )

    add_place_btn_locator: Locators = (
        By.XPATH, 
        "//button[contains(.,'Додати місце') or contains(.,'Add place')]"
        )

    left_panel_title_locator: Locators = (
        By.XPATH, 
        "//*[contains(.,'Популярні еко-місця') or contains(.,'Popular eco-places')]"
        )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_saved_places_filter(self):
        """Click 'Saved places' filter chip/tab."""
        self.driver.find_element(*self.saved_places_chip_locator).click()

    def is_saved_places_filter_active(self) -> bool:
        """Check that Saved places filter is active (basic class/aria check)."""
        el = self.driver.find_element(*self.saved_places_chip_locator)
        cls = el.get_attribute("class") or ""
        aria = (el.get_attribute("aria-selected") or "").lower()
        return "active" in cls or "selected" in cls or aria == "true"

    def enter_search_place(self, text: str):
        """Type into 'Search place' input."""
        inp = self.driver.find_element(*self.search_place_input_locator)
        inp.clear()
        inp.send_keys(text)

    def is_add_place_button_visible(self) -> bool:
        """Check Add place button is visible."""
        return self.driver.find_element(*self.add_place_btn_locator).is_displayed()

    def get_left_panel_title(self) -> str:
        """Return left panel title text."""
        return self.driver.find_element(*self.left_panel_title_locator).text
