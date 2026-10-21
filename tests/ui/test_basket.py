from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_add_product_to_basket(page, user):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["email"], user["password"])

    home_page = HomePage(page)
    home_page.add_to_basket_buttons.first.click()
    expect(home_page.basket_count).to_have_text("1")
