# JSON / PY(dict)
# json - vzdy dvojite uvozovky, true/false vzdy male 1.pismeno, vzdy dava 1 info na 1 radek

# převod json na py-slovnik - LOAD
import json                    # vždy nazačátku

path = r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce10_json\absolventi.json"
#pro .txt text = file.read()

with open(path, encoding = "utf-8") as file:
    absolvents = json.load(file)    # převod na py-slovnik, ukládáání do proměnné absolvents
# print(absolvents)  - vypíše seznam slovníků (1 slovník = 1 absolvent)

for i in absolvents:
    # print(i)             # vypíše všechny slovníky - 1 slovník = 1 řádek
    print(i["dochazka"])   # postupné zanořování do slovníku: vypíše hodnotu klíče "docházka" z každého slovníku         
 

# vytvoreni noveho json ze slovniku - DUMP
# py-slovnik:
hours = {"po": 8, "ut": 7, "st": 6, "ct": 10, "pa": 4}

with open ("hodiny.json", mode= "w", encoding = "utf-8") as file:
    json.dump(hours, file)


# problémy s češtinou - připsat do .dupm argumetnu ENSURE_ASCII
data = {"řeřicha": "Česká Třebová"}
with open ("rericha.json", mode= "w", encoding = "utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii = False)  # rozsype se čeština, proto pridat ensure_ascii


# --- zavod

with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce10_json\zavod.json",  encoding = "utf-8") as file:
    runners = json.load(file)
print(runners[0])                  # cely slovnik
print(runners[0]["jmeno"])         # jen jmeno (zanorovani)