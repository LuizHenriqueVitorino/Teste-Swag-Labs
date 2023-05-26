from selenium.webdriver.common.by import By
from behave import given, when, then


@given(u'que eu esteja na página de Login')
def ir_para_login(context):
    context.driver.get('https://www.saucedemo.com/')

@when(u'eu preencher o campo usuário com {usuario}')
def escrever_username(context, usuario):
    context.driver.find_element(By.ID, 'user-name').send_keys(usuario)

@when(u'preencher o campo senha com {senha}')
def escrever_senha(context, senha):
    context.driver.find_element(By.ID, 'password').send_keys(senha)

@when(u'Clicar no botão de Login')
def submit(context):
    context.driver.find_element(By.ID, 'login-button').click()


@then(u'{resultado}')
def verifica_resultado(context, resultado):
    if resultado == 'devo logar no sistema':
        usuario_logado = is_usuario_logado
        assert usuario_logado, "O usuário não logou"
    elif resultado == 'devo receber uma mensagem de erro':
        mensagem = get_mensagem_usuario_bloqueado(context)
        assert mensagem == 'Epic sadface: Sorry, this user has been locked out.', mensagem

def is_usuario_logado(context):
    return True if 'inventory' in context.driver.current_url else False

def get_mensagem_usuario_bloqueado(context) -> str:
    mensagem = context.driver.find_element(By.XPATH, '//div/h3').text
    return mensagem