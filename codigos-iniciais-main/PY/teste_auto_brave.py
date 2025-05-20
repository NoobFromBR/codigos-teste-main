from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Caminho para o Brave e o ChromeDriver
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver_path = "F:\\code\\chromedriver-win64\\chromedriver.exe"  # ajuste conforme necessário

# Configurações do navegador
options = Options()
options.binary_location = brave_path
options.add_argument("--start-maximized")  # iniciar maximizado
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Inicializa o serviço e o navegador
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Teste: abrir o Google
driver.get("https://www.google.com")

# Espera alguns segundos para você ver
time.sleep(5)

# Encerra o navegador
driver.quit()
