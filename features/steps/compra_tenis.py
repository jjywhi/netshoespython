from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.screenshot import take_screenshot
import os
CHROMEDRIVER_PATH = 'chromedriver.exe'

@given('que eu acesso o site da Netshoes')
def step_given_usuario_na_pagina_de_login(context):
    service = Service(CHROMEDRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.netshoes.com.br")


@when('eu localizo a barra de pesquisa')
def step_localizo_barra_pesquisa(context):
    context.search_bar = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

@when('eu digito "tênis" e pressiono Enter')
def step_digito_tenis(context):
    context.search_bar.send_keys("Nike")
    context.search_bar.send_keys(Keys.RETURN)

@then('a página de resultados exibe uma lista de tênis disponíveis')
def step_verifica_resultados(context):
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Nike")
    )
    take_screenshot(context.driver, "screenshots/resultados_tenis.png")

@given('que eu estou na página de resultados de tênis')
def step_na_pagina_resultados(context):
    pass  # Já estamos na página de resultados

@when('eu escolho um tênis da lista de resultados')
def step_escolho_tenis(context):
    context.tenis = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Tênis Nike Downshifter 13 Masculino")))
    context.driver.execute_script("arguments[0].click();", context.tenis)
    

@then('a página de detalhes do tênis é carregada')
def step_verifica_pagina_detalhes(context):
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Tênis Nike Downshifter 13 Masculino")
    )
    take_screenshot(context.driver, "screenshots/detalhes_tenis.png")

@given('que eu estou na página de detalhes do tênis')
def step_na_pagina_detalhes(context):
    
    pass  # Já estamos na página de detalhes
    


@when('eu seleciono um tamanho')
def step_seleciono_tamanho(context):
    context.tamanho = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[3]/div[1]/section/div[2]/ul/li[4]/a'))
    )
    context.driver.execute_script("arguments[0].click();", context.tamanho)

@when(u'eu clico no botão "Comprar"')
def step_clico_comprar(context):
    context.botao_comprar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@id, 'content')]/div[2]/div[3]/div[2]/div/div/div/button[contains(text(), 'Comprar')]"))
    )
    context.driver.execute_script("arguments[0].click();", context.botao_comprar)


    take_screenshot(context.driver, "screenshots/confirmacao_carrinho.png")

@then('que eu vejo o  tênis ao carrinho')
def step_tenis_adicionado(context):
    pass  # Já adicionamos o tênis ao carrinho

    take_screenshot(context.driver, "screenshots/confirmacao_carrinho.png")
    
    context.driver.quit()