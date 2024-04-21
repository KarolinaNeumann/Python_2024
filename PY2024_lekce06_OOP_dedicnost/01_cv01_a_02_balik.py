# cenný balík

# pokračoování balík (viz minulá lekce) - rozpracovávám původní zadání: 

class Package:
    def __init__(self, 
                 weight,
                 address, 
                 state):
        
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
       return f"Balík na adresu {self.address}, má hmotnost {self.weight} kg je ve stavu {self.state}"

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359

# nové zadání: dědičnost

# Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

# Vytvoř třídu ValuablePackage, která dědí od třídy Package. 
# ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
# Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
# Přidej do výpisu informací o cenném balíku (metoda __str__) informaci o ceně balíku.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí. 
# Současně si vytvoř "obyčejný" balík o zkontroluj, že u něj se nic nezměnilo.
 
class ValuablePackage(Package):
    def __init__(self, 
                 weight, 
                 address,
                 state,
                 value):
        super().__init__(weight,      # přejímá od nadřazení třídy atributy ze závorky
                         address, 
                         state)
        self.value = value            # tento atribut je "navíc" oprati třídě Package

    def __str__(self):
        return super().__str__() + f", cena: {self.value}"     # bere ze řádku 15

    def delivery_price(self):
        return super().delivery_price() + 0.05 * self.value  # bere ze řádku 18

balik_1 = Package(weight=1, address="A", state="in transit")
print(balik_1)
print(balik_1.delivery_price())

balik_2 = ValuablePackage(weight=2, address="B", state="delivered", value=1000)
print(balik_2)
print(balik_2.delivery_price())