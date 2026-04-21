from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item_to_cart(self, item_name):
        self.page.locator(f"[data-test='add-to-cart-{item_name}']").click()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()
    
    def sort_by_price_low_to_high(self):
        self.page.locator("[data-test='product-sort-container']").select_option("lohi")

def filter_by_price_range(self, min_price, max_price):
    self.page.locator("[data-test='filter-price-min']").fill(str(min_price))
    self.page.locator("[data-test='filter-price-max']").fill(str(max_price))
    self.page.locator("[data-test='filter-button']").click()
        