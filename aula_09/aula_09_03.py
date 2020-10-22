from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_elemento(by, elemento, webdriver) -> bool:
    print(f'Tentando encontrar "{elemento}" by {by}')
    if webdriver.find_elements(by, elemento):
        return True
    return False


esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR, 'button')

url = "https://selenium.dunossauro.live/aula_09_a.html"

browser = Firefox()

wdw = WebDriverWait(browser, 10, poll_frequency=0.5)

browser.get(url)

# Esperar botao
wdw.until(esperar_botao)

# Clicar no botao
browser.find_element_by_css_selector('button').click()


wdw.until(
    partial(esperar_elemento, By.ID, 'finished'),
    "A mensagem de sucesso nao apareceu"
    )

sucesso = browser.find_element_by_css_selector('#finished')

assert sucesso.text == "Carregamento concluído"
