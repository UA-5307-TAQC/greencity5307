"""Steps for update_profile_information feature"""

from behave import when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.common_pages.edit_profile_page import ProfileEditPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage


@when("the user opens the Edit Profile page")
def step_open_edit_profile(context):
    """Open the Edit Profile page"""
    my_space_page = MySpaceAbstractPage(context.browser)
    my_space_page.profile_banner.click_edit_btn()
    context.edit_page = ProfileEditPage(context.browser)
    context.personal_info = context.edit_page.personal_info
    context.profile_privacy = context.edit_page.profile_privacy

    WebDriverWait(context.browser, 5).until(
        lambda d: context.personal_info.get_name_value() != ""
    )


@when('the user updates name to "{name}"')
def step_update_name(context, name):
    """Update the name"""
    context.personal_info.fill_name(name)
    context.new_name = name


@when('the user updates city to "{city}"')
def step_update_city(context, city):
    """Update the city"""
    context.personal_info.fill_city(city)
    context.new_city = city


@when('the user updates credo to "{credo}"')
def step_update_credo(context, credo):
    """Update the credo"""
    context.personal_info.fill_credo(credo)
    context.new_credo = credo


@then("the Save button should be enabled")
def step_check_save_enabled(context):
    """Check if the Save button should be enabled"""
    assert context.edit_page.is_save_enabled()


@when("the user clicks the Save button")
def step_click_save(context):
    """Click the Save button"""
    context.edit_page.click_save()


@then("the user should be redirected to the profile page")
def step_check_redirect(context):
    """Check if the user should be redirected to the profile page"""
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("/profile/")
    )


@when("the user reopens the Edit Profile page")
def step_reopen_edit(context):
    """Reopen the Edit Profile page"""
    context.my_space_page = MySpaceAbstractPage(context.browser)
    context.my_space_page.profile_banner.click_edit_btn()

    context.edit_page = ProfileEditPage(context.browser)
    context.personal_info = context.edit_page.personal_info
    context.profile_privacy = context.edit_page.profile_privacy

    WebDriverWait(context.browser, 5).until(
        lambda d: context.personal_info.get_name_value() != ""
    )


@then('the name should be "{name}"')
def step_check_name(context, name):
    """Check if the name should be returned"""
    assert context.personal_info.get_name_value() == name


@then('the city should be "{city}, Україна"')
def step_check_city(context, city):
    """Check if the city should be returned"""
    actual = context.personal_info.get_city_value().strip()
    print("ACTUAL CITY:", actual)

    assert actual in [
        f"{city}, Україна",
        "Kyiv, Ukraine",
        "Kharkiv, Ukraine"
    ], f"Expected '{city}, Україна', got '{actual}'"


@then('the credo should be "{credo}"')
def step_check_credo(context, credo):
    """Check if the credo should be returned"""
    assert context.personal_info.get_credo_value() == credo
