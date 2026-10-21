import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage


@pytest.mark.parametrize("text, expected_count", [("apple", 2), ("banana", 1), ("kuku", 0)])
def test_search(page, text, expected_count):
    home_page = HomePage(page)
    home_page.open()
    home_page.search(text)
    expect(home_page.product_names).to_have_count(expected_count)
