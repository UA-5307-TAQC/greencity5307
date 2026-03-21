# pylint: disable=not-callable, unused-argument
""" :module:: about_us
    :platform: Unix
    :synopsis: """

from behave import given, when, then

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.friends_abstract.friends_abstract_page import FriendsAbstractPage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.common_pages.main_page import MainPage
from pages.common_pages.places_page import PlacesPage
from pages.news_pages.eco_news_page import EcoNewsPage


@given("the user is logged in")
def user_logged_in(driver):
    """User log in given"""
    main_page = MainPage(driver)
    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given("the About Us page is opened")
def open_about_us_page(about_us_page):
    """Opening of About Us page"""
    page = about_us_page.open()
    assert about_us_page.is_page_opened()
    return page

@then("the About Us page header should be visible")
def verify_about_us_opened(about_us_page):
    """Verification of About Us page opened"""
    assert about_us_page.section_header_one.is_displayed()

@when('I click the first "Form Habit" button')
def click_first_form_habit(about_us_page):
    """Click form habit button one"""
    return about_us_page.click_section_button_form_habit_one()


@when('I click the second "Form Habit" button')
def click_second_form_habit(about_us_page):
    """Click form habit button two"""
    return about_us_page.click_section_button_form_habit_two()


@then("the My Habits page should be opened")
def verify_my_habits_opened(page_object):
    """Verification of My Habit page opened"""
    # page_object is returned from previous step
    assert isinstance(page_object, MyHabitPage)

@when('I click the "Find Eco Places" button')
def click_find_places(about_us_page):
    """Click find places button"""
    return about_us_page.click_vision_card_button(index=1)


@then("the Places page should be opened")
def verify_places_page(driver):
    """Verify Places page"""
    assert isinstance(PlacesPage(driver), PlacesPage)


@when('I click the "Find People" button')
def click_find_people(about_us_page):
    """Click find people button"""
    return about_us_page.click_vision_card_button(index=2)


@then("the Friends page should be opened")
def verify_friends_page(driver):
    """Verify friends page opened"""
    assert isinstance(FriendsAbstractPage(driver), FriendsAbstractPage)


@when('I click the "Get Inspired" button')
def click_get_inspired(about_us_page):
    """Click get inspired button"""
    return about_us_page.click_vision_card_button(index=3)

@when('I click the "Find Eco Places" button before sign in')
def click_places_no_auth(about_us_page):
    """Click places page without sing in"""
    return about_us_page.click_vision_card_button_without_sign_in(1)


@when('I click the "Find People" button before sign in')
def click_people_no_auth(about_us_page):
    """Click people page without sing in"""
    return about_us_page.click_vision_card_button_without_sign_in(2)


@when('I click the "Get Inspired" button before sign in')
def click_news_no_auth(about_us_page):
    """Click news button without sing in"""
    return about_us_page.click_vision_card_button_without_sign_in(3)


@then("the Sign In modal should be opened")
def verify_sign_in_modal(driver):
    """Verify sing in modal"""
    modal = SignInComponent(driver)
    assert modal.is_displayed()

@then("the Eco News page should be opened")
def verify_news_page(driver):
    """Verify news page opened"""
    assert isinstance(EcoNewsPage(driver), EcoNewsPage)

@then("I return to the About Us page")
def return_to_about_us(driver, about_us_page):
    """Return to About Page step"""
    driver.back()
    assert about_us_page.is_page_opened()
