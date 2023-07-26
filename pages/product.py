from playwright.sync_api import expect, Page


class ProductPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        locator = self.page.locator('//ul[@data-test-id="menu-list-item"]//span[contains(text(),"Products")]')
        locator.click()

    def open_create_modal(self):
        self.page.get_by_test_id('add-product').click()

    def create_one(self):
        self.page.locator('input.MuiInputBase-input').click()
        self.page.get_by_test_id('submit').click()
