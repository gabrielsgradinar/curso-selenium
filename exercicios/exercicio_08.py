from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


url = "https://selenium.dunossauro.live/caixinha"

browser = Firefox()
browser.get(url)

caixa = browser.find_element_by_id('caixa')
h1 = browser.find_element_by_tag_name('h1')

ac = ActionChains(browser)


def mouse_enter_leave(elemento, ac) -> None:
    '''
    normal
    normal + shift
    normal + ctrl
    normal + ctrl + shift
    '''
    ac.move_to_element(elemento)
    ac.pause(1)
    ac.move_to_element(h1)

    ac.key_down(Keys.SHIFT)
    ac.move_to_element(elemento)
    ac.pause(1)
    ac.move_to_element(h1)
    ac.key_up(Keys.SHIFT)

    ac.key_down(Keys.CONTROL)
    ac.move_to_element(elemento)
    ac.pause(1)
    ac.move_to_element(h1)
    ac.key_up(Keys.CONTROL)

    ac.key_down(Keys.CONTROL)
    ac.key_down(Keys.SHIFT)
    ac.move_to_element(elemento)
    ac.pause(1)
    ac.move_to_element(h1)
    ac.key_up(Keys.CONTROL)
    ac.key_up(Keys.SHIFT)


def click(elemento, ac) -> None:
    '''
    normal
    normal + shift
    normal + ctrl
    normal + ctrl + shift
    '''
    ac.move_to_element(elemento)

    ac.click()
    ac.pause(1)

    ac.key_down(Keys.SHIFT)
    ac.click()
    ac.pause(1)
    ac.key_up(Keys.SHIFT)

    ac.key_down(Keys.CONTROL)
    ac.click()
    ac.pause(1)
    ac.key_up(Keys.CONTROL)

    ac.key_down(Keys.SHIFT)
    ac.key_down(Keys.CONTROL)
    ac.click()
    ac.pause(1)
    ac.key_up(Keys.SHIFT)
    ac.key_down(Keys.CONTROL)

    ac.move_to_element(h1)


def dblclick(elemento, ac):
    '''
    normal
    normal + shift
    normal + ctrl
    normal + ctrl + shift
    '''
    ac.move_to_element(elemento)

    ac.double_click()
    ac.pause(1)

    ac.key_down(Keys.SHIFT)
    ac.double_click()
    ac.pause(1)
    ac.key_up(Keys.SHIFT)

    ac.key_down(Keys.CONTROL)
    ac.double_click()
    ac.pause(1)
    ac.key_up(Keys.CONTROL)

    ac.key_down(Keys.SHIFT)
    ac.key_down(Keys.CONTROL)
    ac.double_click()
    ac.pause(1)
    ac.key_up(Keys.SHIFT)
    ac.key_down(Keys.CONTROL)

    ac.move_to_element(h1)


mouse_enter_leave(caixa, ac)
click(caixa, ac)
dblclick(caixa, ac)
ac.pause(1)
ac.move_to_element(caixa)
ac.context_click()
ac.pause(1)
ac.perform()

resultados = browser.find_element_by_id('area').text.split("\n")
# print(resultados.split("\n"))

cores = []

for r in resultados:
    cor = r.split('cor:"')[1].split('",')[0]
    cores.append(cor)

cores = set(cores)
print(cores)
print(f'{len(cores)} cores')
