"""Component class for an event card element on a web page."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class EventCardComponent(BaseComponent):
    """Component class for an event card element on a web page."""

    save_flag_locator = (By.CSS_SELECTOR, ".event-flags")
    event_tags_locator = (By.CSS_SELECTOR, ".ul-eco-buttons .text")

    event_date_locator = (By.CSS_SELECTOR, ".date")
    event_time_locator = (By.CSS_SELECTOR, ".time")
    event_place_locator = (By.CSS_SELECTOR, "span.place + p")
    event_status_locator = (By.CSS_SELECTOR, ".event-status")

    event_title_locator = (By.CSS_SELECTOR, ".event-name")

    more_button_locator = (By.CSS_SELECTOR, ".secondary-global-button")
    join_button_locator = (By.CSS_SELECTOR, ".primary-global-button")

    created_date_locator = (By.CSS_SELECTOR, ".additional-info .date p")
    author_locator = (By.CSS_SELECTOR, ".additional-info .author p")

    comments_count_locator = (By.CSS_SELECTOR, ".additional-info .frame p")

    like_button_locator = (By.CSS_SELECTOR, ".additional-info .like")
    like_count_locator = (By.CSS_SELECTOR, ".additional-info .like span")

    dislike_button_locator = (By.CSS_SELECTOR, ".additional-info .dislike")
    dislike_count_locator = (By.CSS_SELECTOR, ".additional-info .dislike span")

    def more(self):
        """Click the 'More' button on the event card."""
        self.root.find_element(*self.more_button_locator).click()
        from pages.one_event_page import OneEventPage  # pylint: disable=import-outside-toplevel
        return OneEventPage(self.root.parent)

    def join_event(self):
        """Click the 'Join' button on the event card."""
        join_button_element = self.root.find_element(*self.join_button_locator)
        if "Cancel" not in join_button_element.text:
            join_button_element.click()

    def cancel_request(self):
        """Click the button to cancel the join request if it's currently joined."""
        join_button_element = self.root.find_element(*self.join_button_locator)
        if "Cancel" in join_button_element.text:
            join_button_element.click()

    def save_event(self):
        """Click the button to save the event if it's not already saved."""
        self.root.find_element(*self.save_flag_locator).click()

    def is_saved(self) -> bool:
        """Check if the event is saved."""
        save_flag_element = self.root.find_element(*self.save_flag_locator)
        return "flag-active" in save_flag_element.get_attribute("class")

    @property
    def tags(self):
        """Return a list of tags associated with the event."""
        tag_elements = self.root.find_elements(*self.event_tags_locator)
        return [tag.text for tag in tag_elements]

    @property
    def date(self):
        """Return the date of the event."""
        return self.root.find_element(*self.event_date_locator).text

    @property
    def time(self):
        """Return the time of the event."""
        return self.root.find_element(*self.event_time_locator).text

    @property
    def place(self):
        """Return the place of the event."""
        return self.root.find_element(*self.event_place_locator).text

    @property
    def status(self):
        """Return the status of the event."""
        return self.root.find_element(*self.event_status_locator).text

    @property
    def title(self):
        """Return the title of the event."""
        return self.root.find_element(*self.event_title_locator).text

    @property
    def created_date(self):
        """Return the created date of the event."""
        return self.root.find_element(*self.created_date_locator).text

    @property
    def author(self):
        """Return the author of the event."""
        return self.root.find_element(*self.author_locator).text

    @property
    def comments_count(self):
        """Return the number of comments on the event."""
        return int(self.root.find_element(*self.comments_count_locator).text)

    @property
    def like_count(self):
        """Return the number of likes on the event."""
        return int(self.root.find_element(*self.like_count_locator).text)

    @property
    def dislike_count(self):
        """Return the number of dislikes on the event."""
        return int(self.root.find_element(*self.dislike_count_locator).text)

    def like(self):
        """Click the 'Like' button on the event card."""
        self.root.find_element(*self.like_button_locator).click()

    def dislike(self):
        """Click the 'Dislike' button on the event card."""
        self.root.find_element(*self.dislike_button_locator).click()
