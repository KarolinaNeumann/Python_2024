# slovnik s nazvem velikonoce
velikonoce = {"klic" : "hodnoty",
              "datum" : "1. dubna 2024",
              "symboly" : ["vajicko", "pomlazka", "beranek"],         # seznam
              "pocasi" : {"teplota": "20",                            # vlozeny slovnik
                          "oblacnost": "jasno"},
              "Další slovník" : {"klic" : "hodnota"}
              }

print(velikonoce)
print(velikonoce["Datum"])
print(velikonoce["symboly"][1])         # zanorovani > vypise 2. prvek vlozeneho seznamu  
print(velikonoce["pocasi"]["teplota"])  # zanorovani > vypise z vlozeneho slovniku (1. hran.zavorka) hodnotu teploty (2. hran. zavorka)

velikonoce["pocasi"].update({"srazky": "zadne"})        # .UPDATE (pouze pro slovniky) - pridavani polozky do dilciho slovniku
print(velikonoce)

velikonoce["symboly"].append()                          # .APPEND (pouze pro seznamy) - pridani polozky do slovniku Symboly
print(velikonoce)