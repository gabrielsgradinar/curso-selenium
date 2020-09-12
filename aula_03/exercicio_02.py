from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Firefox()

browser.get(url)

sleep(2)

ancora = browser.find_element_by_id('ancora')

ganhou = False
while(ganhou is not True):
    ancora.click()
    pes = browser.find_elements_by_tag_name('p')
    for p in pes:
        if "Você ganhou" in p.text:
            print("Deu bom")
            print(p.text)
            ganhou = True

browser.quit()
