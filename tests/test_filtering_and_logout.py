from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.header_page import HeaderPage

BASE_URL = "https://www.saucedemo.com/"

def test_logout(logged_in_page: Page):
    header = HeaderPage(logged_in_page)
    header.logout()
    assert logged_in_page.url == BASE_URL

def test_add_item_then_logout(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("sauce-labs-backpack")
    header = HeaderPage(logged_in_page)
    header.logout()
    assert logged_in_page.url == BASE_URL