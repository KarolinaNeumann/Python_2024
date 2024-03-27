# slovniky (dictionary)
# pojme vice pormennych ruznych typu, indexace > snadny pristup
# ulozeni v {}
# klice v ""
# oddeleni klice (keys) od hodnoty (values) dvojteckou
# oddeleni dalsich radku carkou

# vytvoreni prázdneho slovniku
slovnik = {}
print(type(slovnik))        # vypise dict = dictionary

# chci ulozit slovnik s nazvem item (klic: hodnota)
# title = cajova konvice
# price = 899
# in_stock = True

item = {"title": "Cajova konvice",     
        "price": 899,
        "in_stock": True
        }

print(item["title"])     # vypis hodnoty klice title

item["weight"] = 0.5     # prida novy klic weight s hodnotou 0.5 do slovniku
print(item)              # vypise slovnik obohaceny o dalsi klic weight

item["weight"] = 1       # pokud jiz klic ve slovniku je, opravi hodnotu na tuto novou
print(item)              # vypise slovnik s navysenou hodnotou klice weight 

