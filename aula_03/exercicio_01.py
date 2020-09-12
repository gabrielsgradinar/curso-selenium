from selenium.webdriver import Firefox
from time import sleep
import pprint

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Firefox()

browser.get(url)

sleep(2)

h1 = browser.find_element_by_tag_name('h1')

dicionario = {}

dicionario[h1.text] = {}

atributos = browser.find_elements_by_tag_name('p')
for atributo in atributos:
    atributo_nome = atributo.get_attribute('atributo')
    dicionario[h1.text][atributo_nome] = atributo.text

pprint.pprint(dicionario)

browser.quit()
