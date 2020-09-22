from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)


class Escuta(AbstractEventListener):
    def before_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('voltando')

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'Antes do click no {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'Depois do click no {elemento.tag_name}')


browser = Firefox()

new_browser = EventFiringWebDriver(browser, Escuta())

url = 'https://selenium.dunossauro.live/aula_07_d.html'

new_browser.get(url)

input_de_texto = new_browser.find_element_by_tag_name('input')
span = new_browser.find_element_by_tag_name('span')
p = new_browser.find_element_by_tag_name('p')

input_de_texto.click()
span.click()

new_browser.get('https://selenium.dunossauro.live/aula_07_c.html')

new_browser.back()
