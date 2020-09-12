from selenium.webdriver import Firefox


def find_by_text(browser, tag, text):
    """ Encontrar o elemento com o texto 'text'
    Args:
        browser : Instância do browser [firefox, chrome, etc]
        text : conteúdo que deve estart na tag
        tag : tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """ Encontrar o elemento com o 'a' com o link 'link'
    Args:
        browser : Instância do browser [firefox, chrome, etc]
        link : link que será procurado em todas as tag 'a'
    """
    elementos = browser.find_elements_by_tag_name('a')  # lista

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser.get(url)

# elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')
