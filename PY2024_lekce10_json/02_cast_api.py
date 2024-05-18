# api - application programating inteface
# api - ma v sobe pripravene informace ke stazeni
# stahuje pouze jako json, ja si ho pak prepisu do slovniku a uzu s tim pracovat dal

import requests
response = requests.get('https://api.kodim.cz/python-data/people')
print(response)        # vypíše kód, zda odkaz je funkční = hodnota 200 je OK (300 a 400 NEBRAT!!)
                       # nejedná se o data ! 

# --- 
# pro přehlednost ukldat cestu do proměnné path:

# import requests
path = ('https://api.kodim.cz/python-data/people')   # cesta k webu, kde jsou připravená data
response = requests.get(path)                        # volám data pomocí fce .get z balíčku requests
data = response.json()                               # data z webu (formát .json) PŘEVEDE DO DICT
print(type(data)) # ověření výstupního formátu - zde seznam slovníků 
# print(data)                    # vypíše celý soubor - 1000 jmen s údaji o osobě
 
print(data[0])                 # vypíše info o první osobě  
print(data[0]["first_name"])   # vypíše hodnotu kklíče "first_name" > Frederic 
