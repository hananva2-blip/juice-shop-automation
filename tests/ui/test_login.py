from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_login_success(page, user):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["email"], user["password"])

    home_page = HomePage(page)
    home_page.account_menu.click()
    expect(home_page.logout_button).to_be_visible()


def test_login_wrong_password(page, user):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["email"], "wrong-password")
    expect(login_page.error).to_have_text("Invalid email or password.")
