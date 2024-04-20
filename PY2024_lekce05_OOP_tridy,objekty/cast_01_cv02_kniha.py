# kniha

# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. 
# Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

# Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.

    def get_info(self):
        return f"Kniha: {self.title}, Počet stran: {self.pages}, Cena: {self.price} Kč."

# Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. 
# S využitím atributu pages vypočítej čas na přečtení knihy. Metoda bude mít nepovinný parametr, 
# který udává počet minut potřebných pro přečtení jedné stránky knihy. (aby byl parmetr nepovinný, dám za něj v definici znak = rovná se)
# Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. 
# Výchozí hodnota nepovinného parametru je 4. 

    def get_time_to_read(self, minutes_per_page=4):
        total_minutes = self.pages * minutes_per_page
        hours = total_minutes // 60                                        # celočíselné dělení 
        minutes = total_minutes % 60                                       # zbytek po celočíselném dělení 
        return f"Čas potřebný na přečtení: {hours} hodin a {minutes} minut."

# Příklady použití
book1 = Book("Python Programování", 250, 399)
book2 = Book("Pokročilé Algoritmy", 500, 799)

print(book1.get_info())
print(book1.get_time_to_read())

print(book2.get_info())
print(book2.get_time_to_read(5))  # Předpokládáme, že čtenář potřebuje 5 minut na stránku