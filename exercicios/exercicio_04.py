from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

browser = Firefox()

url = 'https://selenium.dunossauro.live/exercicio_04.html'

browser.get(url)


def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


sleep(2)

estrutura = {
    'nome': 'Julia',
    'email': 'julia@gmail.com',
    'senha': '1705',
    'telefone': '11989063499'
}

preenche_form(browser, **estrutura)

url_parseada = urlparse(browser.current_url)

sleep(2)

texto_resultado = browser.find_element_by_tag_name('textarea').text

resultado_arrumado = texto_resultado.replace('\'', "\"")

dict_result = loads(resultado_arrumado)

if dict_result == estrutura:
    print("Deu bom")
