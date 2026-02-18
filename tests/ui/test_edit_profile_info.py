"""Test update basic profile information."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data.config import Config
from pages.base_page import BasePage
from pages.profile_edit_page import ProfileEditPage


@allure.title("Update basic profile information")
@allure.description(
    "Verify user can update name, city and credo on Edit Profile page "
    "and changes are saved successfully."
)
@allure.severity(allure.severity_level.NORMAL)
def test_update_basic_profile_information(driver: WebDriver):
    """TC-EP-01"""

    base_page = BasePage(driver)

    # Sign in
    sign_in_component = base_page.header.click_sign_in_link()
    sign_in_component.sign_in(driver, Config.USER_EMAIL, Config.USER_PASSWORD)

    # Navigate to Edit Profile page
    driver.get(f"{Config.BASE_URL}/#/greenCity/profile/{Config.USER_ID}/edit")

    page = ProfileEditPage(driver)
    personal_info = page.get_personal_info_component()

    new_name = "Oleksandr"
    new_city = "Kyiv"
    new_credo = "I sort waste every day"

    # Step 1 - Update name
    personal_info.clear_name()
    personal_info.enter_name(new_name)
    assert personal_info.get_name_value() == new_name

    # Step 2 - Update city
    personal_info.clear_city()
    personal_info.enter_city(new_city)
    assert personal_info.get_city_value() == new_city

    # Step 3 - Update credo
    personal_info.clear_credo()
    personal_info.enter_credo(new_credo)
    assert personal_info.get_credo_value() == new_credo

    # Step 4 - Check Save button is enabled
    assert page.is_save_enabled(), "Save button should be active"

    # Step 5 - Click Save
    page.click_save()

    # Step 6 - Wait for success notification
    success_locator = (By.CLASS_NAME, "success-notification")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(success_locator)
    )

    # Step 7 - Refresh page
    driver.refresh()

    page = ProfileEditPage(driver)
    personal_info = page.get_personal_info_component()

    # Step 8-10 - Verify updated values
    assert personal_info.get_name_value() == new_name, "Name was not updated"
    assert personal_info.get_city_value() == new_city, "City was not updated"
    assert personal_info.get_credo_value() == new_credo, "Credo was not updated"
