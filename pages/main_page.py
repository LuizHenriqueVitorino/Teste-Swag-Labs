from pages.base_page import BasePage
from utils.locators import MainLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MainLocators

    def clicar_menu(self):
        menu = self.clicar(self.locator.MENU)

    def logout(self):
        self.clicar_menu()
        self.clicar(self.locator.LOGOUT)