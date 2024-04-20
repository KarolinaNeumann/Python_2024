# balik podruhe

# Vrať se k návrhu software pro zásilkovou společnost.

class Package:
    def __init__(self, 
                 weight,
                 address, 
                 state):
        
        self.address = address
        self.weight = weight
        self.state = state
        print("Package created")

# U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, 
# jestli nyní stačí k získání informací o balíku funkce print().

# Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku
# a zaznamená tak jeho doručení. = PŘIDÁVÁM POD Ř. 32

# Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. 
# Pokud ano, metoda vrátí zprávu "Balík již byl doručen". Tím bude řidič (řidička) informován(a) o tom, 
# že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. 
# Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".

# Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?

    # def get_info(self):
    #   print(f"Balík na adresu {self.address}, má hmotnost {self.weight} kg je ve stavu {self.state}") 
    def __str__(self):
       return f"Balík na adresu {self.address}, má hmotnost {self.weight} kg je ve stavu {self.state}"
    
    def delivery_price(self):                      # puvodni- viz cviceni cast 1 
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359
        
    def deliver(self):                             # nove 
        if self.state == "delivered":
            print("Balík již byl doručen")
        else:
            self.state = "delivered"
            print("Doručení uloženo")

balik_1 = Package(address="AAA", weight=5, state="in transit")
balik_2 = Package(address="BBB", weight=15, state="delivered")
balik_3 = Package(address="BBB", weight=25, state="delivered")

print(balik_1)
print(balik_2)

balik_1.deliver()
print(balik_1)

balik_1.deliver()
print(balik_1)

balik_2.deliver()
print(balik_2)

