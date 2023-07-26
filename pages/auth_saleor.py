from playwright.sync_api import expect


class AuthPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:9000/dashboard/")

    def login(self, email, password):
        page = self.page
        page.get_by_test_id('email').fill(email)
        page.get_by_test_id("password").fill(password)
        signin = page.get_by_role("button", name="Sign In")
        signin.click()

    def check_login_success(self):
        expect(self.page.get_by_role(
            "button", name="SigN In")).not_to_be_visible()
