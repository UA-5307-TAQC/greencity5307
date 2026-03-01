"""Component class for an event card element on a web page."""
from typing import List

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent

from utils.custom_web_element import CustomWebElement


class EventCardComponent(BaseComponent):
    """Component class for an event card element on a web page."""

    locators = {
        "save_flag": (By.CSS_SELECTOR, ".event-flags"),
        "event_tags": (By.CSS_SELECTOR, ".ul-eco-buttons .text"),

        "event_date": (By.CSS_SELECTOR, ".date"),
        "event_time": (By.CSS_SELECTOR, ".time"),
        "event_place": (By.CSS_SELECTOR, "span.place + p"),
        "event_status": (By.CSS_SELECTOR, ".event-status"),

        "event_title": (By.CSS_SELECTOR, ".event-name"),

        "more_button": (By.CSS_SELECTOR, ".secondary-global-button"),
        "join_button": (By.CSS_SELECTOR, ".primary-global-button"),

        "event_created_date": (By.CSS_SELECTOR, ".additional-info .date p"),
        "event_author": (By.CSS_SELECTOR, ".additional-info .author p"),

        "event_comments_count": (By.CSS_SELECTOR, ".additional-info .frame p"),

        "like_button": (By.CSS_SELECTOR, ".additional-info .like"),
        "event_like_count": (By.CSS_SELECTOR, ".additional-info .like span"),

        "dislike_button": (By.CSS_SELECTOR, ".additional-info .dislike"),
        "event_dislike_count": (By.CSS_SELECTOR, ".additional-info .dislike span")
    }

    save_flag: CustomWebElement
    event_tags: List[CustomWebElement]

    event_date: CustomWebElement
    event_time: CustomWebElement
    event_place: CustomWebElement
    event_status: CustomWebElement

    event_title: CustomWebElement

    more_button: CustomWebElement
    join_button: CustomWebElement

    event_created_date: CustomWebElement
    event_author: CustomWebElement

    event_comments_count: CustomWebElement

    like_button: CustomWebElement
    event_like_count: CustomWebElement

    dislike_button: CustomWebElement
    event_dislike_count: CustomWebElement

    def click_more(self):
        """Click the 'More' button on the event card."""
        self.more_button.wait_and_click()
        from pages.events_pages.one_event_page import OneEventPage  # pylint: disable=import-outside-toplevel
        return OneEventPage(self.root.parent)

    def click_join_event(self):
        """Click the 'Join' button on the event card."""
        if "Cancel" not in self.join_button.text:
            self.join_button.wait_and_click()

    def cancel_request(self):
        """Click the button to cancel the join request if it's currently joined."""
        if "Cancel" in self.join_button.text:
            self.join_button.wait_and_click()

    def click_save_event(self):
        """Click the button to save the event if it's not already saved."""
        self.save_flag.wait_and_click()

    def is_saved(self) -> bool:
        """Check if the event is saved."""
        return "flag-active" in self.save_flag.get_attribute("class")

    @property
    def tags(self):
        """Return a list of tags associated with the event."""
        return [tag.text for tag in self.event_tags]

    @property
    def date(self):
        """Return the date of the event."""
        return self.event_date.text

    @property
    def time(self):
        """Return the time of the event."""
        return self.event_time.text

    @property
    def place(self):
        """Return the place of the event."""
        return self.event_place.text

    @property
    def status(self):
        """Return the status of the event."""
        return self.event_status.text

    @property
    def title(self):
        """Return the title of the event."""
        return self.event_title.text

    @property
    def created_date(self):
        """Return the created date of the event."""
        return self.event_created_date.text

    @property
    def author(self):
        """Return the author of the event."""
        return self.event_author.text

    @property
    def comments_count(self):
        """Return the number of comments on the event."""
        return int(self.event_comments_count.text)

    @property
    def like_count(self):
        """Return the number of likes on the event."""
        return int(self.event_like_count.text)

    @property
    def dislike_count(self):
        """Return the number of dislikes on the event."""
        return int(self.event_dislike_count.text)

    def click_like(self):
        """Click the 'Like' button on the event card."""
        self.like_button.wait_and_click()

    def click_dislike(self):
        """Click the 'Dislike' button on the event card."""
        self.dislike_button.wait_and_click()
