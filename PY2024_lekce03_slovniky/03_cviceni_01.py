# Vytvoř slovník, který reprezentuje vysvědčení. 
# Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. 
# Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). 
# Vypiš obsah slovníku pomocí funkce print().

vysvedceni = {"cesky jazyk": 1,
              "matematika" : 1,
              "dejepis" : 2}

print(vysvedceni)                     # vypise cely slovnik se vsemi klici a hodnotami 
print(vysvedceni.keys())              # vypise jen klice (bez hodnot)
print(vysvedceni.values())            # vypise jen hodnoty (bez klíčů)
print(vysvedceni["cesky jazyk"])      # vypise hodnotu por klic "cesky jazky"

# vyuziti napr. vypocitat prumer daneho zaka (soucet znamek / soucet predmetu)
print((sum(vysvedceni.values())/len(vysvedceni)))  
      
