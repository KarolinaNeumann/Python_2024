# dalsi datove struktury 

# N-tice: vypada jako seznam, ale nemá [], nelze je menit, prepisovat.. = uzitecne pro 

# TYPE: overeni datoveho typu 
seznam = [1, 2, 3, 4,]
print(type(seznam))      # vypíše <class "list">

ntice = 1, 2, 3, 4
print(type(ntice))       # vypise <class "tuple">

# n-tice se umi transformovat na se vice promennych 
moje_ntice = "Aneta", 8, True

jmeno, cislo, ma_hlad = moje_ntice  #vicenasobna promenna 
print(jmeno)

# mnoziny (set) - nelze do nich ulozit jednu hodnotu dvakrat

names = set()            # vytvori prazdnou mnozinu ( set)
names.add("Kaja")
names.add("Papaki")

print(names)