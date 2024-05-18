# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/format-json/zavod

# Pracuj dál se souborem zavod.json. Cílem cvičení je zjistit čas závodníka, 
# který získal stříbrnou medaili - seznam závodníků je seřazený, tedy výherce je zapsán jako
# první v našem souboru. Budeš tedy muset projít data pomocí cyklu a vytvořit seznam všech 
# závodníků, kteří závod dokončili, tj. jejich oficiální čas není 'DNF'.

#načtení souboru json (load)
import json

with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce10_json\zavod.json", encoding = "utf-8") as file:
    runners = json.load(file)
print(runners)     

# Vytvoř si prázdný seznam finishers, kam budeš vkládat jména závodníků, kteří závod doběhli.
finishers = {}

# Pomocí cyklu projdi seznam závodníků. 

for runner in runners:
    if runner['casy']['oficialni'] != 'DNF':    # != není 
        finishers.append([runner['jmeno'], runner['casy']['oficialni']])  # přidá jméno a čas do seznamu finishers, pokud závodník dokončil závod

print(finishers[1])   #cci vědět stříbrnou medaily - tj. 2. místo v závodu - tj. index 1