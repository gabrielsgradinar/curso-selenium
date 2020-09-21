from selenium.webdriver import Firefox

# from time import sleep

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)

browser.find_elements_by_css_selector('div.form_group')

browser.find_elements_by_css_selector(
    'div.form-group + br'  # br irmão de div class form_group
)

# da tag div com a classe form-group pegue o filho com o id dentro-nome
browser.find_elements_by_css_selector('div.form_group > #dentro-nome')

# do form, pegue todas as tag label existentes
# ignorando a hierarquia (decendente)
browser.find_elements_by_css_selector('form label')
