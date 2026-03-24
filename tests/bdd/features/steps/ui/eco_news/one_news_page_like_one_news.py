"""Steps for one_news_page_like_one_news bdd test"""
import random

import allure
from behave import when, then
from selenium.webdriver.support.wait import WebDriverWait

from clients.eco_new_client import EcoNewClient
from clients.own_security_client import OwnSecurityClient
from data.config import Config
from pages.common_pages.main_page import MainPage
from utils.logger import logger


@when("the user navigates to the Eco News page")
def step_open_eco_news_page(context):
    """Navigate to the Eco News page"""
    main_page = MainPage(context.browser)
    context.news_page = main_page.go_to_eco_news()


@when("the user opens a random news article")
def step_open_random_news_article(context):
    """Open a random news article"""
    news_cards = context.news_page.news_cards

    assert len(news_cards) > 0, "There are no news cards on the news page"

    num = random.randint(0, len(news_cards) - 1)
    context.one_news_page = news_cards[num].navigate_to_one_news_page()


@then("the system checks that the user is not the author of the news")
def step_check_user_not_author(context):
    """Check via API if user is author and skip if true"""

    with allure.step("Get user id via API"):
        client = OwnSecurityClient(Config.BASE_USER_API_URL)
        response = client.sign_in(
            email=Config.USER_EMAIL,
            password=Config.USER_PASSWORD
        )
        assert response.status_code == 200

        context.user_id = response.json().get("userId")
        logger.info("User id: %s", context.user_id)

    with allure.step("Get news id from URL"):
        current_url = context.browser.current_url
        context.news_id = current_url.split("/")[-1]
        logger.info("News id: %s", context.news_id)

    with allure.step("Get author id via API"):
        news_client = EcoNewClient(Config.BASE_API_URL)
        news_response = news_client.find_eco_news_by_id(
            news_id=context.news_id
        )

        context.author_id = news_response.json().get("author").get("id")
        logger.info("Author id: %s", context.author_id)

    with allure.step("Compare user and author"):
        user_is_author = context.user_id == context.author_id
        logger.info("User is author: %s", user_is_author)

        if user_is_author:
            context.scenario.skip("User is author of the news")


@then("the user sees the current number of likes")
def step_get_initial_likes(context):
    """Get current likes count"""
    context.initial_likes = context.one_news_page.likes.get_likes_count()
    context.was_liked = context.one_news_page.likes.check_like_status()


@when("the user clicks the like button")
def step_click_like_button(context):
    """Click the like button"""
    context.one_news_page.likes.click_like_button()


@then("the like counter should update accordingly")
def step_wait_for_like_update(context):
    """Wait until likes count changes"""
    WebDriverWait(context.browser, 10).until(
        lambda driver: context.initial_likes
                       != context.one_news_page.likes.get_likes_count()
    )

    context.updated_likes = context.one_news_page.likes.get_likes_count()


@then("if the article was previously liked the counter decreases by 1")
def step_check_like_decreased(context):
    """Check decrease"""
    if context.was_liked:
        assert context.updated_likes == context.initial_likes - 1, (
            f"Expected {context.initial_likes - 1}, "
            f"got {context.updated_likes}"
        )


@then("if the article was not previously liked the counter increases by 1")
def step_check_like_increased(context):
    """Check increase"""
    if not context.was_liked:
        assert context.updated_likes == context.initial_likes + 1, (
            f"Expected {context.initial_likes + 1}, "
            f"got {context.updated_likes}"
        )
