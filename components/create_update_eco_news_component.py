"""Create/Update eco news components."""
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent
from components.header_component import HeaderComponent
from utils.types import Locators


class CreateUpdateEcoNewsTitleComponent(BaseComponent):
    """Component that contains title information."""
    section_title: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/h2")
    section_description: Locators = (By.XPATH, "//*[@id='main-content']/div/div[1]/div/p")

    def get_section_title_and_description_value(self):
        """Get title value."""
        title = self.root.find_element(*self.section_title).text
        description = self.root.find_element(*self.section_description).text
        return title, description

class CreateUpdateEcoNewsPictureComponent(BaseComponent):
    """Component that contains picture upload."""
    Locators = Tuple[str, str]
    picture_browse: Locators = (By.XPATH,
                                "/html/body/app-root/app-main/div/div[2]/app-greencity-main/" \
                                "app-eco-news/div/app-create-edit-news/main/div/div[2]/form/" \
                                "div[1]/div[4]/app-drag-and-drop/div[1]/div/div/input")
    cancel_button: Locators = (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                               "app-drag-and-drop/div[2]/div[2]/button[1]")
    submit_button: Locators = (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                               "app-drag-and-drop/div[2]/div[2]/button[2]")

    browsed_picture: Locators = (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/" \
                                           "div[4]/app-drag-and-drop/div/div[1]/img")


    def upload_image(self, image_path: str):
        """Upload image using the file input inside picture_browse."""

        file_input = WebDriverWait(self.root, 10).until(
            lambda r: r.find_element(*self.picture_browse))
        self.root.parent.execute_script("arguments[0].style.display='block'; "
                                        "arguments[0].style.opacity=1;",
                                        file_input)

        file_input.send_keys(image_path)

        submit_btn = WebDriverWait(self.root.parent, 20).until(
            lambda driver: driver.find_element(*self.submit_button)
            if driver.find_element(*self.submit_button).is_enabled() else False
        )
        submit_btn.click()

class CreateUpdateEcoNewsTagsComponent(BaseComponent):
    """Component that contains tags choice information."""

    tag_button = "//*[@id='main-content']/div/div[2]/form/div[1]/div[2]/div/app-tags-select"
    selected_tag_button = ".//button[contains(@class, 'global-tag-clicked')]"

    @allure.step("Select multiple tags")
    def select_tag(self, tag_name: str):
        """Select a tag by name."""
        container = self.root.find_element(By.XPATH, self.tag_button)
        header = HeaderComponent(self.root)
        if not header.is_language_english():
            if tag_name.lower() == "news":
                tag_name = "новини"
            elif tag_name.lower() == "events":
                tag_name = "події"
            elif tag_name.lower() == "education":
                tag_name = "освіта"
            elif tag_name.lower() == "initiatives":
                tag_name = "ініціативи"
            elif tag_name.lower() == "ads":
                tag_name = "реклама"


        for button in container.find_elements(By.TAG_NAME, "button"):
            if button.text.strip().lower() == tag_name.strip().lower():
                button.click()
                return

        raise ValueError(
            f"Tag with name '{tag_name}' not found in eco news tags component."
        )

    def select_multiple_tags(self, *tags):
        """Select multiple tags."""
        for tag in tags:
            self.select_tag(tag)

    def get_selected_tags(self) -> list[str]:
        """Return list of selected tag names."""
        elements = self.root.find_elements(By.XPATH, self.selected_tag_button)
        return [el.text for el in elements]


class CreateUpdateEcoNewsFormComponent(BaseComponent):
    """Component that contains main form"""
    Locators = Tuple[str, str]
    title_input: Locators = (By.XPATH,
                             "//*[@id='main-content']/div/div[2]/form/div[1]/div[1]/label/textarea")
    source_input: Locators = (By.XPATH,
                              "//*[@id='main-content']/div/div[2]/form/div[1]/div[3]/label/input")
    content_input: Locators = (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/" \
                               "form/div[2]/quill-editor/div[2]/div[1]")

    def __init__(self, root: WebElement):
        """Initialize the component."""
        super().__init__(root)
        self.tags_input = CreateUpdateEcoNewsTagsComponent(root)
        self.picture_input = CreateUpdateEcoNewsPictureComponent(root)

    def get_tags(self) -> list[str]:
        """Get selected tags."""
        return self.tags_input.get_selected_tags()

    def enter_title(self, title: str):
        """Enter title."""
        element = WebDriverWait(self.root, 10).until(
            EC.element_to_be_clickable(self.title_input)
        )
        element.clear()
        element.send_keys(title)

    def get_title(self) -> str:
        """Get title."""
        element = WebDriverWait(self.root, 10).until(
            EC.visibility_of_element_located(self.title_input)
        )
        return element.get_attribute("value")

    def enter_source(self, source: str):
        """Enter source."""
        element = WebDriverWait(self.root, 10).until(
            EC.element_to_be_clickable(self.source_input)
        )
        element.clear()
        element.send_keys(source)

    def get_source(self) -> str:
        """Get source."""
        element = WebDriverWait(self.root, 10).until(
            EC.visibility_of_element_located(self.source_input)
        )
        return element.get_attribute("value")

    def enter_content(self, content: str):
        """Enter content."""
        element = WebDriverWait(self.root, 10).until(
            EC.element_to_be_clickable(self.content_input)
        )
        element.clear()
        element.send_keys(content)

    def get_content(self) -> str:
        """Get content."""
        element = WebDriverWait(self.root, 10).until(
            EC.visibility_of_element_located(self.content_input)
        )
        return element.text.strip()

    @allure.step("Fill eco news form")
    # pylint: disable=too-many-positional-arguments
    def fill_form(self, title: str, tags: tuple, source: str, content: str):
        """Fill the entire form."""
        self.enter_title(title)
        self.tags_input.select_multiple_tags(*tags)
        self.enter_source(source)
        self.enter_content(content)
