# moznost "lehka" ale otravna na opravovani chyb - 
# file = open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\mereni.txt", encoding = "utf-8")
#print(file.read())

# nutno pridat "r"  + encoding
# v teto moznosti jsem ho pouze otevreli a precetli, ale nezavreli > proto tuto cestu NEDELAT!
# misto toho pouzivat kontext - soubor otevre pouze po dobu kontextu a pak ho zavre

# delat takto s kontextem:
# with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\mereni.txt", encoding = "utf-8") as file:
#    text = file.read()

# print(text)    #nyni ulozeno jen do terminalu > potrebuju prevest nekam a ulozit - zalozit prazdny seznam
# moznost A (pouziti for cyklu)
lines = []

with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\mereni.txt", encoding = "utf-8") as file:
    for line in file:
        lines.append(line)
print(lines)

# moznost B
with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\mereni.txt", encoding = "utf-8") as file:
    text = file.readlines()
print(text)

# rozdeleni seznamu podle tabulatoru
output = []
with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\mereni.txt", encoding = "utf-8") as file:
    for line in file:
        day, temp = line.split('\t')       # /t = tabulator, /n = novy radek , moje nove promenne day a temp  rozdeli podle \t
        output.append([day, float(temp)])  # temp prevede na float, a spolu s day ulozi do prazdneho seznamu output 
print(output)
