# pocet slov 
# Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti slovech 
# pojednávající o našem hlavním městě. Napište program, který spočítá počet slov v tomto textu, 
# abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu 
with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\sloh.txt", encoding = "utf-8") as file:
    text = file.readlines()
print(text)

# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
# Vypište na výstup počty slov na každém řádku
# Vypište na výstup celkový počet všech slov v souboru

word_count = 0
for line in text:
    words = line.split(" ")  # kazde opakovani = novy radek = novy seznam
    print(len(words))
    word_count += len(words)
    # print(words)    

print(word_count)

# -----
# od Anet
# Otevření souboru a načtení řádků do seznamu
seznam_radku = []
with open('reseni-cviceni/lekce-09/01-cteni-souboru/praha.txt', 'r', encoding='utf-8') as soubor:
    seznam_radku = soubor.readlines()

# Analýza počtu slov na řádcích a výpis
celkovy_pocet_slov = 0
print("Počet slov na řádku:")
for radek in seznam_radku:
    slova = radek.split()
    pocet_slov = len(slova)
    print(pocet_slov)
    celkovy_pocet_slov += pocet_slov

# Výpis celkového počtu slov
print(f"Celkový počet slov v dokumentu: {celkovy_pocet_slov}")
