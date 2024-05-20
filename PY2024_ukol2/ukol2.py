# návod: volani na api, vrati json, dostanu slovnik, vykuchat slovnika a zpracovat podle zadani
# bonus povinny neni 

# import modulu
import requests, json

# vstup terminal
ICO_vstup = input("Zadejte IČO subjektu: ")
# print(f"subjekt: {ICO_vstup}")

# uprava url podle zadaneho ICO - 22834958
url = r"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO"
path = url.replace("ICO", ICO_vstup)

# API s daty ve formatu .json se prevedou do sloviku (s nazvem data)
response = requests.get(path)
# print(response) ověření Response (kod 200 - ok)
data = response.json()
# print(data)

# prevod slovniku (s nazvem data) na .json - obsahuje jiz konkretni data o subjektu
with open ("subjekt.json", mode = "w", encoding = "utf-8") as file: 
    json.dump(data, file, ensure_ascii = False)

# ze souboru subjekt.json zjistit jmeno subjektu a sidlo (textovaAdresa)
## prevod souboru subjekt.json na slovnik.py

path_subj = r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_ukol2\subjekt.json"     
with open (path_subj, encoding = "utf-8") as file:
    slovnik_subj = json.load(file)        # slovnik obsahuje info o danem subj                                              
# print(slovnik_subj)

print(slovnik_subj["obchodniJmeno"] + ", " + slovnik_subj["sidlo"]["textovaAdresa"])