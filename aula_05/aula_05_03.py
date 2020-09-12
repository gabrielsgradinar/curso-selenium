from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_05_c.html'

browser.get(url)


def melhor_filme(browser, filme, email, telefone):
    """Preenche o formulários do melhor filme de 2020. """

    browser.find_element_by_name('filme').send_keys(filme)
    email = browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()


melhor_filme(
    browser,
    'Senhor dos Anéis',
    'gabriel@gmail.com',
    '(011)978012388'
)

browser.quit()
