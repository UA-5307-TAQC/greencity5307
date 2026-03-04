"""This module contains the SocialMediaLinksComponent class."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent

from utils.custom_web_element import CustomWebElement


class SocialMediaLinksComponent(BaseComponent):
    """Component class for social media links on a web page."""

    locators = {
        "share_plus_icon": (By.CSS_SELECTOR, "img[alt='Share']"),
        "twitter_icon": (By.CSS_SELECTOR, "img[alt='Share on Twitter']"),
        "linkedin_icon": (By.CSS_SELECTOR, "img[alt='Share on LinkedIn']"),
        "facebook_icon": (By.CSS_SELECTOR, "img[alt='Share on Facebook']")
    }

    share_plus_icon: CustomWebElement
    twitter_icon: CustomWebElement
    linkedin_icon: CustomWebElement
    facebook_icon: CustomWebElement

    def general_share_button(self):
        """Returns the Share icon button."""
        return self.share_plus_icon

    def twitter_button(self):
        """Returns the Twitter icon button."""
        return self.twitter_icon

    def linkedin_button(self):
        """Returns the LinkedIn icon button."""
        return self.linkedin_icon

    def facebook_button(self):
        """Returns the Facebook icon button."""
        return self.facebook_icon
