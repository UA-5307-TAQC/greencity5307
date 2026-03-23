# pylint: disable=not-callable, unused-argument
""" :module:: about_us
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.friends_abstract.friends_abstract_page import FriendsAbstractPage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.common_pages.about_us_page import AboutUsPage
from pages.common_pages.main_page import MainPage
from pages.common_pages.places_page import PlacesPage
from pages.news_pages.eco_news_page import EcoNewsPage


@given('the user is logged in')
def user_logged_in(context):
    """Log in a user using valid credentials."""
    driver = context.browser

    main_page = MainPage(driver)
    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given('the About Us page is opened')
def open_about_us_page(context):
    """Open the About Us page and verify it is loaded."""
    driver = context.browser
    context.about_us_page = AboutUsPage(driver)
    assert context.about_us_page.is_page_opened()


@then("the About Us page header should be visible")
def verify_about_us_opened(context):
    """Verify that the main header on the About Us page is visible."""
    assert context.about_us_page.section_header_one.is_displayed()


@when('I click the first "Form Habit" button')
def click_first_form_habit(context):
    """Click the first 'Form Habit' button and store resulting page."""
    context.habit_page = context.about_us_page.click_section_button_form_habit_one()


@when('I click the second "Form Habit" button')
def click_second_form_habit(context):
    """Click the second 'Form Habit' button and store resulting page."""
    context.habit_page = context.about_us_page.click_section_button_form_habit_two()


@then("the My Habits page should be opened")
def verify_my_habits_opened(context):
    """Verify that the My Habits page is opened."""
    assert isinstance(context.habit_page, MyHabitPage)


@when('I click the "Find Eco Places" button')
def click_find_places(context):
    """Click the 'Find Eco Places' button."""
    context.places_page = context.about_us_page.click_vision_card_button(index=1)


@then("the Places page should be opened")
def verify_places_page(context):
    """Verify that the Places page is opened."""
    assert isinstance(context.places_page, PlacesPage)


@when('I click the "Find People" button')
def click_find_people(context):
    """Click the 'Find People' button."""
    context.friends_page = context.about_us_page.click_vision_card_button(index=2)


@then("the Friends page should be opened")
def verify_friends_page(context):
    """Verify that the Friends page is opened."""
    assert isinstance(context.friends_page, FriendsAbstractPage)


@when('I click the "Get Inspired" button')
def click_get_inspired(context):
    """Click the 'Get Inspired' button."""
    context.news_page = context.about_us_page.click_vision_card_button(index=3)


@then("the Eco News page should be opened")
def verify_news_page(context):
    """Verify that the Eco News page is opened."""
    assert isinstance(context.news_page, EcoNewsPage)


@when('I click the "Find Eco Places" button before sign in')
def click_places_no_auth(context):
    """Attempt to open Places page without authentication."""
    context.modal = context.about_us_page.click_vision_card_button_without_sign_in(1)


@when('I click the "Find People" button before sign in')
def click_people_no_auth(context):
    """Attempt to open Friends page without authentication."""
    context.modal = context.about_us_page.click_vision_card_button_without_sign_in(2)


@when('I click the "Get Inspired" button before sign in')
def click_news_no_auth(context):
    """Attempt to open News page without authentication."""
    context.modal = context.about_us_page.click_vision_card_button_without_sign_in(3)


@then("the Sign In modal should be opened")
def verify_sign_in_modal(context):
    """Verify that the Sign In modal is displayed."""
    modal = SignInComponent(context.browser)
    assert modal.is_displayed()


@then("I return to the About Us page")
def return_to_about_us(context):
    """Navigate back and verify the About Us page is opened again."""
    context.browser.back()
    assert context.about_us_page.is_page_opened()
