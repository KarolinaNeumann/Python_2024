# jine vyuziti slovniku - zjistit unikatnich prvku
my_list = [1, 2, 2, 3, 1, 2]

# moznost prevest na mnozinu(set)
print(set(my_list))                # vypise jedinecne prvky, ztratim ale jejich cetnosti

# { prvek my_list : pocet }
elements = {}                      # vytvroti novy seznam - klice budou unikatni hodntoty, cetnost bude hodnota 
for number in my_list:             # number - moje pomocná proměnná (může se jemnovat libovolně) 

# logika: nejprve vetev else: pokud jsem cislo jeste nevidela, zapise ho do seznamu (vychozí četnost = 1), 
# pak vetev IF: pokud jsem uz cislo videla, pričte cetnost
    if number in elements:
    # Jestli jsme uz ten prvek videli, 
    # zvysujeme jeho pocet
        elements[number] += 1
    # Kdyz je to neco noveho,
    # tak to pridame do slovniku 
    else:
        elements[number] = 1

print(elements)