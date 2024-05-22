#vek = input("Zadej vek: ")
#if vek > 15
#print("Vitej!")


# pristup 1 (testovat a pak spustit)
import sys # knihovna sys

vek = input("Zadej Vek:")
if not vek.isdigit():              # .isdigit = oveří zda je zadana cislice 
    print("Musis tam dat cislo")
    exit()                         # ukončí program

vek = int(vek)
if vek > 15:
    print("Vitej")
else: 
    print("nemáš tu co dělat")


# pristup 2  (vyzkouset TRY + co se ma stat, pou dojde k chybe EXCEPT)
# vzdy spolu TRY + EXCEPT (jako if a lese)
try:
    vek = input("Zadej Vek:")
    vek = int(vek)
    if vek > 15:
        print("Vitej")
    else: 
        print("nemáš tu co dělat")
except ValueError: 
    print("zadej číslici")

# možnost nastaveni oapkovani - while loop
while True:  # pojede dokud nenarazi na break
    try:
        vek = input("Zadej Vek:")
        vek = int(vek)
        if vek > 15:
            print("Vitej")
            break                          # ukončí loop
        else: 
            print("nemáš tu co dělat")
            break                          # ukončí loop
    except ValueError: 
        print("zadej číslici")

