# Farenheit
# Nastuduj, jak se převádějí stupně Fahrenheita na stupně Celsia a napište program, který takový převod provede. 
# Váš program se zeptá uživatele na teplotu ve stupních Fahrenheita a vypíše její ekvivalent ve stupních Celsia.
# wiki: F = (9C/5) + 32

stupen_C = int(input("Zadejte hodnotu ve stupních Ceslia: "))         # POZOR převod vstupu na celá čísla !!!!
prepocet_na_F = ((9 * stupen_C) / 5) + 32
print(prepocet_na_F)
 
# pro převod vstupu vč. des. č použít float(input("Zadej hodnotu ve stupních Celsia: "))
stupen_C = float(input("Zadejte hodnotu ve stupních Ceslia: "))         
prepocet_na_F = ((9 * stupen_C) / 5) + 32
print(prepocet_na_F)
 
