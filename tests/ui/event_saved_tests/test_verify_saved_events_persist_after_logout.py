import allure

from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.abstract_pages.saved_abstract.news_saved_page import NewsPage
from pages.abstract_pages.saved_abstract.saved_events_page import SavedEventsPage
from pages.common_pages.main_page import MainPage

from data.config import Config

EVENT_CARD_NAME = "Some Event"


@allure.title("Verify that saved events persist after the user logs out and logs back in")
def test_verify_saved_events_persist_after_logout(driver_with_login, precondition_if_event_saved):
    with allure.step("Step 1: Navigate to the GreenCity URL."):
        main_page = MySpaceAbstractPage(driver_with_login).header.click_logo()

        # Expected result: The Main page loads successfully.
        assert main_page.is_loaded()

        user_name_from_header = main_page.header.get_signed_in_user_name()
        assert user_name_from_header in [Config.USER_NAME, "Hlib", "Oleksandr"], \
            f"The expected user is not signed in. Found user: '{user_name_from_header}'"

    with allure.step("Step 2: Click on the 'Events' button in the header."):
        events_page = main_page.header.click_event_link()

        # Expected result: The "Events" page loads successfully.
        assert events_page.is_loaded(), "Events page was not loaded successfully"

    with allure.step("Step 3: Click the 'Save' (bookmark) icon on the target event card."):
        target_event_card = events_page.get_event_card_by_name(EVENT_CARD_NAME)
        target_event_card.click_save_event()

        # The "Save" icon turns green (indicating the event is saved)
        assert target_event_card.is_saved()

    with allure.step("Step 4: Click the 'Saved' icon in the header."):
        events_page.header.click_saved_link()
        saved_eco_news_page = NewsPage(driver_with_login)

        # Expected result: The "Saved" page loads successfully with the "Eco-news" section open by default.
        assert saved_eco_news_page.is_loaded(), \
            "'Eco-news' tab on the 'Saved' page was not loaded."

    with allure.step("Step 5: Click on the 'Events' tab/section."):
        saved_eco_news_page.get_tabs_component().click_tab_by_name("Events")
        saved_events_page = SavedEventsPage(driver_with_login)

        # Expected result:
        # The "Saved Events" section is displayed. The event card saved in Step 6 is present in the list.
        assert saved_events_page.is_loaded(), \
            "'Events' tab on the 'Saved' page was not loaded."

        assert saved_events_page.is_event_card_present(EVENT_CARD_NAME), \
            f"The target event card with name '{EVENT_CARD_NAME} was not found in the 'Saved Events' list."

    with allure.step("Step 6: Click on the User Profile icon (dropdown) in the header."):
        saved_events_page.header.click_user_menu()

        # Expected result: A dropdown menu opens containing the "Sign Out" option.
        assert saved_events_page.header.is_user_menu_present(), \
            f"A dropdown menu is absent after clicking the user profile icon in the header."

    with allure.step("Step 7: Click the 'Sign Out' button in the dropdown menu."):
        saved_events_page.header.click_user_menu_sign_out_link()

        # Expected result: The user is logged out successfully.
        # The application redirects user to the Main page.
        main_page = MainPage(driver_with_login)
        assert main_page.is_loaded(), "The Main page did not load"

    with allure.step("Step 8: Click the 'Sign In' button in the header."):
        sign_in_window = main_page.header.click_sign_in_link()

        # Expected result: The "Sign in" modal window appears.
        assert sign_in_window.is_displayed(), \
            "The sign in window did not appear after clicking the 'Sign In' button in the header."

    with allure.step("Step 9: Enter valid credentials and sign in to the account and click the 'Sign In' button ."):
        profile_page = sign_in_window.sign_in(
            email=Config.USER_EMAIL,
            password=Config.USER_PASSWORD
        )

        # Expected result: The user is successfully logged in. The Profile page loads successfully.
        assert profile_page.wait_page_loaded(), \
            f"The profile page did not load"

    with allure.step("Step 10: Click the 'Saved' icon in the header."):
        profile_page.header.click_saved_link()
        saved_eco_news_page = NewsPage(driver_with_login)

        # Expected result: The "Saved" page loads successfully with the "Eco-news" section open by default.
        assert saved_eco_news_page.is_loaded(), \
            "'Eco-news' tab on the 'Saved' page was not loaded."

    with allure.step("Step 11: Click on the 'Events' tab/section."):
        saved_eco_news_page.get_tabs_component().click_tab_by_name("Events")
        saved_events_page = SavedEventsPage(driver_with_login)

        # Expected result:
        # The "Saved Events" section is displayed. The event card saved in Step 6 is present in the list.
        assert saved_events_page.is_loaded(), \
            "'Events' tab on the 'Saved' page was not loaded."

        assert saved_events_page.is_event_card_present(EVENT_CARD_NAME), \
            f"The target event card with name '{EVENT_CARD_NAME} was not found."
