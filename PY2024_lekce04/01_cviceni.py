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


# pocet knih
# var 1
print(len(books))

# var 2
num_books = 0
for book in books:
    num_books += 1

# ad A 
num_pages = 0
for book in books:
    num_pages += book["pages"]
print(num_pages)

# ad A - bonus spocti prumer stranek 1 knihy
print(num_pages / num_books)

# ad A - bonus spocti ktera kniha ma nejvic stran
# pomoci cyklu - nejdriv definovat zacatek a pak porovnavat s kazdym dalsim zaznamem 

max_num_pages = 0
for book in books:
   if book["pages"] > max_num_pages:
       max_num_pages = book["pages"]
print(max_num_pages)

# ad A - bonus spoti ktera kniha ma nejmin stran
# pomoci cyklu - zde musim zacatek dat vysoky, aby davalo smysl porovnavani
min_num_pages = 100000
min_num_pages = books[0]["pages"]
for book in books:
   if book["pages"] < min_num_pages:
       min_num_pages = book["pages"]
print(min_num_pages)

# ad B
num_good_books = 0
#DOPLNIT
