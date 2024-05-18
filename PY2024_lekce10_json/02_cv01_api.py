# seznam lidi 

# Jak už jsme si ověřili v lekci, datové API na adrese https://api.kodim.cz/python-data/people 
# obsahuje seznam lidí. Napište program, který tento seznam z API stáhne a převede
# z formátu JSON na Python slovníky. Proveďte následující úkoly.

import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
print(data)

# Zjistěte kolik lidí celkem seznam obsahuje.
print(len(data))

# Zjistěte jaké všechny informace máme o jednotlivých osobách.
print(data[0])

# Zjistěte, kolik je v souboru mužů a žen.
num_men = 0
for person in data:
    if person["gender"] == "Male":
        num_men += 1

print(num_men)
print(len(data - num_men))   # pocet žen
