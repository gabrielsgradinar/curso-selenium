from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_05.html'

browser.get(url)


def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


sleep(2)

estrutura = {
    'nome': 'Gabriel',
    'email': 'gabriel@gmail.com',
    'senha': '123789123',
    'telefone': '11978061455'
}

preenche_form(browser, **estrutura)

url_parseada = urlparse(browser.current_url)

sleep(2)

texto_resultado = browser.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dict_result = loads(resultado_arrumado)

assert dict_result == estrutura
