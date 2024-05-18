# ad to cviceni 1 vyplata  
# Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok,
# nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# puvodni (zkopirovano)

with open(r"C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\vykaz.txt", encoding = "utf-8") as file:
    text = file.readlines()

print(text)

hours = []
for line in text:
    hours.append(int(line))
print(hours)

hourly_rate = float(input("Hodinová mzda: "))
print(hourly_rate)

# ----
# NOVE

for monthly_hour in hours: 
    print(monthly_hour * hourly_rate)

with open(file ="vyplaty.txt",  mode = "w", encoding = "utf-8") as output_file:
    print(text, file=output_file)
