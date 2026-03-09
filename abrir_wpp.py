from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()

# PERFIL FIXO DEFINITIVO
options.add_argument(r"--user-data-dir=C:\wpp_bot")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://web.whatsapp.com")

input("Escaneie o QR e pressione ENTER quando carregar tudo...")