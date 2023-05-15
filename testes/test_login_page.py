# from base_test import BaseTest
# from pages.login_page import *
# import unittest

# class TestLoginPage(unittest.TestCase):
#     def test_login_sucesso(self):
#         page = LoginPage()
#         page.login(nome='standard_user', senha='secret_sauce')
#         self.assertIn("inventory" , self.driver.title)    

import sys
import os

# Adicione o caminho para o diretório raiz do seu projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import LoginPage

driver = webdriver.Chrome()

page = LoginPage(driver)
page.abrir()
page.login(nome='standard_user', senha='secret_sauce')

print(driver.current_url)
assert "inventory" in driver.current_url