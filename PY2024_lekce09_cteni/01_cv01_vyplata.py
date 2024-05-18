# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/cteni-souboru/vyplata-presneji

# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, 
# což není příliš realistické. Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na
#  každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.


# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. 
# Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.

with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\vykaz.txt", encoding = "utf-8") as file:
    text = file.readlines()

print(text)

# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. 
# Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc. 

hours = []
for line in text:
    hours.append(int(line))
print(hours)

hourly_rate = float(input("Hodinová mzda: "))
print(hourly_rate)

yearly_income = sum(hours) * hourly_rate
print(yearly_income)

print(yearly_income/len(hours))


# -------

# od Anet 
# Otevření souboru a načtení hodin do seznamu
vykaz = []
with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt') as soubor:
    for radek in soubor:
        vykaz.append(int(radek.strip()))


# vykaz = []
# with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt') as soubor:
#     radky = soubor.readlines()
#     for radek in radky:
#         vykaz.append(int(radek.strip()))

# with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt') as soubor:
#     vykaz = list(map(int, soubor.readlines()))


# Výpis seznamu pro kontrolu
print(vykaz)

# Získání hodinové mzdy od uživatele
hodinova_mzda = float(input("Zadejte vaši hodinovou mzdu: "))

# Výpočet celkové výplaty za rok
celkova_vyplata = sum(hodiny * hodinova_mzda for hodiny in vykaz)

# Výpočet průměrné měsíční výplaty
prumerna_vyplata = celkova_vyplata / 12

# Výpis výsledků
print(f"Celková výplata za rok: {celkova_vyplata} Kč")
print(f"Průměrná měsíční výplata: {prumerna_vyplata} Kč")