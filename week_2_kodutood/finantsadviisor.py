#Finantsnõustaja
""" 
Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palganud range
ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
-küsib, kui palju sul on praegu raha,
-võrdleb seda iPhone 17 Pro hinnaga (näiteks 2 500 €),
-ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. 
"""

print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul on praegu?"))

if money < 2500:
    print("Sul pole veel piisavalt raha. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta uue iPhone 17 Pro sularahas!")
else:
    print("Saad osta iPhone 17 Pro ja veel jääb raha üle.")