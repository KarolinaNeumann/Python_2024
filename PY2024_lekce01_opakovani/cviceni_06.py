# Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla z tohoto seznamu.

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for cislo in cisla:
    if cislo % 2 == 0:   # pokud je číslo sudé, vypiš ho
        print(cislo)