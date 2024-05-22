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
print(data) # pri zadani vstupu: "jakub neumann" vypise 15 subjektu + info o nich

