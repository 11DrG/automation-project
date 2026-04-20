from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.remove_buttons = page.locator("[data-test^='remove']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def get_cart_item_count(self):
        return self.cart_items.count()

    def remove_item(self, item_name):
        self.page.locator(f"[data-test='remove-{item_name}']").click()

    def go_to_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()