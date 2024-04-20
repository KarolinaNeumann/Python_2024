# kniha podruhe

# Vrať se k práci se třídou Book.
# U knihy budeme chtít evidovat, kolik kusů bylo prodáno. 
# Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__(). 
# Dále přidej atribut costs, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).

class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs

    def __str__(self):
        return f"Kniha: {self.title}, Počet stran: {self.pages}, Cena: {self.price} Kč."
    
# Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).

    def profit(self):
        return (self.price - self.costs) * self.sold 

# Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". 
# Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".

    def rating(self):
        zisk = self.profit()
        if zisk < 50_000:
            return "propadák"
        elif zisk <= 500_000:
            return "průměr"
        else:
            return "bestseller"

# Příklady vytvoření a použití objektů třídy Book
book1 = Book("Python Programování", 300, 450, sold=200, costs=200)
book2 = Book("Pokročilé Algoritmy", 550, 650, sold=1500, costs=250)

print(book1)
print(f"Zisk z knihy '{book1.title}': {book1.profit()} Kč")
print(f"Hodnocení knihy '{book1.title}': {book1.rating()}")

print(book2)
print(f"Zisk z knihy '{book2.title}': {book2.profit()} Kč")
print(f"Hodnocení knihy '{book2.title}': {book2.rating()}")