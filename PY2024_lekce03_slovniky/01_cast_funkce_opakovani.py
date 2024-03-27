# vytvrott definici vyz zadani:
def vyrob_muffiny(pocet_muffinu, specialni_ingredience=[]):   # nepovinny paraetmr je oznacen = 
    print(f"Vyrábím {pocet_muffinu}muffinu.")
    if specialni_ingredience == True:                         # lze napsat bez True (Python to čte: je neco v seznamu spec. ingre.?)
        print(f"Přidávám speciální ingredience: {specialni_ingredience}")
    else:
        print("Bez specialních ingrediencí")
    return pocet_muffinu

pocet = vyrob_muffiny(5, ["čokoláda", "vanilka"])
print()

# POZOR Ř. 4 True == vs. is True (True == porovnává pravdu) vs. IS TRUE (= hledá retezec "True!")