import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def logged_in_page(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return page

def test_add_item_to_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    assert inventory.get_cart_count() == "1"

def test_add_multiple_items_to_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.add_item_to_cart("sauce-labs-bike-light")
    assert inventory.get_cart_count() == "2"

def test_remove_item_from_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.remove_item("sauce-labs-backpack")
    assert cart.get_cart_item_count() == 0

def test_cart_proceeds_to_checkout(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.go_to_checkout()
    assert "checkout" in logged_in_page.url