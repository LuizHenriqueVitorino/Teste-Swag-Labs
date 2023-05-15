import sys
import os

# Adicione o caminho para o diretório raiz do seu projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
# from suites.testes_suite import TestPages
from testes.test_login_page import TestLoginPage


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
    
    def tearDown(self) -> None:
        self.driver.close() 
        
if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    unittest.TextTestRunner().run(suite)