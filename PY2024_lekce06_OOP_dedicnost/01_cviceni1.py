#
# U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, 
#jestli nyní stačí k získání informací o balíku funkce print().

# Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku 
#a zaznamená tak jeho doručení. Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. 
# že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. 
# Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
# Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?


class Package:
    def __init__(self, 
                 weight,
                 address, 
                 state):
        
        self.address = address
        self.weight = weight
        self.state = state
        print("Package created")

    def __str__(self):
       return f"Balík na adresu {self.address}, má hmotnost {self.weight} kg je ve stavu {self.state}"

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359

# biz horni text z minula
#dedicnost: nové 

class ValuablePackage(Package):
    def __init__(self, 
                 weight, 
                 adress,
                 state,
                 value):
        super().__init__(weight, 
                         adress, 
                         state)
        self.value = value
        
    def __str__(self):
        super().__str__() + f"cena: {self.value}"

# vychozi z minula

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359
        
    def deliver(self):
        if self.state == "delivered":
            print("Balík již byl doručen")
        else:
            self.state = "delivered"

balik_1 = Package(weight = 1, adress = "A", state = "in transit")
print(balik_1)

balik_2 = ValuablePackage(weight = 2, adress = "B", state = "delivered", value = 1000)
print(balik_2)