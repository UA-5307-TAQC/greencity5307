"""Create/Update eco news components."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class CreateUpdateNewsTitleComponent(BaseComponent):
    """Component that contains title information."""
    section_title: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/h2")
    section_description: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/p")

def get_section_title_value(self):
    """Get title value."""
    title = self.root.find_element(*self.section_title).text
    description = self.root.find_element(*self.section_description).text
    return title, description

class CreateUpdateEcoNewsPictureComponent(BaseComponent):
    """Component that contains picture upload."""

    picture_browse: Locators = (By.XPATH,
                                "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                                "app-drag-and-drop/div[1]")
    cancel_button: Locators = (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                               "app-drag-and-drop/div[2]/div[2]/button[1]")
    submit_button: Locators = (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                               "app-drag-and-drop/div[2]/div[2]/button[2]")

    browsed_picture: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/" \
                                           "div[4]/app-drag-and-drop/div/div[1]/img")

    file_input: Locators = (By.XPATH, ".//input[@type='file']")

    def upload_image(self, image_path: str):
        """Upload image."""
        self.root.find_element(*self.file_input).send_keys(image_path)
        self.root.find_element(*self.submit_button).click()

class CreateUpdateEcoNewsTagsComponent(BaseComponent):
    """Component that contains tags choice information."""

    tag_button = ".//button[contains(text(),'{}')]"

    def select_tag(self, tag_name: str):
        """Select tag name."""
        locator = (By.XPATH, self.tag_button.format(tag_name))
        self.root.find_element(*locator).click()

    def select_multiple_tags(self, *tags):
        """Select multiple tags."""
        for tag in tags:
            self.select_tag(tag)


class CreateUpdateEcoNewsFormComponent(BaseComponent):
    """Component that contains main form"""
    title_input: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[1]")
    source_input: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/div[3]")
    content_input: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[2]")

    def __init__(self, root: WebElement):
        """Initialize the component."""
        super().__init__(root)
        self.tags_input = CreateUpdateEcoNewsTagsComponent(root)
        self.picture_input = CreateUpdateEcoNewsPictureComponent(root)

    def enter_title(self, title: str):
        """Enter title."""
        self.root.find_element(*self.title_input).send_keys(title)

    def enter_source(self, source: str):
        """Enter source."""
        self.root.find_element(*self.source_input).send_keys(source)

    def enter_content(self, content: str):
        """Enter content."""
        self.root.find_element(*self.content_input).send_keys(content)

    # pylint: disable=too-many-positional-arguments
    def fill_form(self, title: str, tags: tuple, source: str, content: str, image_path: str):
        """Fill form"""
        self.enter_title(title)
        self.tags_input.select_multiple_tags(*tags)
        self.enter_source(source)
        self.picture_input.upload_image(image_path)
        self.enter_content(content)
