# dědičnost 

class Employee:                           # psát velké písmeno         
    def __init__(self, name, position):   # definování třídy, init 
        self.name = name
        self.position = position 

    def __str__(self):                    # instance = objekt 
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
# instance = Jmenotridy("prvni atribut", "druhy atribut")  

frantisek = Employee("František", "prodavač")
jitka = Employee ("Jitka", "administratorka" )

print(frantisek)
print(jitka)

# pridani dalsiho objektu/pracovniku např. manager, který má ale i dalsi atributy 
# moznost: vytvrot novou tridu NEBO využiju dedičnost - copy/paste puvodni tridy employee

# vytvoreni nove tridy manager, co se bude dedit z employee:
# class Manager(Employee):
#    def __init__(self, name, position, subordinates, car):
#       self.name = name
#       self.position = position
#       self.subordinates = subordinates
#       self.car = car

# janina = Manager("Janina", "reditelka kurzu", 55, "Tesla")
# print(janina)     # pokud neni definovano __str__, prejme trida Manager vse od Eployee > nevypise podrizenen a auto
                    # vypise tvar z Employee: "janina pracuje na pozici manazerka kurzu"

# vyuziti dedicnost - metoda super() říká odkud si má brát.(tečka) a co si má brát (za tečkou)
class Manager(Employee):
    def __init__(self, name, position, subordinates, car):
        super().__init__(name, position)       # SUPER()= zkopiruj z Employee (ř. 30)
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
		# buď napíšu vlastní řetězec pro Managera, nebo použiju SUPER()
        return super().__str__()+ f" Má {self.subordinates} podřízených a řídí auto {self.car}."

janina = Manager("Janina","reditelka kurzu", 55, "Tesla")
print(janina)

