from pages.abstract_pages.friends_abstract.friend_requests_page import FriendRequestsPage

def test_friend_requests_tab_opens(driver_with_login):
    page = FriendRequestsPage(driver_with_login)
    page.click_requests_tab()
    assert "Друзі" in page.get_title()
