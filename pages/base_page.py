class BasePage():
    def __init__(self, driver, base_url='https://www.saucedemo.com/'):
        self.url = base_url
        self.driver = driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def abrir(self, url):
        self.driver.get(url)

    def get_titulo(self):
        return self.driver.title
    
    def escrever(self, locator, str):
        elemento = self.encontrar_elemento(locator)
        elemento.send_keys(str)

    def clicar(self, locator):
        elemento = self.encontrar_elemento(locator)
        elemento.click()