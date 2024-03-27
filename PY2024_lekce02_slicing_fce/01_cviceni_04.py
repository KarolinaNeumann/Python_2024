# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

s = [6, 6, 6]

stred_index = len(s) // 2
stred = s[stred_index]
print("Střed s:", stred)


# Nyní můžeme tento výraz otestovat na různě dlouhých seznamech. Například:
s1 = [1, 2, 3, 4, 5]
s2 = [10, 20, 30, 40]
s3 = [0, 0, 0, 0, 0, 0]

stred_s1 = s1[len(s1) // 2]
print("Střed s1:", stred_s1)

stred_s2 = s2[len(s2) // 2]
print("Střed s2:", stred_s2)

stred_s3 = s3[len(s3) // 2]
print("Střed s3:", stred_s3)