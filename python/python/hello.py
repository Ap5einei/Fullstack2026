

import random

# testaamme pythonia
print("Hello world!")

"""

# otsikko
print("NUMBER GUESSING GAME")

# globaalit muuttujat
arvaus = 0
salainennumero = 42
arvauksienlukumäärä = 0

# funktiot 
def arvonumero(minarg,maxarg):
    return random.randint(minarg,maxarg)


salainennumero = arvonumero(1,100)

while(True):
    print("Test")
    # Syötä pelaajan arvaus
    while(True):
        arvaus = int(input("Anna numero välillä 1 ja 100\n"))
        print("Arvauksesi oli {}!".format(arvaus))
        if arvaus < 1 or arvaus > 100:
            print("Arvauksesi on liian suuri tai pieni")
            continue
        else:
            arvauksienlukumäärä += 1
            break    

    if arvaus == salainennumero:
        print("Onnittelut! Oikein!")
        break
    elif arvaus > salainennumero:
        print("Oikea luku on pienempi!")
    else:
        print("Oikea luku on suurempi!")

print("Tarvitsit {} arvausta...".format(arvauksienlukumäärä))

"""

"""

# luokka
class Cat:
    # konstruktori funktio
    def __init__(self,name,age) -> None:
        self.age = age
        self.name = name

    def kehrää(self):
        print("{} kehrää".format(self.name))

class Siamese(Cat):
    def __init__(self, name, age, value) -> None:
        super().__init__(name, age)
        self.value = value

jenny = Cat("Jenny",123)
print(jenny) # ilmoittaa osoitteen
print(jenny.name) # "Jenny"
jenny.kehrää()

galileo = Siamese("Kali", 111, 1000)
galileo.kehrää()

# polymorphism
lista = []
lista.append(jenny)
lista.append(galileo)

for iteraattori in lista:
    iteraattori.kehrää()



# Perintään on 2 syytä!
# 1 lapsi on äidin erikoistapaus
# sisältää jotain erilaista kuin äiti
# 2 lapsi on koottu äideistä

class AAA:
    def __init__(self,argA) -> None:
        self.argA = argA

class BBB:
    def __init__(self,argB) -> None:
        self.argB = argB

class CCC(AAA,BBB):
    def __init__(self, argA, argB, argC) -> None:
        super().__init__(argA)
        self.argB = argB
        self.argC = argC

ccc = CCC("aarne", "bertta", "celsius")

"""
