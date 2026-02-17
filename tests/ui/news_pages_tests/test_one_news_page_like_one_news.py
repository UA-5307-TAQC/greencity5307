"""Module for test like one news page like one news"""
import random

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.common_components.auth_components.signin_modal_component import \
    SignInComponent
from data.config import Config
from pages.eco_news_page import EcoNewsPage
from pages.main_page import MainPage


@allure.title("Test like one news on one news page")
def test_one_news_page_like_one_news(driver: WebDriver):
    """Test like one news page like one news"""

    # open main page
    main_page = MainPage(driver)
    # sign in
    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)
    # wait to navigate to MyProfile page after sign in
    WebDriverWait(driver, 10).until(
        EC.url_changes(Config.BASE_UI_URL)
    )
    # link to news page
    news_page: EcoNewsPage = main_page.header.click_new_link()
    # get random number to get random news_card
    num = random.randint(0, len(news_page.news_cards) - 1)
    one_news_page = news_page.news_cards[num].navigate_to_one_news_page(driver)
    # get count of likes
    likes_count = one_news_page.likes.get_likes_count()
    # Check if news are already liked
    liked = one_news_page.likes.check_like_status()
    # Click news like button
    one_news_page.likes.click_like_button()
    # wait likes count to update
    WebDriverWait(driver, 10).until(
        lambda driver: likes_count != one_news_page.likes.get_likes_count()
    )
    # Get updated count of likes
    updated_likes_count = one_news_page.likes.get_likes_count()
    # Check correct like count change
    print(likes_count, updated_likes_count)
    if liked:
        assert updated_likes_count == likes_count - 1
    else:
        assert updated_likes_count == likes_count + 1
