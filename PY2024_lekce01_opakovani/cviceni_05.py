# Nejvyšší prvek v seznamu
# Napiš kód, který zpracuje seznam čísel a vypíše největší prvek v tomto seznamu (bez použití funkce max()).

seznam = [5, 3, 8, 1, 9, 2, 7]
nejvyssi = seznam[0]                 # definovat začátek: zde začátek seznam pomoci indexu 0 - tj. první číslo seznamu
for cislo in seznam:                 # "cislo" - mnou definovana promenna
    if cislo > nejvyssi:
        nejvyssi = cislo
print(nejvyssi)