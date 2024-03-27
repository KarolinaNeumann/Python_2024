# rodna cisla
rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]

# Kolik přišlo mužů a kolik žen?

print(len(rodna_cisla[0]))

muzi = []
zeny = []
for rc in rodna_cisla:
    if rc[2] == 5:
        rc.append(zeny)
    else:
        rc.append(muzi)
print(zeny)
print(muzi)

# Kdy se narodil nejstarší a kdy nejmladší pacient?



# Rodné číslo je identifikační číslo, které slouží k jednoznačné identifikaci osoby. V České republice se rodné číslo skládá z 10 číslic a jednoho lomítka, které ho rozděluje na části.
# Prvních 6 číslic udává datum narození v pořadí rok (2 číslice), měsíc (2 číslice) a den (2 číslice). 
# Například pro narození 2. února 1990 by prvních 6 číslic mělo být 900202. 
# Zbytek rodného čísla (tj. část za lomítkem) slouží k identifikaci konkrétní osoby.
# Ženy mají k číslu měsíce přičteno 50, např. 845128/6219 je číslo patřící ženě.