"""This module contains the AboutUsPage class, which represents the about_us page of a website."""

from selenium.webdriver.common.by import By

from components.vision_card_component import VisionCardComponent
from pages.base_page import BasePage
from pages.eco_news_page import EcoNewsPage
from pages.friends_abstract_page import FriendsAbstractPage
from pages.places_page import PlacesPage


class AboutUsPage(BasePage):
    """Page object for the about_us page."""

    locators = {
        "section_header_one": (By.XPATH, "//*[@id='main-content']/div[1]/div/h2"),
        "section_description_one": (By.XPATH, "//*[@id='main-content']/div[1]/div/p"),
        "section_button_form_habit_one": (By.CSS_SELECTOR,
            "#main-content > div.about-section.section > div > button"),

        "section_header_two": (By.XPATH, "//*[@id='main-content']/div[2]/div/div/h2"),
        "section_description_two": (By.XPATH, "//*[@id='main-content']/div[2]/div/div/p"),
        "section_button_form_habit_two": (By.XPATH,
                                                   "//*[@id='main-content']/div[2]/div/div/button"),

        "vision_section_header": (By.XPATH, "//*[@id='main-content']/div[3]/div/h2"),

        "vision_cards": (By.CSS_SELECTOR, "app-vision-card.vision-card")
    }



    def get_vision_cards(self) -> list[VisionCardComponent]:
        """Return list of VisionCardComponent objects."""
        elements = self.driver.find_elements(*self.locators["vision_cards"])
        return [
            VisionCardComponent(self.driver, element)
            for element in elements
        ]

    def click_vision_card_button(self, index: int):
        """Click the button on the vision card based on the provided index."""
        cards = self.get_vision_cards()

        if index < 1 or index > len(cards):
            raise ValueError(f"Index must be between 1 and {len(cards)}.")

        cards[index - 1].click_button()

        match index:
            case 1:
                return PlacesPage(self.driver)
            case 2:
                return FriendsAbstractPage(self.driver)
            case 3:
                return EcoNewsPage(self.driver)
            case 4:
                return FriendsAbstractPage(self.driver)

    def get_vision_cards_count(self) -> int:
        """Gets the number of vision cards present in the section."""
        return len(self.get_vision_cards())


    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded by verifying the presence of the vision cards."""
        return len(self.get_vision_cards()) > 0

    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.section_header_one.is_displayed()
