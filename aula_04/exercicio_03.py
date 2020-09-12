from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse


def find_elemente_by_text(browser, tag, text):
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


def find_answer(browser, texto='', url=''):
    """ Encontrar a resposta correta na página do exercício
    Args:
        browser : Instância do browser [firefox, chrome, etc]
        text : conteúdo que deve estar no attr da tag 'a' [errado, certo]
    """
    main = browser.find_element_by_id('main')
    lis = main.find_elements_by_tag_name('li')
    for li in lis:
        a = li.find_element_by_tag_name('a')
        if a.get_attribute('attr') == texto:
            return a
        if a.text == url:
            return a


browser = Chrome()

url = 'https://selenium.dunossauro.live/exercicio_03.html'

browser.get(url)

# pagina 0
sleep(3)
ancora = find_elemente_by_text(browser, 'a', 'Começar por aqui')
ancora.click()

# pagina 1
sleep(3)
find_answer(browser, texto='errado').click()

# pagina 2
sleep(40)
find_answer(browser, texto='certo').click()

# pagina 3
sleep(3)
url_atual = urlparse(browser.current_url)
find_answer(browser, url=url_atual).click()

# pagina 4
sleep(3)
browser.refresh()

sleep(2)
browser.quit()
