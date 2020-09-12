from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser.get(url)

lista_n_ordenada = browser.find_element_by_tag_name('ul')  # primeiro ul

lis = lista_n_ordenada.find_elements_by_tag_name('li')  # todos os li do ul

a = lis[0].find_element_by_tag_name('a').text  # no primeiro li o texto do a
