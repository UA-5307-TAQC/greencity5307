# pylint: disable=not-callable, unused-argument
"""
.. module:: Header navigation
    :platform: Unix
    :synopsis: """
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage

#
# @given('the user is signed in')
# def step_user_signed_in(context):
#     """Get driver from context and make login."""
#     main_page = MainPage(context.browser)
#
#     sign_in_form = main_page.header.click_sign_in_link()
#     sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()

@given('the user is on the "My Space" page')
def step_user_on_page(context):
    """Check if the user on the right page."""
    main_page = MainPage(context.browser)
    main_page.get_wait().until(
        EC.url_contains("profile"),
        message=f"URL did not change to profile. Current URL: {context.browser.current_url}"
    )
    my_space_page = MySpaceAbstractPage(context.browser)
    assert my_space_page.my_habits_tab.text in ("My habits", "Мої звички"), \
        "This is not my space page."


@given('the header navigation menu is visible')
def step_header_visible(context):
    """User clicks on the header navigation"""
    main_page = MainPage(context.browser)
    assert main_page.header.is_displayed(), "Header is not visible"


# WHEN (ДІЇ)

@when('the user clicks on "{link_name}" in the header navigation')
def step_click_header_link(context, link_name):
    """User clicks on the header navigation"""
    my_space_page = MySpaceAbstractPage(context.browser)

    if link_name == "Eco News":
        context.current_page = my_space_page.header.click_new_link()
    elif link_name == "Events":
        context.current_page = my_space_page.header.click_event_link()
    elif link_name == "Places":
        context.current_page = my_space_page.header.click_places_link()
    elif link_name == "About Us":
        context.current_page = my_space_page.header.click_about_us_link()
    else:
        raise ValueError(f"Unknown menu link: {link_name}")


@when('the user clicks the "GreenCity" logo in the header')
def step_click_logo(context):
    """User clicks the logo in the header"""
    my_space_page = MySpaceAbstractPage(context.browser)
    context.current_page = my_space_page.header.click_logo()


# THEN (ПЕРЕВІРКИ / ASSERTS)

@then('the user is redirected to the {page_name} page')
def step_redirect_page(context, page_name):
    """Redirect the user to the '{page_name}' page"""
    main_page = MainPage(context.browser)

    page_to_url_part = {
        "Eco News": "news",
        "Events": "events",
        "Map": "places",
        "About Us": "about",
        "Homepage": "greenCity",
        ("My Space", "Personal Account"): "profile",
        "UBS Courier": "ubs",
    }

    expected_part = page_to_url_part.get(page_name)

    if expected_part is None:
        raise ValueError(f"Unknown page name for redirection check: '{page_name}'")

    main_page.get_wait().until(
        EC.url_contains(expected_part),
        message=(f"Expected to be redirected to '{page_name}' page,"
                 f" but URL did not contain '{expected_part}'. "
                 f"Current URL: {context.browser.current_url}")
    )


@then('the URL contains "{url_part}"')
def step_url_contains(context, url_part):
    """Check if the URL contains "{url_part}"""
    assert url_part in context.browser.current_url, \
        f"Expected {url_part} in URL"


@then('the page title is "{expected_title}"')
def step_page_title(context, expected_title):
    """Check if the page title is equal to '{expected_title}'"""
    actual_text = context.current_page.main_header.text
    localized_titles = {
        "Eco News": ("Eco News", "Еко новини"),
        "Events": ("Events", "Події"),
        "Places": ("Places", "Карта"),
        "About Us": ("About Us", "Про Нас"),
    }
    acceptable_titles = localized_titles.get(expected_title, (expected_title,))
    assert actual_text in acceptable_titles, f"Actual header text: {actual_text}"


@then('the page content is loaded successfully')
def step_events_content_loaded(context):
    """Check if the page content is loaded successfully"""
    actual_text = context.current_page.main_header_locator.text
    assert actual_text in ("Events", "Події"), f"Actual text: {actual_text}"


@then('the map component is visible')
def step_map_visible(context):
    """Check if the map component is visible"""
    actual_text = context.current_page.add_place_button.text
    assert actual_text in ("Add place", "Додати місце"), f"Actual text: {actual_text}"


@then('the project information is displayed')
def step_about_us_info(context):
    """Check if the project information is displayed"""
    page = context.current_page

    page.get_wait().until(
        lambda d: page.section_header_one.text.strip() != "",
        message="About Us header text did not load in time"
    )
    actual_text = page.section_header_one.text.strip()
    assert actual_text in ("About Us", "Про Нас"), f"Actual text: {actual_text}"


@then('the user is redirected to the Homepage')
def step_redirect_homepage(context):
    """Redirect the user to the Homepage"""
    assert "greenCity" in context.browser.current_url, "URL does not contain 'greenCity'"


@then('the landing page content is displayed')
def step_landing_page_displayed(context):
    """Check if the landing page content is displayed"""
    actual_text = context.current_page.there_are.text
    assert actual_text in ("Нас і сьогодні ми", "There are of us and today we"), \
        f"Actual text: {actual_text}"
