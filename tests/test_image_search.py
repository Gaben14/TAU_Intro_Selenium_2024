"""
These tests (test cases) cover DuckDuckGo image searches.
"""
import requests
from selenium.webdriver.common.by import By

from pages.result import DuckDuckGoSearchResult
from pages.image_search import DuckDuckGoImageSearch
from pages.search import DuckDuckGoSearchPage
from tests.conftest import browser, get_url


class TestImageSearch:
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully - HTTP 200
    2. Find the search-bar. Enter the phrase.
    3. Click on the 'Images' tab - Assert if Images tab is active
    4. Change the value inside "All sizes" to "Medium" - Assert if value has been changed to Medium
    5. Create a list which contains all the color options from the "All colors" dropdown
        5.1 Assert if the color has been changed.
    6. Change the type under the "All types" dropdown to "Animated GIF"
        6.1 Assert if the change has been successful
    7. Change the "All Licenses" to "Free to Share and Use" - Assert if there are any images after this change.
    """

    # Class Variables
    PHRASE = "panda"

    # Temporarily moving the locators here
    IMAGES_TAB = (By.CSS_SELECTOR, 'a[data-testid="tab-label-images"]')
    IMAGE_SIZE_DROPDOWN = (By.CLASS_NAME, 'dropdown--size')
    IMAGE_SIZE_MEDIUM = (By.CSS_SELECTOR, 'a[data-value="Medium"]')
    ALL_COLORS_DROPDOWN = (By.CLASS_NAME, 'dropdown--color')
    BLACK_AND_WHITE = (By.CSS_SELECTOR, 'a[data-value="Monochrome"]')
    ALL_TYPES = (By.CLASS_NAME, 'dropdown--type')
    ANIMATED_GIF = (By.CSS_SELECTOR, 'a[data-value="gif"]')

    def test_images_tab(self, browser, get_url):
        """
        response = requests.get()
        # Assert if the page can be pinged successfully - HTTP 200
        # TODO: If the status code is not 200, the test should not open the browser!
        assert response.status_code == 200
        # TODO: After the response code, wait until an item on the page has loaded
        """
        image_search_page = DuckDuckGoImageSearch(browser, get_url)
        image_search_page.load()
        # Find the search-bar. Enter the phrase.
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(self.IMAGES_TAB)

        # Assert that the images tab has been selected. - check if the <a> tag has the is-active class
        assert 'is-active' in image_search_page.get_html_css_class_list(self.IMAGES_TAB)

    def test_change_image_size(self, browser, get_url):
        # Change the Image Size

        image_search_page = DuckDuckGoImageSearch(browser, get_url)
        image_search_page.load()

        # Search for phrase
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(self.IMAGES_TAB)

        image_search_page.change_image_size()
        image_size_medium_cls_list = image_search_page.get_html_css_class_list(self.IMAGE_SIZE_MEDIUM)

        # Assert that the 'is-selected' class can be found on the Image Size Medium Button
        assert 'is-selected' in image_size_medium_cls_list

    def test_change_color(self, browser, get_url):

        image_search_page = DuckDuckGoImageSearch(browser, get_url)
        image_search_page.load()

        # Search for phrase
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(self.IMAGES_TAB)

        # Click on the 'All Colors' dropdown.
        image_search_page.click_on_item(self.ALL_COLORS_DROPDOWN)

        # TODO: Change from "All Colors" to "Black and white" and validate if color has changed
        image_search_page.click_on_item(self.BLACK_AND_WHITE)
        black_and_white_cls_list = image_search_page.get_html_css_class_list(self.BLACK_AND_WHITE)
        assert 'is-selected' in black_and_white_cls_list

    def test_change_type(self, browser, get_url):
        # TODO: Change from "All Types" to "Animated GIF" and validate if All Types has changed
        image_search_page = DuckDuckGoImageSearch(browser, get_url)
        image_search_page.load()

        # Search for phrase
        image_search_page.search(self.PHRASE)
        # Click on the images tab.
        image_search_page.click_on_item(self.IMAGES_TAB)

        image_search_page.click_on_item(self.ALL_TYPES)

        image_search_page.click_on_item(self.ANIMATED_GIF)
        animated_gif_cls_list = image_search_page.get_html_css_class_list(self.ANIMATED_GIF)
        assert 'is-selected' in animated_gif_cls_list
