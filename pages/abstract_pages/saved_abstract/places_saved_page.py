"""Module contains PlacesSavedPage page object."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract
from utils.types import Locators


class PlacesSavedPage(SavedAbstract):
    """Page Object for Saved -> Places page."""

    title: Locators = (
        By.XPATH,
        "//p[contains(@class,'main-header')]"
    )

    places_tab_locator: Locators = (
        By.XPATH,
        "//button[normalize-space()='Places' or normalize-space()='Карта']"
    )

    search_place_input_locator: Locators = (
        By.XPATH,
        "//input[contains(@placeholder,'Searching for a place') "
        "or contains(@placeholder,'Пошук місця')]"
    )

    choose_location_input_locator: Locators = (
        By.XPATH,
        "//input[contains(@placeholder,'Choose location') "
        "or contains(@placeholder,'Оберіть місце')]"
    )

    saved_places_chip_locator: Locators = (
        By.XPATH,
        "//*[contains(normalize-space(),'Saved Places') "
        "or contains(normalize-space(),'Збереженні Місця') "
        "or contains(normalize-space(),'Збережені Місця')]"
    )

    left_panel_title_locator: Locators = (
        By.XPATH,
        "//*[contains(normalize-space(),'Popular eco places') "
        "or contains(normalize-space(),'Популярні еко-місця')]"
    )

    @allure.step("Checking if Saved Places page is opened")
    def is_page_opened(self) -> bool:
        """Check if Saved Places page is opened."""
        try:
            self.get_wait().until(EC.url_contains("places"))
            self.get_wait().until(EC.url_contains("isBookmark=true"))
            self.get_wait().until(
                EC.visibility_of_element_located(self.search_place_input_locator)
            )
            self.get_wait().until(
                EC.visibility_of_element_located(self.choose_location_input_locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Get Saved page title")
    def get_page_title_text(self) -> str:
        """Return Saved page title text."""
        return self.find(self.title).text

    @allure.step("Check if Places tab is active")
    def is_places_tab_active(self) -> bool:
        """Check whether Places tab is active."""
        element = self.find(self.places_tab_locator)
        classes = element.get_attribute("class") or ""
        aria_selected = (element.get_attribute("aria-selected") or "").lower()
        return "active" in classes or "selected" in classes or aria_selected == "true"

    @allure.step("Check if search input is visible")
    def is_search_input_visible(self) -> bool:
        """Check if search place input is visible."""
        return self.is_visible(self.search_place_input_locator)

    @allure.step("Check if location input is visible")
    def is_location_input_visible(self) -> bool:
        """Check if choose location input is visible."""
        return self.is_visible(self.choose_location_input_locator)

    @allure.step("Get left panel title")
    def get_left_panel_title(self) -> str:
        """Return left panel title text."""
        return self.find(self.left_panel_title_locator).text

    @allure.step("Open Places tab on Saved page")
    def open_places_tab(self):
        """Open Places tab on Saved page."""
        self.find(self.places_tab_locator).click()
