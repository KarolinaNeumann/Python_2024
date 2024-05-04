# while loop - hlidá splnení podmínky 
soucet = 0           # počatek
cislo = 1            # cislo, s kterým pracuji

while cislo <= 10:   # uzavreny interval
    soucet += cislo  # pricti hodnotu cisla
    print(cislo)     # kontrola jaka cisla jsou zahrnuta (overeni intervalu)
    cislo += 1       # a zaroven ho o jednicku navyšit 
                     # jednicku jsem uz secetla v r. 3

print("Součet čísel od 1 do 10 je:", soucet)

# for loop = prochází seznam, dokud má položky, zpracuje je
soucet = 0

for cislo in range(1, 11):
    soucet += cislo
    print(cislo)   # kontrola jaka cisla jsou zahrnuta (overeni intervalu)

print("Součet čísel od 1 do 10 je:", soucet)