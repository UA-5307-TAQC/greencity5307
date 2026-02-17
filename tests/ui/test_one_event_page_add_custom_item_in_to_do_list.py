"""test add custom item into do_list."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from pages.my_habit_page import MyHabitPage
from pages.one_habit_page import OneHabitPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_one_event_page_add_custom_item_in_to_do_list(driver: WebDriver):
    """test add custom item into do_list."""
    base_page = BasePage(driver)

    sign_in_component = base_page.header.click_sign_in_link()

    sign_in_component.sign_in()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.TAG_NAME, "app-auth-modal"))
    )

    # base_page = BasePage(driver)
    #
    # base_page.header.click_my_space()

    page = MyHabitPage(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_any_elements_located(page.habit_cards_list)
    )

    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()

    #prob top test useless
    one_habit_page = OneHabitPage(driver)

    one_habit_page.press_to_do_list_edit_button()

    new_item_text = "Eco Bag"
    one_habit_page.add_element_into_list(new_item_text)

    one_habit_page.save_element()

    items = one_habit_page.check_added_element()

    assert new_item_text  in items, "Текст не зберігся!"
