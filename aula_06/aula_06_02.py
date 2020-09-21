from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)

# usando o atributo type [attr=valor]
# nome = browser.find_element_by_css_selector('[type="text"]')
# senha = browser.find_element_by_css_selector('[type="password"]')
# btn = browser.find_element_by_css_selector('[type="submit"]')

# usando o atributo tag name [attr=valor]
# nome = browser.find_element_by_css_selector('[name="nome"]')
# senha = browser.find_element_by_css_selector('[name="senha"]')
# btn = browser.find_element_by_css_selector('[name="l0c0"]')

# usando o atributo * [attr*=valor]
# nome = browser.find_element_by_css_selector('[name*="me"]')
# senha = browser.find_element_by_css_selector('[name*="nha"]')
# btn = browser.find_element_by_css_selector('[name*="l0"]')

# usando o atributo | [attr|=valor]
# nome = browser.find_element_by_css_selector('[name|="nome"]')
# senha = browser.find_element_by_css_selector('[name|="senha"]')
# btn = browser.find_element_by_css_selector('[name|="l0c0"]')

# usando o atributo ^ [attr^=valor]
nome = browser.find_element_by_css_selector('[name^="n"]')
senha = browser.find_element_by_css_selector('[name^="s"]')
btn = browser.find_element_by_css_selector('[name^="l"]')


nome.send_keys('Gabriel')
senha.send_keys('1705')
sleep(2)

btn.click()
sleep(2)

browser.quit()
