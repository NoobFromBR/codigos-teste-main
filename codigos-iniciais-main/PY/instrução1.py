#instalar biblioteca selenium
#instalar chomedriver
#imporar biblioteca selenium
from selenium import webdriver
import time

#definir navegador
navegador = webdriver.Chrome()

#definir site
navegador.get("https://www.google.com/?hl=pt-BR")
