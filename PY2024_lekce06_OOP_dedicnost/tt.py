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
        
class ValuablePackage(Package):
    def __init__(self, 
                 weight,
                 address, 
                 state,
                 value):
        
        super().__init__(weight,
                         address, 
                         state)
        self.value = value
    
    def __str__(self):
        return super().__str__() + f" cena: {self.value}"
    
    def delivery_price(self):
        return super().delivery_price() + 0.05*self.value
    

balik_1 = Package(weight=1, address="A", state="in transit")
print(balik_1)
print(balik_1.delivery_price())

balik_2 = ValuablePackage(weight=2, address="B", state="delivered", value=1000)
print(balik_2)
print(balik_2.delivery_price())