from utils.locators import *
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver) -> None:
        self.locator = LoginLocators
        super(LoginPage, self).__init__(driver)
    
    def escrever_nome(self, nome):
        self.escrever(self.locator.NOME, nome)

    def escrever_senha(self, senha):
        self.escrever(self.locator.SENHA)

    def clicar_submit(self):
        self.clicar(self.locator.SUBMIT)

    def login(self, nome, senha):
        self.escrever_nome(nome)
        self.escrever_senha(senha)
        self.clicar_submit()

    def get_usuarios(self):
        string = self.encontrar_elemento(self.locator.USUARIOS).text
        vetor = string.split('\n')[1:]
        return vetor
    
    def get_senhas(self):
        string = self.encontrar_elemento(self.locator.SENHAS).text
        vetor = string.split('\n')[1:]
        return vetor

