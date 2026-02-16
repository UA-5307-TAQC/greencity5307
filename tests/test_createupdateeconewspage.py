"""This module contains test Create eco news with valid data"""
import pytest
from pages.create_update_eco_news_page import CreateUpdateEcoNewsPage


@pytest.mark.regression
def test_create_eco_news_with_valid_data(driver):
    """
    TC-101
    Title: Create eco news with valid data
    Author: Vitalina Kliuieva
    Priority: High
    """

    page = CreateUpdateEcoNewsPage(driver)

    assert page.is_page_opened(), "Create Eco News page is not opened"

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

    page.click_submit()
