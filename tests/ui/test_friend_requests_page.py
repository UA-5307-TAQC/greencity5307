from pages.friend_requests_page import FriendRequestsPage


def test_friend_requests_page_smoke(driver):
    page = FriendRequestsPage(driver)

    # перевірка: сторінка існує
    assert page.get_title() != ""

    # перевірка: клік по вкладці не падає
    page.click_requests_tab()