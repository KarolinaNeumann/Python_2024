# oop - seznam zamestnancu poic a jejich dovolene - ulozeni informaci v seznamu
# nevýhoda seznamu : nebude vědět, co znamená 25
zamestnanec_1 = ["Jana", "programatorka", 25]
zamestnanec_2 = ["Zuzana", "vyvojarka", 7]              

# pouziti OOP: vytvoreni tridy pro zachovani dat o zamestnancich + jejich dovolene
# vytvoreni tridy (tvar): 
#     class Emploee  = class, klíčové slovo pro vytvoreni tridy, pojmenování /zde Emploee, vždy 1. velké písmeno (přehlednost)
#     def __init__(self, dalsi atributy):   = pevně daný tvar, doplňuju jen další atributy
#           self.dalsi atribut 1 = dalsi atribut      = definovani dalsich atributu
#           self.dalsi atribut 2 = dalsi atribut


class Employee:                
    def __init__(self, name, position, holiday_entitlement):     # další atributy = name, position, holiday
        self.name = name                                          # definovani dalsich atributu, dany tvar
        self.position = position
        self.holiday_entitlement = holiday_entitlement

# vytvoreni metody (tvar):
#   def pojmenovani metody(vstup):     = zde vstup je SELF !!!
#       return (např. f string)

    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

# vytvoření objektu (tvar): do proměnné, zavolání třídy a atributu
frantisek = Employee("František", "prodavac", 9)           # = atributy: name, position, holiday_entitlement
print(frantisek.get_info())

jitka = Employee("Jitka", "administratorka", 25)
print(jitka.get_info())

