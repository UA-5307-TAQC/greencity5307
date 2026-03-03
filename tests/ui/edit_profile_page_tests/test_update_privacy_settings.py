"""Test update privacy settings"""
import time

import pytest
import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data.config import Config
from pages.base_page import BasePage
from pages.common_pages.edit_profile_page import ProfileEditPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage


@pytest.mark.parametrize(
    "value",
    [
        "Показувати мені та друзям",
        "Показувати всім",
        "Показувати тільки мені",
    ],
)
@allure.title("Update profile privacy settings")
@allure.description(
    "Verify user can update privacy settings on Edit Profile page "
    "and changes are saved successfully."
)
@allure.severity(allure.severity_level.NORMAL)
def test_update_privacy_settings(driver: WebDriver, value: str):
    """TC-EP-02"""

    base_page = BasePage(driver)

    with allure.step("User signs in with valid credentials"):
        sign_in_component = base_page.header.click_sign_in_link()
        sign_in_component.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("User opens Edit Profile page"):
        my_space_page = MySpaceAbstractPage(driver)
        my_space_page.profile_banner.click_edit_btn()

        page = ProfileEditPage(driver)
        profile_privacy_block = page.profile_privacy

    with allure.step("User updates privacy settings"):
        profile_privacy_block.set_show_location_value(value)
        profile_privacy_block.set_show_eco_places_value(value)
        profile_privacy_block.set_show_todo_value(value)

    with allure.step("User saves profile changes"):
        page.click_save()

        WebDriverWait(driver, 10).until(EC.url_contains("/profile/"))

    with allure.step("User reopens Edit Profile page to verify saved settings"):
        my_space_page = MySpaceAbstractPage(driver)
        my_space_page.profile_banner.click_edit_btn()

        page = ProfileEditPage(driver)
        time.sleep(0.3)
        profile_privacy_block = page.profile_privacy

    with allure.step("Verify updated settings is saved correctly"):
        assert profile_privacy_block.get_show_location_value() == value
        assert profile_privacy_block.get_show_eco_places_value() == value
        assert profile_privacy_block.get_show_todo_value() == value
