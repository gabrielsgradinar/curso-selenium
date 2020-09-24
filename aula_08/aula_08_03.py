from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = "https://selenium.dunossauro.live/caixinha"

browser = Firefox()
browser.get(url)

caixa = browser.find_element_by_id('caixa')
h1 = browser.find_element_by_tag_name('h1')

ac = ActionChains(browser)


def caixinha_colorida(key1, key2=None):
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(h1)
    ac.key_up(key1)
    if key2:
        ac.key_up(key2)


caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
caixinha_colorida(Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(caixa)
ac.context_click()
ac.pause(1)
ac.perform()
