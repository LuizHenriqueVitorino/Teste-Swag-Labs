from base_test import BaseTest
from pages.main_page import MainPage
from pages.login_page import LoginPage

from time import sleep

class TestCart(BaseTest):
    def test_cart(self):
        login = LoginPage(self.driver)
        login.abrir()
        login.login(login.get_usuarios()[0], login.get_senhas()[0])

        main = MainPage(self.driver)
        main.clicar_cart()

        self.assertIn("cart", self.driver.current_url)

    