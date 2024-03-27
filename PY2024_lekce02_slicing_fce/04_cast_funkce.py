# vlastni funkce

# def - definovani vlastni fce, jeji jmeno, zde Pozdrav, 
# fce maji za sebou vzdy () a : - odsadi se 
# co ma fce udelat 
# vyvolani funkce - zde ř. 13
# vzdy definovat nahore scriptu, ne v prubehu (pro prehlednost) 
# jmeno fce podle toho, co realne děla 

def pozdrav():               # zakladni syntax def + jmeno definice + () + :
    print("Ahoj!")           # kazda fce musi mit min 1 radek - tj, aspon print, kdyz ho dam ale spustit, nic se nestane

pozdrav()                    # fci musim zavolat (jmenem)


# rozsireni o parametry - pridavaji se do () - jako je print(argument) - zde je argumentem "jmeno"
def pozdrav(jmeno):
    print(f"Ahoj {jmeno}")

pozdrav("Kájo")          # python bude brat Kájo jako jmeno - pt je v definici v ř. 17

# fce na soucet 2 cisel
def soucet_cisel(a, b):       # soucet - tj 2 argumenty scitam neco (zde a) s necim (zde b)
    return a + b              # RETURN (musi byt !!!) - vrati nejakou operaci, zde soucet; zároven definici fce končí /vše za ním už nevezme do vypoctu
                              # kdybych dala jen print, probehne alevysledek se nikam neulozi !! proto RETURN, TEN MUZU ULOZIT DO PROMENNE

vysledek = soucet_cisel(2, 9)   # ulozit do promenne, abych s vysledkem pak mohla dal pracovat 
print(vysledek)

# doposud ČISTÁ FUNKCE bez vstupu (vše obsaženo v definici, nic nenčítá zvenku), vždy stejný výsledek !!!

# vs. fce s globální pormennou - promenna mimo definici, beze ji "zvenku" - v závislosi na hodnotě proměnné vždy jiný výsledek

smenny_kurz = 25

def smena_na_KC(EUR):
    return EUR* smenny_kurz    # nyní pracuje s promennou smenny kurz, s kterym primo nepracuje, ale vytahne si ji 

print(smena_na_KC(2))

# prepis na cistou fci: obecne snaha co nejvic psat cistou fci (netahat veci z venku)
def smena_na_KC(EUR, kurz):
    return EUR * kurz

print(smena_na_KC(2, 25))


# PASS - chci definovat fci, ale jeste presne nevim, co bude delat

def jeste_presne_nevim(vstup1, vstup2):
    pass      # ulozi, python nebude prudit a hazet errro, ze neni dokoncena definice 
              # až budu vedet, smazu pass a fci dodefinuju


# nepovinne parametry fce - to, ze parametr nepovinny reknu ze v argumentu bude = (rovná se)
def pozdrav(jmeno):  # bude ocekavat, ze ve volani vfce vlozim do zavorky jmeno, kdy ho nenapisu, bude brecet
    pass
def pozdrav(jmeno = "defaultni nastaveni"): # kdyz nezadam jmeno, nevypise nic a nebude mu to vadit 
    pass