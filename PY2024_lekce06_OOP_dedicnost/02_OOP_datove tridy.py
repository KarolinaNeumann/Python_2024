# datove tridy (dataclasses)

# novinka od verze 3.07 - boilerplate code
# díky nim nemusím opakovaně vypisovat stejné kusy kódu
# nutný na začátku import dataclass (píšu vždy úplně jako první) from dataclasses import dataclass
# (jen jednou pro celý soubor .py)
# před definicí každé třídy uvádět dekorátor @dataclass

# výchozí definice - viz cast 1 > přepis na dataclasses 
# class Employee:                                
#   def __init__(self, name, position):   
#       self.name = name
#        self.position = position 

#    def __str__(self):                   
#         return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
# class Manager(Employee):
#     def __init__(self, name, position, subordinates, car):
#       super().__init__(name, position)       
#       self.subordinates = subordinates
#       self.car = car

#     def __str__(self):
#       return super().__str__()+ f" Má {self.subordinates} podřízených a řídí auto {self.car}."   

# frantisek = Employee("František", "prodavač")
# print(frantisek)

# janina = Manager("Janina","reditelka kurzu", 55, "Tesla")
# print(janina)

# přepis na dataclasses
from dataclasses import dataclass             
@dataclass  
class Employee:
    name:  str      # anotovani datoveho typu = napovedeni pythonovi jaky datovy typ ma ocekavat 
    position: str   # (on ho sam o sobe nekontorluje)
    
    def __str__(self):  
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

denisa = ("Denisa", "programátorka")
print(denisa)

@dataclass
class Manager:
    subordinates: int    # datový typ inteager (počet podřízených)
    car: str
    holiday: Optional[int] = None  # Počet dnů dovolené, volitelný atribut s výchozí hodnotou None

    def __str__(self):   # zůstává stejné
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
    def __str__(self):
        return super().__str__()+ f" Má {self.subordinates} podřízených a řídí auto {self.car}."   

olga = ("Olga", 55, "Tesla")
print(olga)

# Funkce pro práci s objekty

# funkce isinstance() – kontrola, zda je nějaká fce objektem určité třídy/jejích potomků, vrací True/False 
print(isinstance(olga, Manager))   # True – z příkladu výše: Olga je objektem třídy Manager
print(isinstance(olga, Employee))   # True – ptž třída Manager dědí od Employee

# funkce hasattr() - kontrola, zda má nějaký objekt atribut nebo metodu daného jména, vrátí True/False
print(hasatrr(olga,"car"))    # True = Olga má auto (atribut car je ve třídě manager)

# funkce getattr() – umožňuje získat hodnotu atributu objektu na základě jeho názvu. 
# Pokud funkci zadáme dva parametry (objekt a název atributu), funguje jako tečková notace,
# tj. vrátí hodnotu požadovaného atributu (pokud ji má) nebo spustí chybu AttributeError (pokud objekt atribut nemá). 
# využití: název atributu známe až za běhu programu a nemůžeme jej proto přímo zapsat do kódu (umožnění psát obecnější a opakovaně použitelný kód)
#     př. print(getattr(olga, "car"))      # vypíše Tesla
#         print(denisa, "car")            # vypíše Attribute error: Employee objekt (= Denisa) has no attr “car“


# nepovinné parametry (obdoba jako funkcí) ř. 50
# pokud chci, aby byl parametr=atribut nepovinný, zadám mu = (rovná se) + defaultní hodnotu (None)    
# zápis atributu: holiday: Optional[int] = None  

