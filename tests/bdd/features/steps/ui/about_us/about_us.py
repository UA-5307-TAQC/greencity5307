# pylint: disable=not-callable, unused-argument
""" :module:: about_us
    :platform: Unix
    :synopsis: """
from behave import  when, then

from components.common_components.auth_components.signin_modal_component import SignInComponent


from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.common_pages.about_us_page import AboutUsPage

from pages.common_pages.main_page import MainPage
from pages.common_pages.places_page import PlacesPage
from pages.news_pages.eco_news_page import EcoNewsPage


@when("the user navigates to About Us page")
def step_go_to_about_us(context):
    """Navigation to About us page"""
    context.main_page = MainPage(context.browser)
    context.main_page.go_to_about_us()

@then('the About Us page should be opened')
def step_verify_about_us(context):
    """Verification of About Us opened"""
    context.about_page = AboutUsPage(context.browser)
    assert context.about_page.is_page_opened(), "About Us page is not opened"


@when('the user clicks the first "Form Habit" button')
def step_click_first_habit_button(context):
    """Click of first Form habit button"""
    context.about_page = AboutUsPage(context.browser)
    context.about_page.click_section_button_form_habit_one()


@then("the My Habit page should be opened")
def step_verify_my_habit_page_opened(context):
    """Verification My Habit page is opened """
    context.my_habit_page = MyHabitPage(context.browser)
    assert context.my_habit_page.wait_page_loaded(), "My Habit page is not opened"

@when("the user navigates back to About Us page")
def step_navigate_back_to_about_us_form_habit(context):
    """Navigation back to the About Us"""
    # Reuse MyHabitPage method to go back
    context.my_habit_page = MyHabitPage(context.browser)
    context.my_habit_page.go_to_about_us()

@when('the user clicks the second "Form Habit" button')
def step_click_second_habit_button(context):
    """Click second Form Habit button"""
    context.about_page = AboutUsPage(context.browser)
    context.about_page.click_section_button_form_habit_two()


@when('the user clicks Vision Card button {card_number:d} without signing in')
def step_click_vision_card_without_sign_in(context, card_number):
    """Click vision card button before sing in"""
    context.about_page = AboutUsPage(context.browser)
    if card_number == 3:
        context.about_page.click_vision_card_button_without_sign_in(card_number)
    else:
        context.about_page.click_vision_card_button_without_sign_in(card_number)


@then("the Sign In modal should be displayed")
def step_verify_sign_in_modal(context):
    """Verify sing in modal is opened"""
    context.sign_in_modal = SignInComponent(context.browser)
    assert context.sign_in_modal.is_displayed(), "Sign In modal is not opened"


@then("the user closes the Sign In modal")
def step_close_sign_in_modal(context):
    """Close sing in modal"""
    context.sign_in_modal = SignInComponent(context.browser)
    context.sign_in_modal.close_sign_in()


@then("the Main page should be opened")
def step_verify_main_page(context):
    """Verify Main page is opened"""
    context.main_page = MainPage(context.browser)
    assert context.main_page.is_page_opened(), "Main page is not opened after closing Sign In modal"

@then("the Eco News page should be opened")
def step_verify_news_page(context):
    """Verify Eco News page opened"""
    context.news_page = EcoNewsPage(context.browser)
    assert context.news_page.is_header_visible(), "Eco News page is not opened"


@when('the user clicks Vision Card button {card_number:d}')
def step_click_vision_card_signed_in(context, card_number):
    """Click vision card button after sing in"""
    if card_number == 1:
        context.about_page.click_vision_card_button(card_number)
    elif card_number in (2,4):
        context.about_page.click_vision_card_button(card_number)
    elif card_number == 3:
        context.about_page.click_vision_card_button(card_number)
    else:
        raise ValueError(f"Invalid Vision Card number: {card_number}")


@then("the Places page should be opened")
def step_verify_places_page(context):
    """Verify Places page is opened """
    context.places_page = PlacesPage(context.browser)
    assert context.places_page.is_page_loaded(), "Places page is not opened"


@then("the user navigates back to About Us page")
def step_navigate_back_to_about_us(context):
    """Navigate back to about us from singed in vision cards links"""
    if hasattr(context, "places_page"):
        context.about_page = context.places_page.go_to_about_us()
        del context.places_page
    elif hasattr(context, "friends_page"):
        context.about_page = context.friends_page.go_to_about_us()
        del context.friends_page
    elif hasattr(context, "news_page"):
        context.about_page = context.news_page.go_to_about_us()
        del context.news_page

    assert context.about_page.is_page_loaded(), "About Us page is not opened"
