# vytvreni souboru
# Napište program, který se po spuštění zeptá na název souboru, který má vytvořit 
# (nebo přepsat, pokud už ten soubor existuje),
# a pak se zeptá na řádek textu, který má do souboru zapsat.

filename = input("Nazev souboru: ")
text = input("Text: ")

with open(file = filename, mode = "w", encoding = "utf-8") as output_file:
    print(text, file=output_file)