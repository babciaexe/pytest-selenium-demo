from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.test_data import TestData


class TestLogin(BaseTest):
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        title = login_page.get_title()
        assert title == "My Account"
