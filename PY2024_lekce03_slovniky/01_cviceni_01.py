# Napiš funkci mult, která bude mít dva číselné parametry. 
# Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):           # a, b = parametry 
    return a * b

print(mult(2, 3))

def dev(a, b):            # zohlednit, že závisí na pořadí parametrů 
    if b == 0:
        print("chyba")
    else:
        return a/b

print(dev(10, 2))        # bude fungovat
print(dev(10, 0))        # kyz neni return u vetve IF, vypise Chyba (splneni vetve IF), a None (= vysledek returnu)

# kdyz jsou 2 parametry v 1. řádku definice, bude matchovat 1. parametr k 1. hodnote v argumentu
# je-li vice parametru: lze v printu definovat: print(dev(b=10, a=2)) - uvest vzdy kdyz volam fci !!!

print("---")
# nastaveni fce, aby vracela 2 argumenty:
def dev(a, b):
    if b == 0:
        print("Chyba)")
    else:
        int_part = a//b     # celocislne deleni
        r = a % b           # zbytek po deleni
        return int_part, r 
 
result = (dev(10, 3))               # vypise vysledek 2 parametry do () - jmenuje se to n-tice
print(result)                       # rozbaleni pro pripadnou potrebu s kazdym vysledkem pracovat zvlast > 
                                     # > ulozit kazdy parametr do samostatne promenne (ř. 33-35)
int_part, r = dev(10, 3)
print(int_part)
print(r)

