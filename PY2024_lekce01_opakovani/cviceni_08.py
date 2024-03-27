# Odstraneni duplikatu
# Napiš kód, který zpracuje seznam a vytvoří nový seznam bez duplikátů. Výsledné pořadí prvků musí být zachováno.

seznam = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9]          # vychozi seznam
bez_duplicit = []                                         # zacatek: vytvorit prazdny seznam
for cislo in seznam:
    if cislo not in bez_duplicit:                         # neni-li uz číslo v seznamu bez_duplicit
        bez_duplicit.append(cislo)                        # pridej toto cislo do seznamu bez_duplicit
print(bez_duplicit)