"""Module for test like one news page like one news"""
import random

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from clients.eco_new_client import EcoNewClient
from clients.own_security_client import OwnSecurityClient
from data.config import Config
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from utils.logger import logger


@allure.title("Test like one news on one news page")
def test_one_news_page_like_one_news(driver_with_login: WebDriver):
    """Test like one news page like one news"""

    with allure.step("Make API sign in request"):
        # make API login request with the same credentials as in driver_with_login fixture
        client = OwnSecurityClient(f"{Config.BASE_USER_API_URL}")
        response = client.sign_in(
            email=Config.USER_EMAIL,
            password=Config.USER_PASSWORD
        )

    with allure.step("Validate sign in status code and response time"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Get user id"):
        data = response.json()
        user_id = data.get("userId")

        logger.info("User id: %s", user_id)
        assert user_id is not None and user_id >= 0, "User ID is invalid or missing"

    # link to news page
    news_page = MyHabitPage(driver_with_login).header.click_new_link()

    with allure.step(
            "Link to One News Page by random news card form Eco News Page"):
        news_cards = news_page.news_cards
        assert len(news_cards) > 0, "There are no news cards on the news page"
        # get random number to get random news_card
        num = random.randint(0, len(news_cards) - 1)
        one_news_page = news_cards[num].navigate_to_one_news_page()

    with allure.step("Get news id"):
        one_news_page_url = driver_with_login.current_url
        news_id = one_news_page_url.split("/")[-1]
        logger.info("News id: %s", news_id)

    with allure.step("Get author id"):
        news_client = EcoNewClient(base_url=Config.BASE_API_URL)
        news_response = news_client.find_eco_news_by_id(news_id=news_id)
        author_id = news_response.json().get("author").get("id")

        logger.info("Author id: %s", author_id)
        assert author_id is not None and author_id >= 0, "Author ID is invalid or missing"

    with allure.step("Check if news author is current user"):
        user_is_author = user_id == author_id
        logger.info("User is author: %s", user_is_author)

        if user_is_author:
            allure.attach(
                "User is author, skipping test",
                name="Skip reason",
                attachment_type=allure.attachment_type.TEXT
            )
            pytest.skip("User is author of the news, so he can't like")

    with allure.step("Check if like works"):
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
