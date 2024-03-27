# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/excs/prevody-jednotek
# Převod kilometrů na míle a zpět
# Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), 
# které provedou převod mezi kilometry a mílemi.

def mile_na_km(mile):
    return 1.6 * mile
print(mile_na_km(21))