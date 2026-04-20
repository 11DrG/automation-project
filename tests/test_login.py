from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_password(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "wrong_password")
    assert "Epic sadface" in login.get_error_message()

def test_empty_credentials(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    assert "Epic sadface" in login.get_error_message()