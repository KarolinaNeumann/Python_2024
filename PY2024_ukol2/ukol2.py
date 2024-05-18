# návod: volani na api, vrati json, dostanu slovnik, vykuchat slovnika a zpracovat podle zadani
# bonus povinny neni 

# import modulu
import requests
import json

# vstup terminal
ICO_vstup = input("Zadejte IČO subjektu: ")
# print(f"subjekt: {ICO_vstup}")

# uprava url podle zadaneho ICO
url = r"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO"
path = url.replace("ICO", ICO_vstup)

# API s daty v .json se prevedou do sloviku (s nazvem data)
response = requests.get(path)
# print(response) ověření Response (kod 200 - ok)
data = response.json()
print(data)

# prevod slovniku (s nazvem data) na .json
with open ("subjekt.json", mode = "w", encoding = "utf-8") as file: 
    json.dump(data, file, ensure_ascii = False)

# ze souboru subjekt.json zjistit jmeno subjektu a sidlo (textovaAdresa)
