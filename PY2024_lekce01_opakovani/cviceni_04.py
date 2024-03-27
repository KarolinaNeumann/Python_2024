# součet čísel v seznamu 
# Napiš kód, který zpracuje seznam čísel a vypíše jejich součet (bez použití funkce sum()).

seznam = [1, 2, 3, 4, 5]          # definovat seznam
soucet = 0                        # definovat začátek
for cislo in seznam:              # "cislo" (mnou zvolena promenna pro cyklus), prochází seznam viz ř. 3
    soucet += cislo               # přičte číslo k předchozímu v seznamu
print(soucet)
