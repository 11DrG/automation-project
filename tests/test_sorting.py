from playwright.sync_api import Page
from pages.inventory_page import InventoryPage

def test_sort_products_by_price_low_to_high(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_price_low_to_high()
    assert "lohi" in logged_in_page.url or logged_in_page.locator("[data-test='product-sort-container']").input_value() == "lohi"