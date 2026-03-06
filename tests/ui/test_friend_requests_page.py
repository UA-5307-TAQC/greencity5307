from pages.friend_requests_page import FriendRequestsPage

def test_friend_requests_tab_opens(driver):
    page = FriendRequestsPage(driver)
    page.click_requests_tab()
    assert "Друзі" in page.get_title()