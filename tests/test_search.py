"""
These tests (test cases) cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage


# @pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser):  # phrase
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoSearchResult(browser)

    PHRASE = 'panda'

    # GIVEN the DuckDuckGo home page is displayed
    search_page.load()

    # WHEN the user searches for "panda"
    search_page.search(PHRASE)

    # THEN the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # AND the search result links pertain (relates) to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # AND the search result title contains "panda"
    assert PHRASE in result_page.title()


def test_random_article(browser):
    search_page = DuckDuckGoSearchPage(browser)

    PHRASE = 'panda'

    # GIVEN the DuckDuckGo home page is displayed
    search_page.load()

    # WHEN the user searches for "panda"
    search_page.search(PHRASE)

    search_page.click_on_search_result()
