# balicek datetime
# soucasti pythonu, staci jen import (vždy na začatku scriptu)
# ma celkem 5 trid (viz obr ve wordu: hlavní pro mě datetime + deltatime)
 
# možnosti importu:
# a. celý balik, dotaz na metodu ve formatu: balik.trida.metoda
# import datetime 
# casto se zkracuje ALIASem (as):
# import datetime as dt

# b. pouze danou třídu, dotaz na metodu ve formatu: trida.metoda
from datetime import datetime, timedelta # lze napsat vice trid

                    
# zjisteni aktualniho casu - metoda .now() ve třídě datetime
print(datetime.now())     # odkaz na tridu datatime pomoci teckove notace

# kdybych importovala:
# cely balik (viz r. 7):
#   print(datetime.datetime.now()) - viz ř. 6
# cely balik s aliasem (viz r. 9):
#   print(dt.datetime.now()) 

# zjisteni dnesniho data - metoda .today() ve třídě datetime:
print(datetime.today())
# lze zjistit ale i ze třídy date:
# from datetime import date (lze jen připsat třídu date k importu ř. 12)
# print(date.today())

# vytvoření vlastního data: funkce .datetime + argument (year – month – day – hour – minute – sec):
# pokud nenapíšu sekundy, python si sám doplní 00 (viz ř. 33)
muj_udaj = datetime(2024, 5, 1, 13, 00)
print(muj_udaj)         # vypíše datum ve tvaru 2024-05-01 13:00:00)

# zjištění dne v týdnu v daném datu (navazuji na muj_udaj - 1.5.2024)
# fce weekday() - pozor počítá dny 0-6 (pondělí = 0)
# fce isoweekday() - počítá dny 1-7 (pondělí = 1)
print(muj_udaj.weekday())   # vypíše 2 (= středa)
# fce isoweekday()
print(muj_udaj.isoweekday())   # vypíše 3 (= středa) 

# formátování času z tvaru (yyyy – mm – dd – hh – mm – ss – msms): 
# fce .isoformat - do výpisu nahradí mezeru písmenem T – podle toho poznám, že je datum v isoformátu)
#    - nezadám-li jinak, nastaví isoformát dané země 
#    - (pozor, každá má vlastní: ČR 1.5.2024, USA 2024-5-1) 
print(muj_udaj.isoformat()) # (2024-05-01 13:00:00 > 2024-05-01T13:00:00)

# fce strftime() string from time: jako argument bude brát formát (= textový řetězec s direktivami
#    direktivy: %Y = year, %m = month, %d = day, %H = hour, %M = min, %S = sec
#    (direktivy lze ruzne kombinovat jak já chci)
print(muj_udaj.strftime("%d. %m. %Y, %H:%M")) # vypíše 01.05.2024, 13:00

# název dne v týdnu (AJ): direktiva %A : 
print(muj_udaj.strftime("%A")) # vypíše Wednesday

# české názvy dnů: 
import locale 
print(locale.setlocale(locale.LC_TIME, 'cz.UTF-8')) # vypíše cs CZ.UTF-8

# převod data v isofotmátu (v terminálu označený T) na klasický datetime: 
# fce fromisoformat()
retezec_iso = "2024-05-01T13:00:00"
print(datetime.fromisoformat(retezec_iso))   # vypíše 2024-05-01 13:00:00

# fce strptime() : převod textového řetězce označující datum/čas na formát datetime
retezec = "1. 5. 2024, 18:30"  # textový řetězec
print(datetime.strptime(retezec, "%d. %m. %Y, %H:%M")) # argument: nadefinovat můj formát

# třída timedelta: pro počítání rozdílů mezi časovými údaji
# nutný import hned na začátku scriptu
dnes = datetime.today()                  # nastavení dnešního data
vcera = dnes - timedelta(days = 1)       # timedelta (tj.rozdíl) v argumentu definuju čas. jednotku
print(dnes, vcera)                       # vypíše dnešní datum + včerejší 
	
# výpočet kolik dní něco trvá (např. kolik dní jsem naživu)
datum_narozeni = datetime(1990, 3, 16)     # definování začátku – tj. datum narození
print(datetime.today() - datum_narozeni)

# výpočet za kolik dní bude něco (např. za jak dlouho budu žít 10.000 dní)
hodnota_timedelta = timedelta(days=10_000, hours = 23)  # podtržítko python nevidí
print(hodnota_timedelta)              # vypíše počet dní, od kterého pak můžu odečítat 
print(hodnota_timedelta.total_seconds) # přepočet na sekundy, pak lze dělit abych se dostala na minuty, hodiny...
