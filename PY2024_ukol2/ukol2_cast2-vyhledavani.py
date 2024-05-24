import requests, json

# vstup terminal
subj_name = input("Zadejte název subjektu: ")

# hlavičky (ze zadání)
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno" : "' + subj_name + '"}'
response = requests.post(
    r"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", 
    headers=headers, 
    data=data
    )

# print(response) # ověření Response (kod 200 - ok)
data = response.json()

# vypis poctu nalezenych subjketu
pocet_subj = len(data["ekonomickeSubjekty"])
print(f"Počet nalezených subjektů: {pocet_subj}")

# vypis pomoci cyklu
for subjekt in data["ekonomickeSubjekty"]:
   print(subjekt["obchodniJmeno"] + ", " + subjekt["ico"])

