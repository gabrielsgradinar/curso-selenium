from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_elemento(by, elemento, webdriver):
    print(f"Procurando o elemento {elemento} por {by}")
    elementos = webdriver.find_elements(by, elemento)
    if elementos:
        print(f"Achei o {elemento}")
        print(elementos[0].get_attribute('class'))
        return True
    return False


esperar_botao = partial(esperar_elemento, By.CLASS_NAME, 'selenium')

url = "https://selenium.dunossauro.live/exercicio_09.html"

browser = Firefox()

wdw = WebDriverWait(browser, 30, poll_frequency=0.2)

browser.get(url)

# Esperar botao
wdw.until(esperar_botao, 'Deu ruim, nao achei o selenium')
