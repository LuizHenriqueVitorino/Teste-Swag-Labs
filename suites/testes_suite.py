import unittest
from testes.test_login_page import TestLoginPage

class TestPages(unittest.TestSuite):
    def __init__(self) -> None:
        super().__init__()
        self.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLoginPage))