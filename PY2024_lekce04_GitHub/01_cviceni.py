# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. 
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

# A. Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# B. Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]


# pocet prectenych knih
# var 1
print(len(books))

# var 2
num_books = 0
for book in books:
    num_books += 1

# ad A - celkovy pocet prectenych hstran
num_pages = 0
for book in books:
    num_pages += book["pages"]
print(num_pages)

# ad A - bonus spocti prumer stranek 1 knihy
print(num_pages / num_books)

# ad A - bonus spocti ktera kniha ma nejvic stran
# pomoci cyklu - nejdriv definovat zacatek a pak porovnavat s kazdym dalsim zaznamem 

max_num_pages = 0                            # definovat začátek - maximum = 0
for book in books:                
   if book["pages"] > max_num_pages:         # je-li pocet stran v dane knizce vyšší, než max
       max_num_pages = book["pages"]         # pak je tato kniha maximum
print(max_num_pages)

# ad A - bonus spocti, ktera kniha ma nejmin stran

min_num_pages = 100000                       # záměrně vysoké, aby porovnávání dávalo smysl
min_num_pages = books[0]["pages"]            # NEBO uložit počet stran 1. knihy a s ní porovnávat
for book in books:
   if book["pages"] < min_num_pages:
       min_num_pages = book["pages"]
print(min_num_pages)

# ad B
pocet_knih_s_vysokym_hodnocenim = 0
for book in books:
    if book["rating"] >= 8:
        pocet_knih_s_vysokym_hodnocenim += 1
print("Počet knih s hodnocením alespoň 8:", pocet_knih_s_vysokym_hodnocenim)
