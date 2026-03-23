"""Steps for one_news_page_like_one_news bdd test"""
import random

from behave import when, then
from selenium.webdriver.support.wait import WebDriverWait

from pages.common_pages.main_page import MainPage


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
    context.one_news_page = news_cards[num].navigate_to_one_news_page(
        context.browser)


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
