from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("[data-test='firstName']")
        self.last_name_field = page.locator("[data-test='lastName']")
        self.postal_code_field = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.confirmation_header = page.locator(".complete-header")
        self.error_message = page.locator("[data-test='error']")

    def fill_details(self, first_name, last_name, postal_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_confirmation_message(self):
        return self.confirmation_header.text_content()

    def get_error_message(self):
        return self.error_message.text_content()