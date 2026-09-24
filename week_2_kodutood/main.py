""" 

Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev) ning väljastab vastuse põhjal vastava sõnumi.
Kasutaja sisestab ühe sõna:
Kas "tööpäev"
või "puhkepäev". 

Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst:
Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev", kuvatakse ekraanile tekst:
Veel üks osa Netflixist!
"""

#Alusta programmi.
#Küsi kasutajalt: „Mis päev on homme? (tööpäev/puhkepäev)“.
#Salvesta vastus muutujasse day.
#Kui day on võrdne sõnaga „tööpäev“, siis väljasta ekraanile: „Ma lähen magama, head ööd!“.
#Muidu, kui day on võrdne sõnaga „puhkepäev“, siis väljasta ekraanile: „Veel üks osa Netflixist“.
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: „Vale väärtus“.
#Lõpeta programm.

day = input("Mis päev on homme? (tööpäev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus")