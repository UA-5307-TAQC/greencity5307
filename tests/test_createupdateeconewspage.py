"""This module contains tests for creating eco news with valid data"""
import pytest
import allure

from pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
@pytest.mark.regression

class TestCreateUpdateEcoNewsPage: # pylint: disable=no-member
    """
        TC-101
        Title: Create eco news with valid data
        Author: Vitalina Kliuieva
        Priority: High
    """


    @allure.title("Test Validation: Create Eco News with Valid Data. Open Create Eco News page.")
    @allure.description(
        "This test verifies that a user can successfully open eco news page. ")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "vitalina.kliuieva")
    @allure.testcase("TC-101")
    @allure.step("Open Create Eco News page")
    def test_open_create_update_eco_news_page(self, driver):
        """Open Create Eco News page."""
        page = CreateUpdateEcoNewsPage(driver)

        assert page.is_page_opened(), "Create Eco News page is not opened"

    @allure.title("Test Validation: Create Eco News with Valid Data. Filling the form.")
    @allure.description(
        "This test verifies that a user can fill create eco news form with valid data.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "vitalina.kliuieva")
    @allure.testcase("TC-101")
    @allure.step("Fill in the form with valid data")
    def test_fill_in_form(self, driver):
        """Fill in the form with valid data."""
        page = CreateUpdateEcoNewsPage(driver)

        form = page.get_form()

        title = "Save the Planet"
        tags = ("Events", "News")
        source = "Green Blog"
        content = "Eco content " * 30
        image_path = "tests/data/test_image.jpg"

        form.fill_form(
            title=title,
            tags=tags,
            source=source,
            content=content,
            image_path=image_path
        )
        assert form is not None, "Form should not be None after filling in data"

    @allure.title("Test Validation: Create Eco News with Valid Data. Submission.")
    @allure.description(
        "This test verifies that a user can submit create eco news form with valid data. ")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "vitalina.kliuieva")
    @allure.testcase("TC-101")
    @allure.step("Submit the form")
    def test_submit_form(self, driver):
        """Submit the form."""
        page = CreateUpdateEcoNewsPage(driver)

        page.click_submit()
