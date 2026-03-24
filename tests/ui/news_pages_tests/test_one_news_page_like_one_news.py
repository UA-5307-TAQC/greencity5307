"""Module for test like one news page like one news"""
import random

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage


@allure.title("Test like one news on one news page")
def test_one_news_page_like_one_news(driver_with_login: WebDriver):
    """Test like one news page like one news"""

    # link to news page
    news_page = MyHabitPage(driver_with_login).header.click_new_link()
    # get random number to get random news_card
    news_cards = news_page.news_cards
    assert len(news_cards) > 0, "There are no news cards on the news page"
    num = random.randint(0, len(news_cards) - 1)
    one_news_page = news_cards[num].navigate_to_one_news_page(
        driver_with_login)
    # get count of likes
    likes_count = one_news_page.likes.get_likes_count()
    # Check if news are already liked
    liked = one_news_page.likes.check_like_status()
    # Click news like button
    one_news_page.likes.click_like_button()
    # wait likes count to update
    WebDriverWait(driver_with_login, 10).until(
        lambda driver: likes_count != one_news_page.likes.get_likes_count()
    )
    # Get updated count of likes
    updated_likes_count = one_news_page.likes.get_likes_count()
    # Check correct like count change
    if liked:
        assert updated_likes_count == likes_count - 1
    else:
        assert updated_likes_count == likes_count + 1
