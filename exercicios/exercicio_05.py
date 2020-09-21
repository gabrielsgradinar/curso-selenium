from selenium.webdriver import Firefox
from time import sleep

# from time import sleep

browser = Firefox()

url = 'https://selenium.dunossauro.live/exercicio_05.html'

browser.get(url)

sleep(2)

form_l0c0 = browser.find_element_by_css_selector('form.form-l0c0')
form_l0c0.find_element_by_css_selector(
    'input[name="nome"]'
    ).send_keys('Gabriel')

form_l0c0.find_element_by_css_selector(
    'input[name="senha"]'
    ).send_keys('1705')

form_l0c0.find_element_by_css_selector(
    'input[name="l0c0"]'
    ).click()


form_l0c1 = browser.find_element_by_css_selector('form.form-l0c1')
form_l0c1.find_element_by_css_selector(
    'input[name="nome"]'
    ).send_keys('Julia')

form_l0c1.find_element_by_css_selector(
    'input[name="senha"]'
    ).send_keys('1705')

form_l0c1.find_element_by_css_selector(
    'input[name="l0c1"]'
    ).click()


form_l1c0 = browser.find_element_by_css_selector('form.form-l1c0')
form_l1c0.find_element_by_css_selector(
    'input[name="nome"]'
    ).send_keys('Tiago')

form_l1c0.find_element_by_css_selector(
    'input[name="senha"]'
    ).send_keys('1705')

form_l1c0.find_element_by_css_selector(
    'input[name="l1c0"]'
    ).click()


form_l1c1 = browser.find_element_by_css_selector('form.form-l1c1')
form_l1c1.find_element_by_css_selector(
    'input[name="nome"]'
    ).send_keys('Nicolly')

form_l1c1.find_element_by_css_selector(
    'input[name="senha"]'
    ).send_keys('1705')

form_l1c1.find_element_by_css_selector(
    'input[name="l1c1"]'
    ).click()

sleep(2)
# browser.quit()
