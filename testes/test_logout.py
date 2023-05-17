import sys
import os

# Adicione o caminho para o diretório raiz do seu projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.main_page import MainPage
from pages.login_page import LoginPage
from base_test import BaseTest

class TestLogout(BaseTest):
    def test_logout(self):
        login = LoginPage(self.driver)
        login.abrir()
        login.login(login.get_usuarios()[0], login.get_senhas()[0])

        page = MainPage(self.driver)
        page.logout()


