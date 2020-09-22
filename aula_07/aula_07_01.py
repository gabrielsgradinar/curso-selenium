"""
1. Checar se a mudança ocorre no span(focus, blue)
2. Checar se a mudança ocorre no p (change)
"""
from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_07_d.html'

browser.get(url)

input_de_texto = browser.find_element_by_tag_name('input')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

"""
Quando clicar no elemento 'input'
Então o texto 'esta com foco' deve ser o content de 'span'
Quando clicar no elemento 'span'
Então o texto 'esta sem foco' deve ser o content de 'span'
"""
input_de_texto.click()
assert "está com foco" == span.text
span.click()
assert "está sem foco" == span.text

# browser.quit()

"""
Dado que o texto '1' deve ser o content de 'p'
Quando enviar 'batata' no elemento 'input'
Então o texto 'esta com foco' deve ser o content de 'span'
Quando clicar no elemento 'span'
Então o texto 'esta sem foco' deve ser o content de 'span'
Então o texto '1' deve ser o content de 'p'
"""

assert p.text == '0', 'p não é zero'
input_de_texto.send_keys('batata')
assert "está com foco" == span.text
span.click()
assert "está sem foco" == span.text
assert p.text == '1', 'p não é um'
