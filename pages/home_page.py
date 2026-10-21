class HomePage:
    def __init__(self, page):
        self.page = page
        self.account_menu = page.locator("#navbarAccount")
        self.logout_button = page.locator("#navbarLogoutButton")
        self.search_icon = page.locator("#searchQuery")
        self.search_input = page.locator("#searchQuery input")
        self.product_names = page.locator(".item-name")
        self.add_to_basket_buttons = page.get_by_role("button", name="Add to Basket")
        self.basket_count = page.locator("button[routerlink='/basket'] .fa-layers-counter")

    def open(self):
        self.page.goto("/#/")

    def search(self, text):
        self.search_icon.click()
        self.search_input.fill(text)
        self.search_input.press("Enter")
