# Uvažujme vysvědčení, které máme zapsané jako slovník.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# Napiš program, který spočte průměrnou známku ze všech předmětů
def prumerna_znamka(school_report):
    return sum(school_report.values()) / len(school_report)
print(f"Prumerna znamka zaka je {prumerna_znamka(school_report)}")

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

for key in school_report:
    if school_report[key] == 1:
        print(key)