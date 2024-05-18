# zapis do slovniku 

names = ["Zuzana", "Kaja", "Olga"]
with open("ucastnictvo.txt", mode = "w", encoding = "utf-8") as output_file:
    for name in names:
        print(name, file= output_file)