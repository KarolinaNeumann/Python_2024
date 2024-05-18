# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/format-json/transformace-dat

# Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující 
# slovník. Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči. 
# Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude. 
# Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly 
# seřazeny a data byla odsazena čtyřmi mezerami pro lepší čitelnost člověkem.
# Vzorový výstup: output.json

# načtení souboru .txt - viz minula lekce - readlines()
import json
with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce10_json\words.txt", encoding = "utf-8") as file:
    words_raw = file.readlines() 
#print(words_raw)

# vytvoření prázdného seznamu 
words = []

for word in words_raw: 
    words.append(word[:-1]) # odebrání 2 posledních znaků \n
#print(words)

# vytvorit prazdny slovnik
slovnik = {}
# {"a": [a, ananas, alio], "b": [banana]...}

# do slovniku zapsat slova - vytorit klice
for word in words:
    # word obsahuje nove slovo, treba "look"
    # je uz "l" (word[0]) ve slovniku jako klic?
    if word[0] in slovnik:          # je-li prvni pismeno = klic
        slovnik[word[0]].append(word)    # pokud ano, pridame na odpovidajici seznam nase nove slovo
    else: 
        slovnik[word[0]] = [word]        # pokud ne, vytvorime novy seznam, ktery bude obsahovat nase nove slovo
                                         # a ulozime ho do slovniku

#print(slovnik)

# Seřazení slov na každém klíči
for letter in slovnik:
    slovnik[letter].sort()
print(slovnik)

# Zápis do JSON souboru s odsazením 4 mezery + seřazení klíčů podle abecedy
with open("slovnik_novy.json", "w") as json_file:
    json.dump(slovnik, json_file, indent=4, sort_keys=True)