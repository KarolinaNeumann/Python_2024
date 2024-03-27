# zaokrouhlovani 
# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo 
# zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.

import math
cislo = (float(input("vložte čílo: ")))
print(cislo)

print(math.ceil(cislo))  # zaokrouhleni nahoru
print(math.floor(cislo))  # zaokrouhleni dolu
print(round(cislo))      # zaokrouhleni klasice, soucasti zakladniho baliku python - nemusim

print(int(cislo))         # vypise cele cislo př. 5 (float vypise př. 5.0)