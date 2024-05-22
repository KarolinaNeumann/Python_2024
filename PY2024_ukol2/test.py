
if vysledky in data:
        for subjekt in data["vysledky"]:
            obchodni_jmeno = subjekt.get("obchodniJmeno", "N/A")
            ico = subjekt.get("ico", "N/A")
            print(f"Obchodní jméno: {obchodni_jmeno}, IČO: {ico}")
    else:
        print("Nebyl nalezen žádný výsledek.")



print(data["ekonomickeSubjekty"])
#chci pocet subbj, nazev ico 


# seznam [] - indexy 
# slovnik {} - print (nazev slovniku["nazevklice"])

# print(data["ekonomickeSubjekty"]["ico"] + ", " + data["ekonomickeSubjekty"]["obchodniJmeno"])
# print(data["obchodniJmeno"] + ", " + data["sidlo"]["textovaAdresa"])