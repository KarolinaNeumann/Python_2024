class Employee:                           # psát velké písmeno         
    def __init__(self, name, position):   # definování třídy, init 
        self.name = name
        self.position = position 

    def __str__(self):                     # instance = objekt 
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
instance = Jmenotridy("prvni atribut", "druhy atribut")

# frantisek = 
# jitka = Employee ("Jitka", )

# pridani dalsiho objektu/pracovniku např. manager, který ma ale i dalsi atributy 
# moznost: vytvrot novou tridu NEBO využiju dedičnost - copy/paste puvodni tridy employee

# vytvoreni nove tridy manager, co se bude dedit z employee:
# class Manager(Employee):
#    def __init__(self, name, position, subordinates, car):
#        self.name = name
#       self.position = position
#       self.subordinates = subordinates
#        self.car = car

# janina = Manager("Janina", "reditelka kurzu", 55, "Tesla")
# print(janina)       # pokud neni definovano __str__, prejme trida MAnager vse od Eployee > nevypise podrizenen a auto
                    # vypise tvar z Employee: "janina pracuje na pozici manazerka kurzu"

# vyuziti dedicnost: 
class Manager(Employee):
    def __init__(self, name, position, subordinates, car):
        super().__init__(name, position)       # SUPER = zkopiruj z Employee (ř. 30)
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
        return super



