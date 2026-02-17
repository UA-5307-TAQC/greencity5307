"""This module contains tests for creating eco news with valid data"""
import tempfile
import pytest
import allure
from PIL import Image

from components.common_components.auth_components.singin_component import SignInComponent
from pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
from pages.eco_news_page import EcoNewsPage
from pages.main_page import MainPage
from data.config import Config



@pytest.mark.regression

 # pylint: disable=no-member
@allure.title("Test Validation: Create Eco News with Valid Data. Open Create Eco News page.")
@allure.description("This test verifies that a user can successfully open eco news page. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-101")
@allure.step("Open Create Eco News page")

def test_open_create_update_eco_news_page(driver):
    """
        TC-101
        Title: Create eco news with valid data
        Author: Vitalina Kliuieva
        Priority: High
    """

    main_page = MainPage(driver)

    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(driver, Config.USER_EMAIL, Config.USER_PASSWORD)

    news_page: EcoNewsPage = main_page.go_to_eco_news()
    create_news_page: CreateUpdateEcoNewsPage = news_page.click_create_button()

    assert create_news_page.is_page_opened(), "Create Eco News page is not opened"

    form = create_news_page.get_form()

    title = "Save the Planet"
    tags = ("Events", "News")
    source = "https://saving-planet.org/"
    content = "Eco content " * 30
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        temp_file_path = tmp.name
        # Generate a tiny 1x1 pixel image
        image = Image.new('RGB', (10, 10), color='red')
        image.save(temp_file_path)

    form.fill_form(
        title=title,
        tags=tags,
        source=source,
        content=content,
        #image_path=None
    )
    assert form is not None, "Form should not be None after filling in data"

    create_news_page.click_submit()
