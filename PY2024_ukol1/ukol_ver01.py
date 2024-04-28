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

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        self.ingredients[ingredient] = quantity
        self.price = self.price + (quantity * 0.1 * price_per_ingredient)
        return self.price
      
    def __str__(self):
        return f"Pizza " + super().__str__() 

margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
print(margarita)
print(margarita.add_extra("olivy", 50, 10))

@dataclass
class Drink(Item):
    volume: int    # objem napoje (ml)

    def __str__(self):
        return f"Nápoj " + super().__str__() + f" (objem nápoje je {self.volume} ml)"


cola = Drink("Cola", 1.5, 500)
print(cola)

@dataclass
class Order:
    customer_name: str                    # Jméno zákazníka
    delivery_address: str                 # Adresa doručení 
    items: List[Item]                     # Seznam položek v objednávce
    status: str = "Nová objednávka"       # Stav objednávky 

    def mark_delivered(self):
        self.status = "Doručena"

    def __str__(self):
        return f"{self.status} pro {self.customer_name} s adresou doručení {self.delivery_address} obsahuje: {self.items}."
    
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

@dataclass
class DeliveryPerson:
    name: str                       # Jméno doručovatele 
    phone_number: str               # Telefonní číslo doručovatele
    available: bool = True          # Dostupnost doručovatele 
    current_order: Order = None     # Aktuální objednávka k doručení (Order).

    def assign_order(self, order):
        if self.available:
            self.current_order = order
            self.status = "Na cestě"
            self.available = False
            print(f"Vaši objednávku zajistí doručovatel {self.name}.")
        else:
            print("Doručovatel není dostupný")

    def complete_delivery(self):
        if self.current_order:
            self.current_order.status = "Úspěšně doručeno"
            print(f"Vaší objednávku doručil: {self.name}.")
            self.available = True
            self.current_order = None     
        else:
            print("Aktuálně doručovatel nemá nic k doručení.")

    def __str__(self):
        if self.available:
            self.status = "dostupný"
        else:
            self.status = "nedostupný"
        return f"Doručovatel {self.name}, tel. číslo: {self.phone_number} je: {self.status}"

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person) 

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)