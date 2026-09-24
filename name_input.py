perekonnanimi = input("Sisesta oma perekonnanimi: ")
sugu = input("Sisesta oma sugu (m või n): ")

if sugu == "m":
    print("Tere, härra " + perekonnanimi + "!")
elif sugu == "n":
    print("Tere, proua " + perekonnanimi + "!")
else:
    print("Tere tulemast, " + perekonnanimi + ", sugu polegi tähtis!")