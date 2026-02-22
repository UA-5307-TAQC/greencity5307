"""Test update basic profile information."""

import allure
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data.config import Config
from pages.base_page import BasePage
from pages.edit_profile_page import ProfileEditPage
from pages.my_space_abstract_page import MySpaceAbstractPage


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

    my_space_page = MySpaceAbstractPage(driver)
    my_space_page.profile_banner.click_edit_btn(driver)

    page = ProfileEditPage(driver)
    personal_info_block = page.personal_info

    # new_name = "Oleksandr"
    new_name = "test"
    # new_city = "Kyiv"
    new_city = "Kharkiv"
    new_credo = "I sort waste every day"

    # Step 2
    personal_info_block.fill_name(new_name)

    # Step 3
    personal_info_block.fill_city(new_city)

    # Step 4
    personal_info_block.fill_credo(new_credo)

    # Step 5
    assert page.is_save_enabled()

    # Step 6
    page.click_save()

    # Step 7
    WebDriverWait(driver, 10).until(EC.url_contains("/profile/"))

    # Step 8 - reopen edit page
    my_space_page = MySpaceAbstractPage(driver)
    my_space_page.profile_banner.click_edit_btn(driver)

    page = ProfileEditPage(driver)
    personal_info_block = page.personal_info

    WebDriverWait(driver, 5).until(
        lambda d: personal_info_block.get_name_value() != ""
    )

    # Step 9-10
    assert personal_info_block.get_name_value() == new_name
    assert personal_info_block.get_city_value() == new_city + ", Ukraine"
