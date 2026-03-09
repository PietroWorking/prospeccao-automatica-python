import requests
import pandas as pd
import time
import re
import gspread
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os
import numpy as np
import webbrowser

# AUTH GOOGLE SHEETS (MANTÉM LOGADO!)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = None

if os.path.exists("token.pickle"):
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)

if not creds:
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json",
        SCOPES
    )
    creds = flow.run_local_server(port=0)

    with open("token.pickle", "wb") as token:
        pickle.dump(creds, token)

client = gspread.authorize(creds)

# CRIAR OU ABRIR PLANILHA

NOME_PLANILHA = "base_rj"

try:
    spreadsheet = client.open(NOME_PLANILHA)
    print("Planilha encontrada")
except:
    spreadsheet = client.create(NOME_PLANILHA)
    print("Planilha criada automaticamente")

sheet = spreadsheet.sheet1


spreadsheet.share('', perm_type='anyone', role='reader')


# LIMPAR TELEFONE

def limpar_telefone(numero):
    if not numero:
        return ""

    numero = re.sub(r"\D", "", str(numero))

    if len(numero) >= 10 and not numero.startswith("55"):
        numero = "55" + numero

    return numero


# GOOGLE PLACES API


API_KEY = "senha da API"

search_url = "https://places.googleapis.com/v1/places:searchText"

headers_search = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask":
    "places.id"
}

headers_details = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask":
    "displayName,formattedAddress,nationalPhoneNumber,websiteUri,rating,userRatingCount"
}

queries = [
    "hospital Rio de Janeiro",
    "clinica médica Rio de Janeiro",
    "diagnóstico por imagem Rio de Janeiro",
    "radiologia Rio de Janeiro"
]

lista_geral = []

for query in queries:

    print(f"\n Buscando: {query}")

    response = requests.post(
        search_url,
        headers=headers_search,
        json={"textQuery": query}
    )

    resultado = response.json()

    lugares = resultado.get("places", [])

    print("Resultados encontrados:", len(lugares))

    for place in lugares:

        place_id = place["id"]

        details = requests.get(
            f"https://places.googleapis.com/v1/places/{place_id}",
            headers=headers_details
        ).json()

        telefone = limpar_telefone(
            details.get("nationalPhoneNumber")
        )

        lista_geral.append({
            "Nome": details.get("displayName", {}).get("text"),
            "Endereço": details.get("formattedAddress"),
            "Telefone": telefone,
            "Website": details.get("websiteUri"),
            "Avaliação": details.get("rating"),
            "Total Avaliações": details.get("userRatingCount"),
            "Status Contato": "",
            "Responsável": "",
            "Observações": ""
        })

        time.sleep(0.2)

# DATAFRAME

df_novo = pd.DataFrame(lista_geral)

print("\n Empresas coletadas:", len(df_novo))

if len(df_novo) == 0:
    print(" Nenhum resultado encontrado")
    exit()

dados_existentes = sheet.get_all_records()

if dados_existentes:
    df_existente = pd.DataFrame(dados_existentes)
    df_final = pd.concat([df_existente, df_novo])
else:
    df_final = df_novo

df_final = df_final.drop_duplicates(subset=["Nome", "Telefone"])

# CORREÇÃO DO ERRO JSON (PROBLEMA SÉRIO!)
df_final = df_final.replace([np.inf, -np.inf], "")
df_final = df_final.fillna("")

print(" Total final:", len(df_final))

# ATUALIZAR GOOGLE SHEETS

sheet.clear()

sheet.update(
    range_name="A1",
    values=[df_final.columns.tolist()] +
           df_final.values.tolist()
)

print("\n GOOGLE SHEETS ATUALIZADO!")

# ABRIR AUTOMATICAMENTE

url = f"https://docs.google.com/spreadsheets/d/{spreadsheet.id}"

webbrowser.open(url)

print(" Planilha aberta automaticamente!")