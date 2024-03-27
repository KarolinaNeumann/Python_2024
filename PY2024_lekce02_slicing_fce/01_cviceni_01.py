# pohyby na uctu 
# Mějme seznam pohybů na nějakém bankovním účtu:

pohyby = [1200, -250, -800, 540, 721, -613, -222]

# Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])

# Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])

# Vypište kolik je všech pohybů dohromady.
print(len(pohyby))

# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(max(pohyby))
print(min(pohyby))
# v tomto cviceni nedava vlastne smysl, potrebovali bysme uzit absolutni hodnotu pomoci fce abs() !!!!
orig_pohyby = [1200, -250, -800, 540, 721, -613, -222]
abs_pohyby = []                             # iniciace prázdného seznamu
for cislo in orig_pohyby:                   # cyklus na prochazeni puvodniho seznamu
    if cislo < 0:                           # je
        abs_pohyby.append(-1 * cislo)         
    else:
        abs_pohyby.append(cislo)
print(abs_pohyby)

print(abs(orig_pohyby))

# NEBO FCE ABS()
orig_pohyby = [1200, -250, -800, 540, 721, -613, -222]
abs_pohyby = []
for cislo in orig_pohyby:
    abs_pohyby.append(abs(cislo))
print(abs_pohyby)

# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
celkovy_prirustek = sum(pohyby)
print("Celkový přírůstek na účtu:", celkovy_prirustek)