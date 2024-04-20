# rozšíření původni definice tridy o atribut k vypoctu dovolene 
class Employee:                
    def __init__(self, name, position, holiday_entitlement):     
        self.name = name                                          
        self.position = position
        self.holiday_entitlement = holiday_entitlement

#   def get_info(self):
#      return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

# namísto get info již připravená fce __str__(self): v kombinaci s printem objektu vypise to, co ma return (a nemusim psat metodu)
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
# pridani nove metody na pocitani dovolene  
    def take_holiday(self, days):  
        if self.holiday_entitlement >= days:           # odkazování přes self. !
            self.holiday_entitlement -= days           # operator -= aktualizuje a odečte days od porměnné holiday_entitlement
            return f"Užij si to"
        else:
            return f"Bohužel už nemáš nárok, zbývá ti jen {self.holiday_entitlement} dní dovolené."
    
frantisek = Employee("František", "prodavac", 9)           
# print(frantisek.get_info())   # uprava get info na ř. 8 na __str__
print(frantisek)                # vztahuje se ke __str__

jitka = Employee("Jitka", "administratorka", 25)
# print(jitka.get_info())
print(jitka)

# zavolani nove fce na pocitani dovolene s argumentem:
print(frantisek.take_holiday(5))
print(frantisek.take_holiday(35))

# uprava get info na ř. 8 - pro vypis hodnot BEZ pouzivani metod > __STR__: