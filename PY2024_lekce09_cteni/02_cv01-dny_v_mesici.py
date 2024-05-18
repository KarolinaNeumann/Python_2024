# dny v mesici
# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto: 
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.

with open(r"months.txt", mode = "w", encoding = "utf-8") as output_file:
    for days in pocty_dni:
        print(days, file= output_file)