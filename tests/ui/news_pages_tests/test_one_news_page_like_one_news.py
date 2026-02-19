"""Module for test like one news page like one news"""
import random

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.main_page import MainPage


@allure.title("Test like one news on one news page")
def test_one_news_page_like_one_news(driver: WebDriver):
    """Test like one news page like one news"""
    main_page = MainPage(driver)

    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    news_page = main_page.header.click_new_link()

    num = random.randint(0, len(news_page.news_cards) - 1)

    one_news_page = news_page.news_cards[num].navigate_to_one_news_page()

    initial_likes_count = one_news_page.likes.get_likes_count()
    was_liked = one_news_page.likes.check_like_status()

    one_news_page.likes.click_like_button()

    updated_likes_count = one_news_page.likes.get_likes_count()

    if was_liked:
        assert updated_likes_count == initial_likes_count - 1, "Кількість лайків мала зменшитися на 1"
    else:
        assert updated_likes_count == initial_likes_count + 1, "Кількість лайків мала збільшитися на 1"
