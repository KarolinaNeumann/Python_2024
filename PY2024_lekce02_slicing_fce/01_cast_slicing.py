# seznamy slicing - dostat se ke konkrtetnimu datu
# indexovani od 0 - pocet kroku od zacatku !!!
venecky = [1, 2, 4, 1, 6, 0, 1]
print(venecky[0])   # zaznam z prvni pozice, tj. 1

venecky[0] = 3      # oprava zaznamu na indexu 0 (tj. 1 se zmeni na  3)
print(venecky)

print(venecky[0:5])  # vypis prvnich 5 prvku - tj. od indexu 0 - 4 (5 je vnější závora !!!)
print(venecky[:5])   # stejny zapis jako ř. 8
print(venecky[5:])   # vypis od indexu 5 (tj. 6. cislo) až do konce 
print(venecky[::2])  # vypis kazdeho 2. prvku od zacatku do konce 3. PARAMETR VYPIŠE OB 2 (tj. KAŽDÝ DRUHÝ)
print(venecky[1:5:2]) # vvpis kazdeho druhoho prvku od 2. do 5. prvku (tj. index 1 a 4)

print(len(venecky))  # vypise pocet zaznamu v seznamu
print(sum(venecky))  # vypise soucet hodnot v seznamu
print(min(venecky))  # vypise nejmensi hodnotu v seznamu
print(max(venecky))  # vypise nejvetsi hodnotu v seznamu
print(sorted(venecky))  # seradi hodnoty v seznamu od nejmensiho po nejvetsi
print(sorted(venecky, reverse = True))  # seradi hodnoty v seznamu od nejvetsi po nejmensi, potreba opravit defaultni nastaveni reverse z false na true (kouknout pripadne na oficialni dokumnetaci pythonu)

retezec = "Mate radsi moře nebo hory"
# obdobne fce vit ř.12 - 17, nejde sum :)
print(len(retezec))  # vypise pocet zaznamu v seznamu
print(sum(retezec))  # vypise soucet hodnot v seznamu
print(min(retezec))  # výpis znaku s nejnižší hodnotou v ASCII tabulce v řetězci
print(max(retezec))  # výpis znaku s nejvyšší hodnotou v ASCII tabulce v řetězci
print(sorted(retezec))  # seradi hodnoty v seznamu od nejmensiho po nejvetsi
print(sorted(retezec, reverse = True)) # 2. parametr mění dafultní nastavení na SESTUPNÉ řazení viz ř. 20

# IN, NOT IN seznam
inzerat = "Na pracovni pozici se pouziva Python"
if "Python" in inzerat:
    print("Beru to!")

inzerat = "Na pracovni pozici se pouziva R"
if "Python" not in inzerat:
    print("Neberu to!")
