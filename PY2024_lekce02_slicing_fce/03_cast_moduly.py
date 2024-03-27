# moduly = sbirky funkci 
# pred pouzitim nutne importovat NA ZACATEK CELEHO SCRIPTU 
# POZOR !!!! nepojmenovat script stejne jako modul (prepsal by se cely a nebude fungovat) 

# MODUL MATH - zaokrouhleni nahoru (ceil = ceiling - strop) a dolu (floor - podlaha, dolu)
import math     # math = nazev modulu
cislo = 3.14
print(math.floor(cislo))    # zapis bez math. bude brecet, nevi odkud fci floor ma spustit print(floor(cislo)) >nutne vzdy uvadet modul
                            # je i jiny zpusob pres dunder podtrzitka, je ale pro interni potreby ostatnim nepristupne
                            # vse co zacina __ NEPOUZIVAT !!!

print(math.ceil(cislo))

# MODUL STATISTICS 
import statistics
print(statistics.mean([1, 10]))   # vypise prumer z daneho seznamu 


