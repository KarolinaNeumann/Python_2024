output = []

with open(r'C:\Users\jkbnm\PY2024\Python_2024\PY2024_lekce09_cteni\mereni.txt', encoding='utf-8') as file:
    for line in file:
        day, temp = line.split('\t')
        output.append([day, float(temp)])

print(output)