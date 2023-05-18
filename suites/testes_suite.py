import unittest
from testes.test_login_page import TestLoginPage
from testes.test_logout import TestLogout
from testes.test_cart import TestCart

class TestesSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLoginPage))
    suite.addTest(unittest.makeSuite(TestLogout))
    suite.addTest(unittest.makeSuite(TestCart))