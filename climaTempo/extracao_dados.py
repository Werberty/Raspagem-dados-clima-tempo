from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# navegador = webdriver.Chrome(options=chrome_options)


def obtem_dados_clima(url):
    navegador = webdriver.Chrome()
    navegador.get(url)

    temperatura = navegador.find_element(
        by=By.XPATH, value='//ul[@class="variables-list"]/li[1]/div').text.split('\n')
    chuva = navegador.find_element(
        by=By.XPATH, value='//ul[@class="variables-list"]/li[2]/div').text
    vento = navegador.find_element(
        by=By.XPATH, value='//ul[@class="variables-list"]/li[3]/div').text
    umidade = navegador.find_element(
        by=By.XPATH, value='//ul[@class="variables-list"]/li[4]/div').text.split('\n')
    sol = navegador.find_element(
        by=By.XPATH, value='//ul[@class="variables-list"]/li[5]/span[2]').text.replace(' ', '-')

    navegador.quit()

    dados_clima = {
        'Temperatura minima': temperatura[0],
        'Temperatura maxima': temperatura[1],
        'Chuva': chuva,
        'Vento': vento,
        'Umidade min': umidade[0],
        'Umidade max': umidade[1],
        'Sol': sol
    }
    return dados_clima


url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/1000/varzeaalegre-ce'
clima = obtem_dados_clima(url)
for k, c in clima.items():
    print(k + ' => ' + c)
