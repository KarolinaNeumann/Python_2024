# soukromé atributy 
# - nevyhoda pythonu, že neumí uzamknout nastavení atributu na private/public
# - pokud chci, aby nikdo nezasahoval a natrvdo neopravoval hodnotu atribudu, do jeho nazvu dat podrztzitko (př. _adress)
# - python sice realne zmnenu pusti, ale programator ma toto proavidlo ctit
# - oprava natvrdo = oprava mimo definici objektu skrze zavolani fce:
#         objekt frantisek = ("prodavac", 15000, 20)          # atributy: pozice, plat, zbyvajici dovolena
#                                                             # zde oprava např 20 > 15 nneni povazovana za tvrde prepsani
#         frantisek.holiday_entitlement = 0          TOTO JE TVRDÉ PŘEPSÁNÍ!!!
#                                                    abych ostatním naznačila, že se to nemá, použiju pojmenování atributu s podtrzitkem
#                                                    tj. _holiday_entitlement

# Property @ (vlastnost) - tváří se jako atribut, je to ale metoda

class Employee:                
    def __init__(self, name, position, holiday_entitlement, gross_salary):      # nově přidaný atribut hrubá mzda/gross salary
        self.name = name                                          
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.gross_salary = gross_salary

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):  
        if self.holiday_entitlement >= days:           # odkazování přes self. !
            self.holiday_entitlement -= days           # operator -= aktualizuje a odečte days od porměnné holiday_entitlement
            return f"Užij si to"
        else:
            return f"Bohužel už nemáš nárok, zbývá ti jen {self.holiday_entitlement} dní dovolené."
    
# chci zjistit z hrubé mzdy čistou mzdu - pro to nepotřebuji vstup zvenku, můžu si ho dopočítat   
    @ property                                                  # dekorátor @ tvořící property - vypadí jako atribut, je to ale metoda
    def net_salary(self):                                       # definice výpočtu čisté mzdy
	    return self.gross_salary * (1-0.15)                     # výpočet může být jakýkoli zde jen pro ilustraci

frantisek = Employee("František", "prodavac", 9, 115000)       # doplnená hodnota atributu hruba mzda (gross_salary) 
# print(frantisek.get_info())   # uprava get info na ř. 8 na __str__
print(frantisek)                # vztahuje se ke __str__

jitka = Employee("Jitka", "administratorka", 25, 150000)
# print(jitka.get_info())
print(jitka)

# zavolani nove fce na pocitani dovolene s argumentem:
print(frantisek.take_holiday(5))
print(frantisek.take_holiday(35))

# zavolání property čistá mzda - chci jen ukázat, ne vypočítat 
print(frantisek.net_salary)   
