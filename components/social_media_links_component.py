"""This module contains the SocialMediaLinksComponent class."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class SocialMediaLinksComponent(BaseComponent):
    """Component class for social media links on a web page."""

    share_plus_icon_locator = (By.CSS_SELECTOR, "img[alt='Share']")
    twitter_icon_locator = (By.CSS_SELECTOR, "img[alt='Share on Twitter']")
    linkedin_icon_locator = (By.CSS_SELECTOR, "img[alt='Share on LinkedIn']")
    facebook_icon_locator = (By.CSS_SELECTOR, "img[alt='Share on Facebook']")

    def facebook_button(self):
        """Clicks on the Facebook icon."""
        return self.root.find_element(*self.facebook_icon_locator)

    def linkedin_button(self):
        """Clicks on the LinkedIn icon."""
        return self.root.find_element(*self.linkedin_icon_locator)

    def twitter_button(self):
        """Clicks on the Twitter icon."""
        return self.root.find_element(*self.twitter_icon_locator)

    def general_share_button(self):
        """Clicks on the general share (+) icon."""
        return self.root.find_element(*self.share_plus_icon_locator)
