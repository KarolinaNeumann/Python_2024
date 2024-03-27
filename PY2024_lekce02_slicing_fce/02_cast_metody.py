retezec = "Python"

# print(upper(retezec)) tato vy byla zapsana funkce!
# VOLÁNÍ POMOCÍ TEČKOVÉ NOTACE jmeno_retezce.upper() - zde metoda upper + vždy prázdné () !!!

# upper / lower
print(retezec.upper())   # zvetsi pisena na hulkove
print(retezec.lower())   # zmensi hulkove pismo na male

# strip
retezec = "   Python   "
print(retezec)
print(retezec.strip)  # odebere z retezce vsechny bile znaky, tj. mezery, entery, tabulatory

# split
print("aa bb cc dd ee".split(" "))    # rozdeli retezec podle zvoleneho separatoru v uvozovkach, zde mezera)

# join
retezec = ["1", "2", "3", "4"]
print("+".join(retezec))              # spoji jednotlive znaky zvolenym separatorem, zde +

# replace(old, new) : nahradí v řetězci výskyty old za new
text = "Kurz vede lektor Marek"
novy_text = text.replace("Marek", "Martin")
print(novy_text)  # "Kurz vede lektor Martin".
