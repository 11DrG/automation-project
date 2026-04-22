from playwright.sync_api import Page
from pages.inventory_page import InventoryPage

def test_sort_by_price_low_to_high(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_price_low_to_high()
    assert inventory.page.locator("[data-test='product-sort-container']").input_value() == "lohi"

def test_sort_by_price_high_to_low(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_price_high_to_low()
    assert inventory.page.locator("[data-test='product-sort-container']").input_value() == "hilo"

def test_sort_by_name_a_to_z(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_name_a_to_z()
    assert inventory.page.locator("[data-test='product-sort-container']").input_value() == "az"

def test_sort_by_name_z_to_a(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by_name_z_to_a()
    assert inventory.page.locator("[data-test='product-sort-container']").input_value() == "za"