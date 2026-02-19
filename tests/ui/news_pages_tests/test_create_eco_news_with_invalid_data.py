"""This module contains tests for creating eco news with invalid data"""
import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
from pages.eco_news_page import EcoNewsPage
from pages.main_page import MainPage
from data.config import Config





 # pylint: disable=no-member
@allure.title("Test Validation: Create Eco News with Invalid Data. Open Create Eco News page.")
@allure.description("This test verifies that a user "
                    "cannot successfully create eco new, because of invalid data. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-102")
@allure.step("Open Create Eco News page")
def test_create_eco_news_with_invalid_data(driver):
    """
        TC-101
        Title: Create eco news with invalid data
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

    title = ""
    tags = ("Invalid", "Invalid")
    source = "invalid-url"
    content = "Eco content"



    form.fill_form(
        title=title,
        tags=tags,
        source=source,
        content=content
    )

    assert form.get_title() == title
    assert form.get_source() == source
    assert form.get_content() == content

    create_news_page.click_submit()
    assert create_news_page.is_page_opened(), "Form not submitted successfully with invalid data"
