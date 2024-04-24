# 1. Inicializace projektu
# Vytvořte nový Python soubor (např. task_manager.py).
# Na začátek souboru přidejte import potřebného modulu datetime, který bude využit pro 
# přidávání časových razítek k úkolům.

import datetime

# 2. Definice třídy Task
# Definujte třídu Task, která bude reprezentovat jednotlivé úkoly.
# Třída bude mít konstruktor __init__, který přijímá jeden parametr description (popis úkolu).
# V konstruktoru nastavte atributy description a timestamp. 
# Atribut timestamp bude automaticky nastaven na aktuální datum a čas.

class Task():
    def __init__(self, description):         
        self.description = description    
        self.timestamp = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    def __str__(self):
        return f"Task: {self.description}, time created: {self.timestamp}"

task_1 = Task("A")
print(task_1)
task_2 = Task("B")
print(task_2)

# 3. Vytvoření datové struktury pro ukládání úkolů
# Použijte slovník tasks pro ukládání úkolů, kde klíče budou jedinečná ID úkolů 
# a hodnoty budou instance třídy Task.

tasks = {}


# 4. Implementace funkcí pro manipulaci s úkoly
# add_task(description): Funkce pro přidání nového úkolu. Generuje unikátní ID pro každý úkol, 
# přidává úkol do slovníku a vypisuje informaci o přidání.

def add_task(description):
    
    
    


# remove_task(task_id): Funkce pro odstranění úkolu. Kontroluje, zda úkol s daným ID existuje,
# a pokud ano, odstraní ho.

def remove_task(task_id):
    pass

# show_tasks(): Funkce pro zobrazení všech aktuálně uložených úkolů společně s jejich
# popisem a časem přidání.

def show_tasks():
    pass