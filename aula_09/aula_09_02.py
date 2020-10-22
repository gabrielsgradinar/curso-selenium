from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait


def esperar_botao(webdriver) -> bool:
    elementos = webdriver.find_elements_by_css_selector('button')
    print('Tentando encontrar "button"')
    return bool(elementos)


def esperar_sucesso(webdriver) -> bool:
    elementos = webdriver.find_elements_by_css_selector('#finished')
    print('Tentando encontrar "#finished"')
    return bool(elementos)


url = "https://selenium.dunossauro.live/aula_09_a.html"

browser = Firefox()

wdw = WebDriverWait(browser, 10, poll_frequency=0.5)

browser.get(url)

# Esperar botao
wdw.until(esperar_botao)

# Clicar no botao
browser.find_element_by_css_selector('button').click()


wdw.until(esperar_sucesso, "A mensagem de sucesso nao apareceu")

sucesso = browser.find_element_by_css_selector('#finished')

assert sucesso.text == "Carregamento concluído"
