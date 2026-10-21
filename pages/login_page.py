class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.login_button = page.locator("#loginButton")
        self.error = page.locator(".error")

    def open(self):
        self.page.goto("/#/login")

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
