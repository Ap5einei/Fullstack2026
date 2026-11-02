# Python 115
# ==========

# funktiolla voi olla paluuarvo ja sen suositeltu tietotyyppi voidaan määrittää:
"""

def funktionnimi(muuttuja):
    muuttuja += 1234
    return muuttuja

def funktionnimi(muuttuja:int):
    muuttuja += 1234
    return muuttuja
"""


def funktionnimi(muuttuja:int) -> int:
    muuttuja += 1234.56
    return muuttuja

print(funktionnimi(1234))

"""
Seuraavaksi kutsutaan funktioita toisista funktioista.
"""

# Tehtävä 115-1: Tee ohjelma, jonka funktio palauttaa anntuista parametreista pienimmän
para1 = 33.56
para2 = 65.88

def palautamin(para1,para2):
    if para1 <= para2:
        tulos = para1
    else:
        tulos = para2
    return tulos

print(palautamin(para1,para2))

# Tehtävä 115-2: Tee ohjelma, jonka funktio ilmoittaa onko annettu merkki sama tai ei (True tai false)
merkkijono1 = "kalle"
merkkijono2 = "mikko"

def onkosama(merkkijono1,merkkijono2):
    return merkkijono1 == merkkijono2

print(onkosama(merkkijono1,merkkijono2))

# Tehtävä 115-3: Tee ohjelma, jossa
# on funktio, joka piirtää parametrina annettua merkkiä annetun luvun verran.
# Tee funktio joka piirtää näin neliön annettua merkkiä.
def teerivi(merkki,koko):
    print(merkki*koko)

def teenelio(merkki,koko):
    laskuri = 0
    while laskuri < koko:
        teerivi(merkki,koko)
        laskuri += 1

teenelio("*",5)

# Tehtävä 115-4: Tee ohjelma, jossa
# on funktio, joka piirtää parametrina annettua merkkiä annetun luvun verran.
# Tee funktio joka piirtää näin nelikulmion annettua merkkiä.
def teerivi(merkki,koko):
    print(merkki*koko)

def teenelikulmio(merkki,X,Y):
    laskuri = 0
    while laskuri < Y:
        teerivi(merkki,X)
        laskuri += 1

teenelikulmio("#",5,8)


# Tehtävä 115-5: Tee ohjelma, joka piirtää funktiossa joulukuusen "*" merkeillä.
# Tee toinen funktio, joka antaa sille parametrit

def piirrajoulukuusi(korkeus):
    iteraattori = 0
    while (iteraattori <= korkeus):
        malli = " "*(korkeus-iteraattori) + "*"*(iteraattori*2+1)
        print(malli)
        iteraattori += 1

def piirrakuusi():
    korkeus = int(input("Anna kuusen korkeus: "))
    piirrajoulukuusi(korkeus)

piirrakuusi()

# Tehtävä 115-6: Tee ohjelma, joka piirtää funktioilla nelikulmioita ja joulukuusia.
# Tee toinen funktio, joka antaa sille parametrit ja piirrä erilaisia muotoja.

def piirrajotain():
    piirrakuusi()
    teenelikulmio("*",15,3)
    piirrakuusi()

piirrajotain()
