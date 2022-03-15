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
navegador.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/1000/varzeaalegre-ce')



time.sleep(4)
navegador.quit()
