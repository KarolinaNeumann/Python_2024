# Rozdělení čísel
# Napiš kód, který zpracuje seznam čísel a vytvoří nový seznam 
# se sudými čísly a nový seznam s lichými čísly z původního seznamu.

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suda = []                                  # definovat prázdný seznam, do ktereho budu přidávat hodnoty
licha = []
for cislo in seznam:
    if cislo % 2 == 0:                     # zbytek po deleni = 2 > suche cislo
        suda.append(cislo)                 # .append prida cislo di prazdneho seznamu "suda"
    else: 
        licha.append(cislo)
print(suda)
print(licha)
