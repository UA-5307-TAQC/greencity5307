"""Create/Update eco news components."""
import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class CreateUpdateEcoNewsTitleComponent(BaseComponent):
    """Component that contains title information."""
    locators = {
        "section_title" : (By.XPATH, "//*[@id='main-content']/div/div[1]/h2"),
        "section_description" : (By.XPATH, "//*[@id='main-content']/div/div[1]/div/p")
    }

    section_title_input: CustomWebElement
    section_description_input: CustomWebElement

    def get_section_title_and_description_value(self):
        """Get title value."""
        return self.section_title.text, self.section_description.text

class CreateUpdateEcoNewsPictureComponent(BaseComponent):
    """Component that contains picture upload."""
    locators = {
        "picture_browse": (By.XPATH,
                                    "/html/body/app-root/app-main/div/div[2]/app-greencity-main/" \
                                    "app-eco-news/div/app-create-edit-news/main/div/div[2]/form/" \
                                    "div[1]/div[4]/app-drag-and-drop/div[1]/div/div/input"),
        "cancel_button": (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                               "app-drag-and-drop/div[2]/div[2]/button[1]"),
        "submit_button": (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/form/div[1]/div[4]/" \
                               "app-drag-and-drop/div[2]/div[2]/button[2]"),

        "browsed_picture": (By.XPATH, "//*[@id='main-content']/div/div[2]/form/div[1]/" \
                                           "div[4]/app-drag-and-drop/div/div[1]/img")
    }

    picture_browse: CustomWebElement
    cancel_button: CustomWebElement
    submit_button: CustomWebElement
    browsed_picture: CustomWebElement

    @allure.step("Upload image in EcoNews form")
    def upload_image(self, image_path: str):
        """Upload image using the file input and click submit."""
        # Show hidden input if needed
        self.driver.execute_script(
            "arguments[0].style.display='block'; arguments[0].style.opacity=1;",
            self.picture_input
        )
        self.picture_input.send_keys(image_path)
        self.submit_button.wait_and_click()

class CreateUpdateEcoNewsTagsComponent(BaseComponent):
    """Component that contains tags choice information."""
    locators = {
        "tag_button" : (By.XPATH,
                        "//*[@id='main-content']/div/div[2]/form/"
                        "div[1]/div[2]/div/app-tags-select"),
        "selected_tag_button" : (By.XPATH, ".//button[contains(@class, 'global-tag-clicked')]")
    }

    tag_button: CustomWebElement
    selected_tag_button: CustomWebElement


    @allure.step("Select multiple tags")
    def select_tag(self, tag_name: str):
        """Select a tag by name."""
        uk_tags = ["новини","події","освіта","ініціативи", "реклама"]
        if tag_name in uk_tags:
            mapping = {
                "news": "новини",
                "events": "події",
                "education": "освіта",
                "initiatives": "ініціативи",
                "ads": "реклама"
            }
            tag_name = mapping.get(tag_name.lower(), tag_name)

        buttons = self.root.find_elements(By.TAG_NAME, "button")

        for button in buttons:
            if button.text.strip().lower() == tag_name.strip().lower():
                button.click()
                return

        raise ValueError(f"Tag '{tag_name}' not found.")

    @allure.step("Select multiple tags")
    def select_multiple_tags(self, *tags: str):
        """Select multiple tags by their names."""
        for tag in tags:
            self.select_tag(tag)

    def get_selected_tags(self) -> list[str]:
        """Return list of selected tag names."""
        elements = self.root.find_elements(
            By.XPATH,
            ".//button[contains(@class, 'global-tag-clicked')]"
        )
        return [el.text.strip() for el in elements]

class CreateUpdateEcoNewsFormComponent(BaseComponent):
    """Component that contains main form"""
    locators = {"title_input": (By.XPATH,
                                "//*[@id='main-content']/div/div[2]/"
                                "form/div[1]/div[1]/label/textarea"),
        "source_input": (By.XPATH,
                              "//*[@id='main-content']/div/div[2]/form/div[1]/div[3]/label/input"),
        "content_input": (By.XPATH,
                               "//*[@id='main-content']/div/div[2]/" \
                               "form/div[2]/quill-editor/div[2]/div[1]"),
        "tags_input": (By.XPATH,
                       "//*[@id='main-content']/div/div[2]/form/div[1]/div[2]/div/app-tags-select")
    }

    title_input: CustomWebElement
    source_input: CustomWebElement
    content_input: CustomWebElement
    tags_input: CreateUpdateEcoNewsTagsComponent

    def get_tags_input(self) -> CreateUpdateEcoNewsTagsComponent:
        """Get the form component."""
        element = self.driver.find_element(*self.locators["tags_input"])
        return CreateUpdateEcoNewsTagsComponent(element)

    def enter_title(self, title: str):
        """Enter title."""
        self.title_input.clear()
        self.title_input.send_keys(title)

    def get_title(self) -> str:
        """Get title."""
        return self.title_input.get_attribute("value")

    def enter_source(self, source: str):
        """Enter source."""
        self.source_input.clear()
        self.source_input.send_keys(source)

    def get_source(self) -> str:
        """Get source."""
        return self.source_input.get_attribute("value")

    def enter_content(self, content: str):
        """Enter content."""
        self.content_input.clear()
        self.content_input.send_keys(content)

    def get_content(self) -> str:
        """Get content."""
        return self.content_input.text.strip()

    @allure.step("Fill eco news form")
    # pylint: disable=too-many-positional-arguments
    def fill_form(self, title: str, tags: tuple, source: str, content: str):
        """Fill the entire form."""
        self.enter_title(title)
        self.get_tags_input().select_multiple_tags(*tags)
        self.enter_source(source)
        self.enter_content(content)
