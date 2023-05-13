from selenium.webdriver.common.by import By

class LoginLocators():
    NOME = (By.ID, "user-name")
    SENHA = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    USUARIOS = (By.ID, "login_credentials")
    SENHAS = (By.CLASS_NAME, "login_password")

