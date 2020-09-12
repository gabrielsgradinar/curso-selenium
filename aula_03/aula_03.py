from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/aula_03.html"

browser = Firefox()

browser.get(url)

sleep(2)

# browser.implicitly_wait(10)

a = browser.find_element_by_tag_name('a')

for click in range(10):
    ps = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do último p: {ps[-1].text}, Valor do click {click}')

    print(f'Os valores são iguais {ps[-1].text == str(click)}')


browser.quit()
