"""Module that contains UI test for verifying the event saving
and unsaving functionality, including authorization flow."""
import allure

from pages.common_pages.main_page import MainPage
from pages.abstract_pages.saved_abstract.news_saved_page import NewsPage
from pages.abstract_pages.saved_abstract.saved_events_page import SavedEventsPage

from components.common_components.auth_components.signin_modal_component \
    import SignInComponent

from data.config import Config


EVENT_CARD_NAME = "Some Event"


@allure.title("Verify Event Saving Functionality and Saved Items Management")
def test_verify_event_saving_functionality_management(driver, precondition_if_event_saved):
    """Test case that verifies flow of saving and unsaving an event.
    Includes unauthorized save attempt, authorization process,
    verifying the event in the 'Saved' tab, and its successful removal."""
    with allure.step("Step 1:"
                     "Navigate to the GreenCity URL."):
        main_page = MainPage(driver)

        # Expected result: The Home page loads successfully.
        assert main_page.is_page_opened(), "Main page was not loaded successfully."

    with allure.step("Step 2:"
                     "Click on the 'Events' button in the header."):
        events_page = main_page.header.click_event_link()

        # Expected result: The "Events" page loads successfully.
        assert events_page.is_loaded(), "Events page was not loaded successfully"

    with allure.step("Step 3:"
                     "Click the 'Save' (bookmark) icon in the upper-right corner "
                     "of the first event card."):
        target_event_card = events_page.get_event_card_by_name(EVENT_CARD_NAME)
        target_event_card.click_save_event()
        sign_in_window = SignInComponent(driver)

        # Expected result: The "Sign in" modal window appears.
        assert sign_in_window.is_displayed()

    with allure.step("Step 4:"
                     "Sign in into the account by valid credentials."):
        profile_page = sign_in_window.sign_in(
            email=Config.USER_EMAIL,
            password=Config.USER_PASSWORD
        )

        # Expected result: The user is successfully logged in and redirected to the Profile page.
        assert profile_page.wait_page_loaded(), \
            "My Habits page of profile user was not loaded."

    with allure.step("Step 5:"
                     "Navigate back to the 'Events' page."):
        events_page = profile_page.header.click_event_link()

        # Expected result: The "Events" page loads successfully.
        assert events_page.is_loaded(), "Events page was not loaded successfully"

    with allure.step("Step 6:"
                     "Click the 'Save' (bookmark) icon in the upper-right corner "
                     "of the first event card."):
        target_event_card = events_page.get_event_card_by_name(EVENT_CARD_NAME)
        target_event_card.click_save_event()

        # Expected result: The "Save" icon turns green (indicating the event is saved).
        assert target_event_card.is_saved()

    with allure.step("Step 7:"
                     "Click the 'Saved' icon in the header."):
        events_page.header.click_saved_link()
        saved_eco_news_page = NewsPage(driver)

        # Expected result: The "Saved" page loads successfully with the "Eco-news" section open by default.
        assert saved_eco_news_page.is_loaded(), \
            "'Eco-news' tab on the 'Saved' page was not loaded."

    with allure.step("Step 8:"
                     "Click on the 'Events' tab."):
        saved_eco_news_page.get_tabs_component().click_tab_by_name("Events")
        saved_events_page = SavedEventsPage(driver)

        # Expected result:
        # The "Saved Events" section is displayed. The event card saved in Step 6 is present in the list.
        assert saved_events_page.is_loaded(), \
            "'Events' tab on the 'Saved' page was not loaded."

        found_saved_card = saved_events_page.get_first_event_card()
        assert found_saved_card.title == EVENT_CARD_NAME, \
            f"Wrong card. Expected: {EVENT_CARD_NAME}, got: {found_saved_card.title}"

    with allure.step("Step 9:"
                     "Click the 'Save' (bookmark) icon in the upper-right corner of this event card."):
        found_saved_card.click_save_event()

        # Expected result: The "Save" icon turns white (indicating the event is removed from saved).
        assert not found_saved_card.is_saved(), "Card should be unsaved."

    with allure.step("Step 10:"
                     "Refresh the page."):
        saved_events_page.refresh_page()

        # Expected result: The event card disappears from the "Saved Events" page.
        assert saved_events_page.is_loaded(), \
            "'Events' tab on the 'Saved' page was not loaded."
        assert not saved_events_page.is_event_card_present(EVENT_CARD_NAME), \
            "Event card should be unsaved."
