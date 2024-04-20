# Balík 1

# A
# Uvažuj, že navrhuješ software pro zásilkovou společnost.
# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. 
# Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.

class Package:
    def __init__(self, 
                 weight,
                 address, 
                 state):
        
        self.address = address
        self.weight = weight
        self.state = state
        print("Package created")

# B 
# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. 
# Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".

# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. 
# U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.

    def get_info(self):
       print(f"Balík na adresu {self.address}, má hmotnost {self.weight} kg je ve stavu {self.state}") 

# C 
# Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. 
# Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg 
# do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.


    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359

# ad B 
balik_1 = Package(address="AAA", weight=5, state="in transit")
print(balik_1.weight)
balik_1.get_info()

balik_2 = Package(address="BBB", weight=15, state="delivered")
balik_2.get_info()

balik_3 = Package(address="BBB", weight=25, state="delivered")
balik_3.get_info()

# ad C 
print(balik_1.delivery_price())
print(balik_2.delivery_price())
print(balik_3.delivery_price())

# Neni dobry napad, ale jde to
# lepsi to nastavit v metode (self.cena = ...)
balik_1.cena = balik_1.delivery_price()