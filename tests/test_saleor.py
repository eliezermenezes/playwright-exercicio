import pytest

from pages.auth_saleor import AuthPage
from pages.product import ProductPage
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    playwright.selectors.set_test_id_attribute("data-test-id")

    # playwright.chromium.launch(headless=False)

    return {
        **browser_context_args,
        # "storage_state": "storage.json",
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        # "locale": "it-IT"
    }


# class TestAuth:
#
#     def test_login_valid(self, page: Page):
#         auth = AuthPage(page)
#         auth.navigate()
#         auth.login("admin@gmail.com", "admin")
#         auth.check_login_success()


class TestProduct:
    def test_create_product(self, page: Page):
        # login
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admin@gmail.com", "admin")
        auth.check_login_success()

        # product
        product = ProductPage(page)
        product.navigate()

        # open modal
        product.open_create_modal()
        product.create_one()

