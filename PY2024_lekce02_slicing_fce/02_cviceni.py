# zadani 1 - prevod pismen
# Uložte si do proměnné jmeno svoje jméno. 
# Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

jmeno = "Kája"
print(jmeno.upper())
print(jmeno.lower())


# zadani 2 - cisla jako text
# Mějme seznam celých čísel zadaných jako text 
hodnoty = ['12', '1', '7', '-11']
# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto: hodnoty = ['12', '1', '11', '-11'] 

hodnoty[2] = "11"  # bude platne pouze v tomto pripade

# spravně reseni:
# Uložení hodnoty na třetí pozici do proměnné
hodnota_na_treti_pozici = hodnoty[2]

# Přičtení 4 k hodnotě a uložení výsledku do proměnné
vysledek = int(hodnota_na_treti_pozici) + 4

# Převedení výsledku zpět na řetězec a uložení na třetí pozici v seznamu hodnoty
hodnoty[2] = str(vysledek)

print(hodnoty)


# zadani 3 
# Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu, 
# ale v řetězci oddělená mezerou:
# 1. z retezce udelat seznam : 

hodnoty = '12.1 1.68 7.45 -11.51'

# Rozdělení řetězce na seznam čísel
seznam_cisel = hodnoty.split()

# Převedení posledního čísla na float, přičtení 0.25 a převedení zpět na řetězec
posledni_cislo = float(seznam_cisel[-1]) + 0.25
seznam_cisel[-1] = str(posledni_cislo)

# Spojení upraveného seznamu zpět do řetězce
upraveny_retezec = ' '.join(seznam_cisel)

print(upraveny_retezec)