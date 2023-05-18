from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver, base_url='https://www.saucedemo.com/'):
        self.url = base_url
        self.driver = driver
        self.wdw = WebDriverWait(driver, 10)

    def encontrar_elemento(self, locator):
        self.wdw.until(EC.element_to_be_clickable(locator), "Não conseguimos encontrar o elemento!")
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        self.wdw.until(EC.element_to_be_clickable(locator), "Não conseguimos encontrar os elementos!")
        return self.driver.find_elements(*locator)
    
    def abrir(self):
        self.driver.get(self.url)

    def get_titulo(self):
        return self.driver.title
    
    def escrever(self, locator, str):
        elemento = self.encontrar_elemento(locator)
        elemento.send_keys(str)

    def clicar(self, locator):
        elemento = self.encontrar_elemento(locator)
        elemento.click()