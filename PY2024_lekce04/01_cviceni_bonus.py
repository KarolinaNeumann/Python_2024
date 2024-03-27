# jine vyuziti slovniku - zjistit unikatnich prvku
my_list = [1, 2, 2, 3, 1, 2]

# moznost prevest na mnozinu(set)
print(set(my_list))                # vypise jedinecne prvky, ztratim ale jejich cetnosti

# { prvek my_list : pocet }
elements = {}                      # vytvroti novy seznam klice budou unikatni hodntoty, cetnost bude hodnota 
for number in my_list:             
    if number in elements:
        

# logika: nejprve vetev else: pokud jsem cislo jeste nevidela, zapise ho do seznamu, pak vetev IF: 
# pokud jsem uz cislo videla, zapise cetnost
    
