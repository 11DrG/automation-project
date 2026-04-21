from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

items_to_add = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"]

def test_add_multiple_items_from_list(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    for item in items_to_add:
        inventory.add_item_to_cart(item)
    assert inventory.get_cart_count() == "3"

def test_remove_specific_item(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.add_item_to_cart("sauce-labs-bike-light")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.remove_item("sauce-labs-backpack")
    assert cart.get_cart_item_count() == 1

def test_add_all_items_in_list(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    for item in items_to_add:
        inventory.add_item_to_cart(item)
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    assert cart.get_cart_item_count() == 3