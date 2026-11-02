# Python 122
# ==========
"""
# Tuplen muodostus

from typing import Tuple


tuple = (123,456)

print(tuple[0])
print(tuple[1])


# Tehtävä 122-1: Tee funktio, joka ottaa 3 parametria ja luo tuplen, 
# johon kuuluu elementit x, y ja z.

def luotuple(x:int,y:int,z:int) -> tuple:
    tuple = (x,y,z)
    return tuple

tulos = luotuple(111,222,333)
print(tulos)
tulos = (1,2,3)
print(tulos)

# tuple on eräänlainen vakiolista...

# Tehtävä 122-2: Tee lista tupleja, joilla on nimi ja ikä. Hae nuorin ja vanhoin.
def teetuple(nimi:str, ika:int):
    dummy = (ika, nimi)
    return dummy

lista = []
lista.append(teetuple("Tupu",3))
lista.append(teetuple("Hupu",2))
lista.append(teetuple("Lupu",1))
print(lista)

print(max(lista)[1])
print(min(lista)[1])

# Tehtävä 122-3: Tee lista tupleja, joilla on nimi ja ikä. Hae kaikki ikää X nuoremmat.
def haenuoret(X:int):
    for elementti in lista:
        if elementti[0] < X:
            print(elementti)

haenuoret(3)

"""
# Tehtävä 122-4: Tee ohjelma, jossa on dictionary, johon kuuluu nimi 
# ja X kappaletta opintosuorituksia. Tee opintosuorituksista tupleja.

def teeoppilas(nimi:str):
    oppilaat[nimi] = []

def teeopintosuoritus(henkilo:str, suoritus:tuple):
    dummy = oppilaat[henkilo] # lista suorituksista
    dummy.append(suoritus)
    oppilaat[henkilo] = dummy

oppilaat = {}
teeoppilas("Tupu")
teeoppilas("Hupu")
teeoppilas("Lupu")

teeopintosuoritus("Tupu",("Äidinkieli",9))
teeopintosuoritus("Hupu",("Äidinkieli",8))
teeopintosuoritus("Tupu",("Matematiikka",9))

print(oppilaat)
