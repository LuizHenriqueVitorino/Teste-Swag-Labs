import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        # print("-------------Início----------------")
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.close() 
        # print("-----------Fim do Teste----------\n")
        