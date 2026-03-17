"""Page object for the Places page."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.places_components.add_place_modal_component import AddPlaceModalComponent
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class PlacesPage(BasePage):
    """Page object for the Places page."""
    locators = {
        "add_place_button": (
            By.CSS_SELECTOR,
            ".secondary-global-button.m-btn.ng-star-inserted"
        ),
        "add_place_modal": (By.CSS_SELECTOR, ".ng-star-inserted > .form-container")
    }
    add_place_button: CustomWebElement
    add_place_modal: AddPlaceModalComponent

    @allure.step("Open modal form to add place")
    def open_add_place_modal(self) -> AddPlaceModalComponent:
        """Open add place modal component."""
        self.add_place_button.click()
        return AddPlaceModalComponent(self.add_place_modal)

    @allure.step("Open Saved Places page from Places page")
    def go_to_saved_places(self):
        """Open Saved Places page."""
        from pages.abstract_pages.saved_abstract.places_saved_page import PlacesSavedPage  # pylint: disable=import-outside-toplevel

        self.header.click_saved_link()
        self.get_wait().until(EC.url_contains("isBookmark=true"))

        saved_places_page = PlacesSavedPage(self.driver)
        saved_places_page.open_places_tab()

        self.get_wait().until(EC.url_contains("places"))
        self.get_wait().until(
            EC.visibility_of_element_located(saved_places_page.search_place_input_locator)
        )

        return saved_places_page

    @allure.step("Navigating to the About Us page from Places page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        from pages.common_pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        self.header.click_about_us_link()
        self.get_wait().until(EC.url_contains("about"))
        return AboutUsPage(self.driver)

    @allure.step("Checking if Places page is opened")
    def is_page_opened(self) -> bool:
        """Check if the Places page is opened."""
        return self.is_visible(self.locators["add_place_button"])

    @allure.step("Checking if Places page is loaded")
    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded."""
        self.get_wait().until(EC.visibility_of(self.add_place_button))
        return True
