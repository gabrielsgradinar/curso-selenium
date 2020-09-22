from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
from time import sleep


class Escuta(AbstractEventListener):

    def before_click(self, elemento, webdriver):
        label = print_label_modification(elemento, webdriver)
        print(f'Antes do click no {elemento.tag_name}, label = {label}')

    def after_click(self, elemento, webdriver):
        label = print_label_modification(elemento, webdriver)
        print(f'Depois do click no {elemento.tag_name} , label = {label}')


def print_label_modification(elemento, webdriver):
    id = f"l{elemento.get_attribute('name')}"
    label = webdriver.find_element_by_id(id).text
    return label


browser = Firefox()

new_browser = EventFiringWebDriver(browser, Escuta())

url = 'https://selenium.dunossauro.live/exercicio_07.html'

new_browser.get(url)
sleep(2)

nome = new_browser.find_element_by_id('nome')
nome.click()
nome.send_keys('Gabriel')

email = new_browser.find_element_by_id('email')
email.click()
email.send_keys('gabriel@gmail.com')

senha = new_browser.find_element_by_id('senha')
senha.click()
senha.send_keys('1705')

btn = browser.find_element_by_id('btn')
btn.click()
