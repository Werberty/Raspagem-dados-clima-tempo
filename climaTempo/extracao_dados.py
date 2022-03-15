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

navegador = webdriver.Chrome()
url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/1000/varzeaalegre-ce'
navegador.get(url)

# temp_min = navegador.find_element(
#     by=By.XPATH, value='//*[@id="min-temp-1"]').text
# temp_max = navegador.find_element(
#     by=By.XPATH, value='//*[@id="max-temp-1"]').text
temperatura = navegador.find_element(
    by=By.XPATH, value='//ul[@class="variables-list"]/li[1]/div').text
chuva = navegador.find_element(
    by=By.XPATH, value='//ul[@class="variables-list"]/li[2]/div').text
vento = navegador.find_element(
    by=By.XPATH, value='//ul[@class="variables-list"]/li[3]/div').text
umidade = navegador.find_element(
    by=By.XPATH, value='//ul[@class="variables-list"]/li[4]/div').text
sol = navegador.find_element(
    by=By.XPATH, value='//ul[@class="variables-list"]/li[5]/span[2]').text

# print(temp_min, temp_max, chuva, vento)

print(temperatura)
print(chuva)
print(vento)
print(umidade)
print(sol)

navegador.quit()
