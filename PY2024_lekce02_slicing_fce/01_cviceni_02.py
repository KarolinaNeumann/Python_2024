# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. 
s = [6, 6, 6]
prumer = sum(s) / len(s)
print("Průměr s:", prumer)


# Otestujte jej na seznamech různých délek.
s1 = [1, 2, 3, 4, 5]
s2 = [10, 20, 30]
s3 = [0, 0, 0, 0, 0, 0]

prumer_s1 = sum(s1) / len(s1)
print("Průměr s1:", prumer_s1)

prumer_s2 = sum(s2) / len(s2)
print("Průměr s2:", prumer_s2)

prumer_s3 = sum(s3) / len(s3)
print("Průměr s3:", prumer_s3)