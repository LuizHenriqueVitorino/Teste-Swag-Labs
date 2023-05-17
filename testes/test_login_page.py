from pages.login_page import LoginPage
from testes.base_test import BaseTest

class TestLoginPage(BaseTest):
    def test_login(self):
        page = LoginPage(self.driver)
        page.abrir()
        page.login(nome='standard_user', senha='secret_sauce')

        print(self.driver.current_url)
        assert "inventory" in self.driver.current_url