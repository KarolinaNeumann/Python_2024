# vytvoreni souboru pro zapis .txt

# definovani textu
text = "chci zapsat tento text do souboru" # pokud opravim text (.txt), v souboru se to natvrdo prepise

# mod zapisovani (defaultne nastaveno čtení, nutno zmenit pomoci "mode" )
with open("soubor.txt", mode = "w", encoding = "utf-8") as output_file:   # w = write - zapise do souboru
    print(text, file = output_file)       # pokud existuje již dokument txt s nazvem soubor - prid text
                                          # pokud již existuje, přidá do něj text

with open("soubor.txt", mode = "r", encoding = "utf-8") as output_file:   # r = read - napise chybu not writable
    print(text, file = output_file)

with open("soubor.txt", mode = "a", encoding = "utf-8") as output_file:   # a = append - prida do souboru nakonec
    print(text, file = output_file)

