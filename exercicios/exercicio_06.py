from selenium.webdriver import Firefox
from time import sleep

# from time import sleep

browser = Firefox()

url = "https://selenium.dunossauro.live/exercicio_06.html"

browser.get(url)
sleep(2)

for i in range(0, 6):
    sleep(1)

    form_para_preencher = browser.find_element_by_css_selector(
        "header span").text

    form = browser.find_element_by_css_selector(
        f"form.form-{form_para_preencher}")
    form.find_element_by_css_selector(
        'input[name="nome"]').send_keys("Gabriel")
    form.find_element_by_css_selector(
        'input[name="senha"]').send_keys("1705")
    sleep(1)
    form.find_element_by_css_selector(
        f'input[name="{form_para_preencher}"]').click()

# sleep(2)
# browser.quit()
