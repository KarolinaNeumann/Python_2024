# slovnik s nazvem velikonoce
velikonoce = {"klic" : "hodnoty",
              "datum" : "1. dubna 2024",
              "symboly" : ["vajicko", "pomlazka", "beranek"],         # seznam
              "pocasi" : {"teplota": "20",                            # vlozeny slovnik
                          "oblacnost": "jasno"},
              "Další slovník" : {"klic" : "hodnota"}
              }

print(velikonoce)                       # vypise cely slovnik Velikonoce s hodnotami
print(velikonoce["Datum"])              # vypise hodnotu klice DAtum - tj. 1. dubna 2024 
print(velikonoce["symboly"][1])         # zanorovani > vypise 2. prvek vlozeneho seznamu Symboly
print(velikonoce["pocasi"]["teplota"])  # zanorovani > vypise z vlozeneho slovniku (1. hran.zavorka) hodnotu teploty (2. hran. zavorka)

# aktualizace slovniku - přidání nové dvojice "klíč : hodnota" do podslovníku 
# var. 1 - pomocí .update()
velikonoce["pocasi"].update({"srazky": "zadne"})   # .UPDATE (pouze pro slovniky) - pridavani polozky do dilciho slovniku
print(velikonoce)

# var. 2 - pomocí rovná se =
velikonoce["pocasi"]["tlak"] = "nizky"
print(velikonoce)  

# Přidání nového symbolu do seznamu velikonočních symbolů - pomocí .append()
velikonoce["symboly"].append("kuratko")           # .APPEND (pouze pro seznamy) - pridani polozky do slovniku Symboly
print(velikonoce)

# Získání a výpis informace o koledování   
koledovani = velikonoce["tradice"]["koledovani"]
print(f"Koledování během Velikonoc: {'Ano' if koledovani else 'Ne'}")