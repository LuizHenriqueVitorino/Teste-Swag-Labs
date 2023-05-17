import unittest
from testes.test_login_page import TestLoginPage
from testes.test_logout import TestLogout

class TestesSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLoginPage))
    suite.addTest(unittest.makeSuite(TestLogout))