"""This module contains the MutualFriendsPage class and its methods."""
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement
from components.abstract_pages_components.friend_users_components.mutual_friends_component \
    import MutualFriendsComponent


class MutualFriendsPage(BasePage):
    """Page that shows mutual friends page."""

    # Твої ідеальні локатори!
    locators = {
        "root": (By.XPATH, "(//*[contains(@class, 'mdc-tab')]/span[2]/span)[5]"),
        "page_title": (By.CSS_SELECTOR, ".friends-list.ng-star-inserted", MutualFriendsComponent),
        "all_friends_tab": (By.XPATH, "//span[contains(normalize-space(), 'All friends') "
                                      "or contains(normalize-space(), 'Всі друзі')]"),
        "mutual_friends_tab": (By.XPATH, "//span[contains(normalize-space(), 'Mutual friends') "
                                         "or contains(normalize-space(), 'Спільні друзі')]"),
        "friend_card_mutual_count": (By.XPATH, "//p[contains(normalize-space(), 'mutual friend') "
                                               "or contains(normalize-space(), 'спільн')][1]")
    }

    root: CustomWebElement
    page_title: MutualFriendsComponent
    all_friends_tab: CustomWebElement
    mutual_friends_tab: CustomWebElement
    friend_card_mutual_count: CustomWebElement

    def has_mutual_friends(self) -> bool:
        """Check if the mutual friends page is visible."""
        locator = self.locators["page_title"][:2]
        return self.is_visible(locator)

    def get_title_text(self) -> str:
        """Get page title."""
        return self.page_title.text

    # --- ОНОВЛЕНІ МЕТОДИ З JS-КЛІКАМИ ТА ОЧІКУВАННЯМИ ---

    def click_all_friends_tab(self):
        """Click on all friends tab."""
        # Чекаємо до 15 секунд, поки вкладка просто з'явиться на екрані
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.locators["all_friends_tab"]),
            message="All friends tab is not visible."
        )
        # Бронебійний клік через JavaScript
        element = self.driver.find_element(*self.locators["all_friends_tab"])
        self.driver.execute_script("arguments[0].click();", element)

    def click_mutual_friends_tab(self):
        """Click on mutual friends tab."""
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.locators["mutual_friends_tab"]),
            message="Mutual friends tab is not visible."
        )
        element = self.driver.find_element(*self.locators["mutual_friends_tab"])
        self.driver.execute_script("arguments[0].click();", element)

    def is_mutual_friends_tab_active(self) -> bool:
        """Check if the mutual friends tab is active."""
        parent_tab = self.mutual_friends_tab.find_element(
            By.XPATH,
            "./ancestor::*[contains(@class, 'mdc-tab') or @role='tab'][1]")
        return "active" in parent_tab.get_attribute("class") or parent_tab.get_attribute("aria-selected") == "true"

    def get_mutual_friends_count(self) -> str:
        """Return number of mutual friends from card."""
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.locators["friend_card_mutual_count"]),
            message="Mutual friends count in user card is not visible."
        )
        full_text = self.driver.find_element(*self.locators["friend_card_mutual_count"]).text

        # Витягуємо першу знайдену цифру з тексту
        match = re.search(r'\d+', full_text)
        return match.group(0) if match else "0"

    @property
    def friends_list_component(self) -> MutualFriendsComponent:
        """Return the component with mutual friends list."""
        return self.page_title