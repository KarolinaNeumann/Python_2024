# Rozvoz pizzy

from dataclasses import dataclass, field  
from typing import Dict 
from typing import List  

@dataclass  
class Item:
    name:  str      
    price: float   
    
    def __str__(self):
        return f"{self.name}: {self.price} Kč"

@dataclass
class Pizza(Item):
    ingredients: Dict[str, int] = field(default_factory=dict)  # slovník = {ingredience: vaha}

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        if quantity > 0:
            total_pizza_price = super().price + (quantity * price_per_ingredient)
            return total_pizza_price
        else: 
            total_pizza_price = super().price
            return total_pizza_price
        
    def __str__(self):
        return f"Pizza {self.name} s extra ingrediencemi:{self.ingredient} stojí {total_pizza_price} Kč."

margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)       
print(margarita)


@dataclass
class Drink(Item):
    volume: int    # objem napoje (ml)

    def __str__(self):
        return f"Nápoj " + super().__str__() + f" (objem nápoje je {self.volume} ml)"


@dataclass
class Order:
    customer_name: str                    # Jméno zákazníka
    delivery_address: str                 # Adresa doručení 
    items: List[Item]                     # Seznam položek v objednávce
    status: str = "Nová objednávka"       # Stav objednávky 

    def mark_delivered(self):
        self.status = "Doručeno"

    def __str__(self):
        return f"Objednávka pro {self.customer_name} s adresou doručení {self.delivery_address} je {self.status}. Doručeno bylo: {self.items}."
    

@dataclass
class DeliveryPerson:
    