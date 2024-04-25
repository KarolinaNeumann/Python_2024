# Rozvoz pizzy

from dataclasses import dataclass      

@dataclass  
class Item:
    name:  str      
    price: float   
    
    def __str__(self):
        return f"{self.name}: {self.price} Kč."

@dataclass
class Pizza(Item):
    ingredients: dict   # ingredience: vaha (g)

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if ingredients[ingredient] > 0: 
            total_pizza_price = super().price + (quantity * price_per_ingredient)
            return total_pizza_price
        else: 
            total_pizza_price = super().price
            return total_pizza_price

    def __str__(self):
        return f"Pizza {self.name} s extra ingrediencemi ({ingredient}) stojí {self.total_pizza_price} Kč." 
    
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)