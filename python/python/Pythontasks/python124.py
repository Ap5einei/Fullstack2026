# python 124
# ==========
"""
# w tarkoittaa että kirjoittaa ja pyyhkii edellisen
# a tarkoittaisi appends, eli lisätään loppuun

with open("testitesti.txt", "a") as tiedosto:
    tiedosto.write("Tupu\n")
    tiedosto.write("Hupu\n")
    tiedosto.write("Lupu\n")
    tiedosto.write("Ankkalinnan kauhut\t\t")
    tiedosto.write("Huhuu!")


# tyhjää tiedoston sisällön muttaa säilyttää itse tiedoston
open("testitesti.txt", "w").close()


#tuhoa tiedosto

import os 

os.remove("testitesti.txt")


# Tehtävä 124-1: Tee ohjelma, jolle syötetään lauseita, jotka kirjoitetaan 
# lopuksi tiedostoon.

lista = []
while True:
    lause = input("Anna talletettava lause? ")
    if lause == "":
        break
    lista.append(lause)

with open("testitesti.txt", "w") as tiedosto:
    for lause in lista:
        tiedosto.write(f"{lause}\n")

# Tehtävä 124-2: Tee ohjelma, jolle syötetään nimi ja ikä pareja. 
# Ohjelma kirjoittaa sen .csv tiedostoksi. Erota tiedot ";" merkillä.

lista = []
while True:
    nimi = input("Anna talletettava nimi? ")
    if nimi == "":
        break
    ikä = int(input("Anna talletettava ikä? "))
    lista.append(f"{nimi};{ikä}\n")

with open("testitesti.csv", "w") as tiedosto:
    for lause in lista:
        tiedosto.write(f"{lause}")
"""


# Tehtävä 124-3: Tee ohjelma, jolle voidaan syöttää lauseita tai lukea 
# mitä on kirjoitettu. Käytä numerointia erottamaan lauseet.
def luetiedosto(tiedostonimi:str):
    with open(tiedostonimi) as tiedosto:
        for rivi in tiedosto:
            print(rivi)

def kirjoitatiedosto(tiedostonimi:str, lause, numero):
    with open(tiedostonimi, "a") as tiedosto:
        tiedosto.write(f"{numero}\n")
        tiedosto.write(f"{lause}\n")

def haekorkeinnumero(tiedostonimi:str) -> int:
    tulos = 0
    with open(tiedostonimi) as tiedosto:
        laskuri = 1
        for rivi in tiedosto:
            if laskuri % 2 != 0:
                if tulos < int(rivi.strip()):
                    tulos = int(rivi.strip())
            laskuri += 1
    return tulos

tiedostonimi = "mietelause.txt"
numero = haekorkeinnumero(tiedostonimi) + 1

while True:
    valinta = int(input("Mitä teet? -1 lue kaikki, 0=lopeta ja 1 = kirjoita ... "))
    if valinta == 0:
        break
    elif valinta == 1:
        lause = input("Anna mietelause? ")
        kirjoitatiedosto(tiedostonimi,lause, numero)
        numero += 1
    else:
        luetiedosto(tiedostonimi)        

