# seznam baliku 

# Přepravní společnost musí rozdělovat balíky do jednotlivých aut. 
# Při plánování dopravy je potřeba hlídat, zda pro jeden automobil není naplánována přeprava příliš velkého množství balíků. 
# Vytvoř tedy tři objekty třídy Package. Dále vytvoř seznam package_list, do kterého vlož vytvořené objekty. 
# Příklad objektů a seznamu je níže.

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def delivery_price(self):                    # viz cviceni 1 
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
package_list = [package_1, package_2, package_3]

# Vytvoř si proměnnou total_weight, do které si s využitím cyklu budeš ukládat celkovou hmotnost všech balíků. 
# Na začátku bude mít hodnotu 0.
# Vytvoř cyklus, který projde seznam package_list.
# Pro každý balík přičti jeho hmotnost k proměnné total_weight.
# Na konci programu vypiš, jaká je celková hmotnost všech balíků.

# Vypočet celkové hmotnosti všech balíků
total_weight = 0
for package in package_list:
    total_weight += package.weight
print(f"Celková hmotnost všech balíků je {total_weight} kg.")

# Vypočet celkových nákladů na přepravu
total_delivery_cost = 0
for package in package_list:
    total_delivery_cost += package.delivery_price()
print(f"Celkové náklady na přepravu všech balíků jsou {total_delivery_cost} Kč.")