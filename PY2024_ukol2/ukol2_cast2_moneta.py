# input: zadat jmeno
# vzit vstup a projit api
# previst na slovnik
# prochazet slovnik for cyklem s podminkou IN - print : f"retezec "nalezeno subjetu: " a vypis

import requests, json

# vstup terminal
# subj_name = input("Zadejte název subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno" : "moneta"}'
response = requests.post(
    r"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", 
    headers=headers, 
    data=data
    )

# print(response) # ověření Response (kod 200 - ok)
data = response.json()
print(data)

