from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.go_to_checkout()
    checkout = CheckoutPage(logged_in_page)
    checkout.fill_details("John", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()
    assert "Thank you for your order" in checkout.get_confirmation_message()

def test_checkout_without_details(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.go_to_checkout()
    checkout = CheckoutPage(logged_in_page)
    checkout.continue_checkout()
    assert "Error" in checkout.get_error_message()

def test_checkout_without_postal_code(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.go_to_checkout()
    checkout = CheckoutPage(logged_in_page)
    checkout.fill_details("John", "Doe", "")
    checkout.continue_checkout()
    assert "Error" in checkout.get_error_message()