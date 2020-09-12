from selenium.webdriver import Firefox
from urllib.parse import urlparse


browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser.get(url)

url_parseada = urlparse(browser.current_url)
