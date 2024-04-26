# Rozvoz pizzy

from dataclasses import dataclass, field  
from typing import Dict   

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
