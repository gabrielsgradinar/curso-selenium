from selenium.webdriver import Firefox
from time import sleep


def find_by_text(browser, tag, text):
    """ Encontrar o elemento com o texto 'text'
    Args:
        browser : Instância do browser [firefox, chrome, etc]
        text : conteúdo que deve estart na tag
        tag : tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_04_b.html'

browser.get(url)

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.back()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.forward()
