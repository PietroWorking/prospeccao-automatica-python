from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import urllib.parse
import re

# CONFIG CHROME

options = Options()
options.add_argument(r"--user-data-dir=C:\wpp_bot")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://web.whatsapp.com")
input("Pressione ENTER quando carregar o WhatsApp...")

# LISTA ABAIXO

LISTA_NUMEROS = """
5521998190020
552121345000
552131828282
552130781555
552130888100
552139694990
552126070472
552138280730
552124143600
552124470040
5521968029585
552133488066
5521971112006
552131803645
552134059494
552122550145
5521967165417
552125782209
552122551468
552134423322
552137473600
5521971563236
552121254882
552135296666
552135503400
552140039108
552133941101
5521997926926
552139508727
552124559600
552140422050
5519998355398
552139103910
552132831959
551140901740
552131950199
5521997706402
552133367141
552121399999
552125218240
5521991651362
552124342081
552125278001
551140901740
552134337713
552122278080
5530032223
552122559130
5540072001
552124319000
552139778548
552121119150
552122771850
5540020203
552730791382
552124932194
5521975952980
5521973255508
5521999228990
5540072001
552125356000
5521968017477
552131180229
552121122200
5530032223
552125378929
552130035552
5521980575454
5521998078668
5521970261772
552125129181
5521998774692
552133827300
552124131288
552121311400
5521971180996
552122668989
5521989835813
552125441068
"""

# MENSAGENS (RESUMIDO)

mensagens = [
    "Olá! Trabalhamos com diagnóstico raio-X, elevando padrão técnico e reduzindo prazo de entrega. Gostaria de conversar com o responsável para apresentar uma possível melhoria nos processos atuais.",
    "Boa tarde! Estamos ampliando parcerias na área de diagnóstico por imagem e gostaria de falar com o responsável pela parte comercial. Poderia me direcionar, por favor?",
    "Olá! Represento uma empresa especializada em emissão de laudos de raio-X com redução de prazo e custo. Poderia me indicar quem cuida das decisões comerciais na unidade?",
    "Olá! Atuamos como referência em diagnóstico radiológico por raio-X e estamos ajudando instituições a elevar o padrão técnico e reduzir prazos de entrega. Gostaria de apresentar uma oportunidade de melhoria ao responsável pela área.",
    "Boa tarde. Temos desenvolvido soluções em raio-X que aumentam a qualidade dos exames e reduzem custos operacionais. Poderia me direcionar ao responsável para avaliarmos uma possível oportunidade?",
    "Olá! Somos referência em diagnóstico por raio-X e identificamos oportunidades de otimização que impactam tempo, qualidade e preço. Com quem posso falar sobre melhorias na área de imagem?",
    "Boa tarde. Estamos apoiando clínicas e hospitais na evolução dos processos de diagnóstico por raio-X. Gostaria de conversar com o responsável para avaliar se há espaço para melhorias.",
    "Olá! Trabalhamos com soluções modernas em diagnóstico radiológico por raio-X, elevando precisão e reduzindo tempo de resposta. Poderia me indicar o responsável para falarmos sobre uma possível atualização de processo?",
    "Boa tarde. Represento uma empresa referência em diagnóstico por raio-X que tem gerado ganhos técnicos e financeiros para nossos parceiros. Com quem posso tratar sobre uma possível parceria?",
    "Olá! Estamos abrindo novas parcerias na área de diagnóstico por raio-X, com foco em qualidade superior e redução de prazo. Gostaria de apresentar essa oportunidade ao responsável.",
    "Olá! Muitas clínicas estão operando abaixo do potencial na área de raio-X sem perceber. Somos referência no setor e gostaria de apresentar uma possível melhoria ao responsável técnico.",
    "Olá! Somos referência em diagnóstico radiológico por raio-X e temos identificado oportunidades claras de melhoria em qualidade e tempo de entrega em diversas instituições. Gostaria de falar com o responsável para apresentar algo que pode gerar ganho imediato no setor.",
]

# LIMPAR NÚMERO

def limpar_numero(numero):

    numero = re.sub(r"\D", "", numero)

    if numero.startswith("0"):
        numero = numero[1:]

    if not numero.startswith("55"):
        numero = "55" + numero

    return numero


# VALIDAR CELULAR

def numero_whatsapp_valido(numero):

    if len(numero) != 13:
        return False

    # celular brasileiro tem 9 após DDD
    if numero[4] != "9":
        return False

    return True


# TRANSFORMAR TEXTO EM LISTA

numeros = LISTA_NUMEROS.splitlines()

numeros = [
    limpar_numero(n)
    for n in numeros
    if n.strip() != ""
]

numeros = list(set(numeros))

print(f"\nTotal carregado: {len(numeros)}\n")

# CONTADORES

tentativas = 0
enviadas = 0
ignoradas = 0

# ENVIO

for numero in numeros:

    tentativas += 1

    if not numero_whatsapp_valido(numero):
        print(f"[IGNORADO] {numero}")
        ignoradas += 1
        continue

    mensagem = random.choice(mensagens)
    mensagem_codificada = urllib.parse.quote(mensagem)

    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}"
    driver.get(link)

    time.sleep(random.randint(90,300))

    try:
        wait = WebDriverWait(driver,40)

        campo = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,'//div[@contenteditable="true"][@data-tab="10"]')
            )
        )

        time.sleep(random.uniform(1.5,3.5))
        campo.send_keys(Keys.ENTER)

        print(f"[ENVIADO] {numero}")
        enviadas += 1

        delay = random.randint(150,400)
        print(f"Aguardando {delay}s\n")
        time.sleep(delay)

    except:
        print(f"[ERRO] {numero}")
        continue


# RELATÓRIO PROMPT

print("\n========== RELATÓRIO ==========")
print(f"Tentativas: {tentativas}")
print(f"Enviadas: {enviadas}")
print(f"Ignoradas: {ignoradas}")
print("================================")