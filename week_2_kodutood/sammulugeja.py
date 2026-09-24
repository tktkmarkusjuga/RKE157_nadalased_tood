#Sammulugeja

""" 
Sul on eesmärk teha iga päev 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
-Kui protsent < 50: „Alles poolel teel, liigu edasi!“
-Kui protsent < 75: „Tubli, oled peaaegu kohal!“
-Kui protsent ≥ 100: „Palju õnne, oled oma eesmärgi täitnud!“ 
"""

goal = 10000
steps = int(input("Mitu sammu oled juba teinud?:"))

percent = (steps / goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")