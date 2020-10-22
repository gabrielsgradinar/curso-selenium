from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False


locator = (By.CSS_SELECTOR, 'button')
esperar_botao = EsperarElemento(locator)

url = "https://selenium.dunossauro.live/aula_09_a.html"

browser = Firefox()

wdw = WebDriverWait(browser, 10, poll_frequency=0.5)

browser.get(url)

# Esperar botao
wdw.until(esperar_botao)

# Clicar no botao
browser.find_element_by_css_selector('button').click()


wdw.until(
    EsperarElemento(locator=(By.ID, 'finished')),
    "A mensagem de sucesso nao apareceu"
    )

sucesso = browser.find_element_by_css_selector('#finished')

assert sucesso.text == "Carregamento concluído"
