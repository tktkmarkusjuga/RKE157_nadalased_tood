klaasid = int(input("Mitu klaasi vett oled täna joonud? "))

vesi = klaasid * 250
protsent = vesi / 2000 * 100

print("Oled täitnud", protsent, "% päevanormist.")

if protsent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")