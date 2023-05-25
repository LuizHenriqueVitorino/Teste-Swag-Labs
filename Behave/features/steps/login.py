from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

driver = webdriver.Chrome()

@given(u'que eu esteja na página de Login')
def ir_para_login(context):
    driver.get('https://www.saucedemo.com/')

@when(u'eu Escrever meu nome de usuário')
def escrever_username(context):
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')

@when(u'Escrever minha senha')
def escrever_senha(context):
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')

@when(u'Clicar no botão de Login')
def submit(context):
    driver.find_element(By.ID, 'login-button').click()


@then(u'eu devo logar no sistema')
def assert_homepage(context):
    assert 'inventory' in driver.current_url