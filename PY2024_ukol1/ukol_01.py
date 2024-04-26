

class Item:
    def __init__(self, name, price):
        self.name = name      # str
        self.price = price    # float
    
    def __str__(self):
        return f"{self.name}: {self.price} Kč."

class Pizza(Item):
    def __init__(self, name, price,ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients      # dict {ingredint : vaha v g}

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if self.ingredients[ingredient] > 0: 
            total_pizza_price = super().price + (quantity * price_per_ingredient)
            return total_pizza_price
        else: 
            total_pizza_price = super().price
            return total_pizza_price
    
    def __str__(self):
        return f"Pizza {self.name} s extra ingrediencemi ({ingredient}) stojí {total_pizza_price} Kč." 
    
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)


