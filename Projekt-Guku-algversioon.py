"""
Kivi-paber-käärid mäng

Autorid: Reelika Möller, Hannalore Menning

Programmil hetkel erilist käivitamisjuhendit pole, töötab tavalise
Pythoni programmina, tuleb lihtsalt käivitada.
Graafilise keskkonna juurde lisamisel saab mängus nuppudega valida,
algprogrammis hetkel on aga vaja valik ise kirjutada. Programm on
algeline ja teeme arvatavasti põhiprogrammis mitmeid muudatusi
seoses graafika lisamisega. Plaanis on ka teha mäng nii üksi
(arvuti vastu) kui ka sõbraga mängitavaks, et Deltas õppimisele
veidi vaheldust pakkuda.

"""

from random import randint

kasutaja_valik = input("Sisesta kivi/paber/käärid/lõpp: ") #Selle asemel potetsiaalis nupuvajutusega graafilises

kasutaja = 0
arvuti = 0

while kasutaja_valik != "lõpp":
    arvuti_valik = randint(1,4)
    
    #Teeb kasutaja valiku numbrilisteks väärtusteks, et saaks arvutiga võrrelda
    if kasutaja_valik == "kivi":
        kasutaja_valik = 1
    elif kasutaja_valik == "paber":
        kasutaja_valik = 2
    elif kasutaja_valik == "käärid":
        kasutaja_valik = 3
    
    #Leiab, kumb roundi võitis
    if kasutaja_valik == 1 and arvuti_valik == 3:
        print("kasutaja võit!")
        kasutaja += 1
    elif kasutaja_valik == 3 and arvuti_valik == 1:
        print("arvuti võit!")
        arvuti += 1
    elif kasutaja_valik > arvuti_valik:
        print("kasutaja võit!")
        kasutaja += 1
    elif kasutaja_valik < arvuti_valik:
        print("arvuti võit")
        arvuti += 1
    elif kasutaja_valik == arvuti_valik:
        print("viik")
        arvuti += 1
        kasutaja += 1

    #Näitab vahepealset seisu
    if kasutaja > arvuti:
        print(f"Kasutaja juhib {kasutaja}:{arvuti}")
    elif arvuti > kasutaja:
        print(f"Arvuti juhib {arvuti}:{kasutaja}")
    else:
        print(f"Viik {kasutaja}:{arvuti}")
    
    kasutaja_valik = input("Sisesta kivi/paber/käärid/lõpp: ")
    
    #Võiks lisada ka mõlema valikud printidega

#Näitab lõppseisu
if kasutaja > arvuti:
    print(f"Kasutaja võit {kasutaja}:{arvuti}")
elif arvuti > kasutaja:
    print(f"Arvuti võit {arvuti}:{kasutaja}")
else:
    print(f"Lõppes viigiga {kasutaja}:{arvuti}")









