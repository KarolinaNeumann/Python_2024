class Employee:                           # psát velké písmeno         
    def __init__(self, name, position):   # definování třídy, init 
        self.name = name
        self.position = position 

    def __str__(self):                    # instance = objekt 
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

class Manager(Employee):
    def __init__(self, name, position, subordinates, car):
        #super().__init__(name, position)       # SUPER()= zkopiruj z Employee (ř. 30)
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
		# buď napíšu vlastní řetězec pro Managera, nebo použiju SUPER()
        return super().__str__()+ f" Má {self.subordinates} podřízených a řídí auto {self.car}."

janina = Manager("Janina","reditelka kurzu", 55, "Tesla")
print(janina)