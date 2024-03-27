sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for k in sales:     # k = key, tj. zde kniha
    print(k)


for key, values in sales.items():
   total_sales += values
   print(key, value)
print(total_sales)

print(sales.items())     # vypise klice i s hodnotami
print(sales.keys())      # vypise jen klice
print(sales.values())    # vypise jen hodnoty
