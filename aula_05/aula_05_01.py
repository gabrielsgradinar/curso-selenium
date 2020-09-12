from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_05_a.html'

browser.get(url)

# Selecionando elementos pelo atributo id
div_py = browser.find_element_by_id('python')
div_hk = browser.find_element_by_id('haskell')
print(div_py.text)

browser.quit()
