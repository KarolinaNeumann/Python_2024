# Rozvoz pizzy

from dataclasses import dataclass      

@dataclass  
class Item:
    name:  str      
    price: float   
    
    def __str__(self):
        return f"{self.name}: {self.price} Kč."

@dataclass
class Pizza:
    ingredients: dict   # ingredience: vaha (g)
    
    def add_extra(self, ingredient, quantity, price_per_ingredient):
        return 
    
    def __str__(self):
        return 