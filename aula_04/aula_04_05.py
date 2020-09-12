"""
    1. Pegar todos os links de aulas
        {'nomde da aula': 'link da aula'}
    2. Navegar até o exercício 3
        achar a url do exercício 3 e ir até la
"""

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_04.html'

browser.get(url)


def get_links(browser, elemento):
    """
    Pega todos os links dentro de um elemento

    - browser = a instância do navegador
    - elemento = webelement
    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado


# PARTE 1
sleep(2)

aulas = get_links(browser, 'aside')
pprint(aulas)

# PARTE 2

exercicios = get_links(browser, 'main')
pprint(aulas)

exercicio3 = exercicios['Exercício 3']

browser.get(exercicio3)
