# Python 120
# ==========

# """

# Muuttuja tallennetaan tietokoneen muistiin.
# Siihen voidaan viitata lauseella id

muuttujaA = 1234
muuttujaB = 5678

print(id(muuttujaA))
print(id(muuttujaB))

muuttujaA = 1111

# viittaus on sama...
muuttujaC = muuttujaA

# ...kunnes A sai uuden arvon!
# muuttujaA = 2222

print(muuttujaC)
print(id(muuttujaA))
print(id(muuttujaC))

# referenssimuuttujissa, kuten list
# näin ei kuitenkaan käy vaan arvot menevät
# "päällekkäin"...
muuttujaA = [1,2,3,4]
muuttujaB = muuttujaA # Näin ei saa kopioida!

muuttujaA[0] = 111
muuttujaB[1] = 222
print(muuttujaA)
print(muuttujaB)

# listan kopiointi

# tee kaksi listaa, ja siirrä arvot esimerkiksi näin
# " elementti elementiltä"
# tai käytä jotain valmista funktiota
listaA = [1, 2, 3, 4]

listaB = []
for elementti in listaA:
    listaB.append(elementti)

# lista menee viittauksena funktion parametriksi
# tämän vuoksi sitä voi muuttaa funktiossa.
listaA = [1, 2, 3, 4]
luku = 111

def funktio(luku:int, lista:list):
    lista.append(1234)
    luku += 111

def funktio2(lista:list) -> list:
	uusi = lista[:]
	uusi.append(1111)
	return uusi
	
funktio(luku, listaA)
print(listaA)
print(luku)
tulos = funktio2(listaA)
print(tulos) 



# Tehtävä 120-1: Tee funktio, joka palauttaa parametrina annetun listan arvot 
# kerrottuna kahdella.

def kertaakaksi(lista:list) -> list:
    uusi = []
    for elementti in lista:
        uusi.append(elementti*2)
    return uusi

lista = [1,2,3,4]
print(kertaakaksi(lista))

# Tehtävä 120-2: Tee funktio, joka poistaa parametrina 
# annetun listan pienimmän arvon.
def poistapienin(lista:list):
    lista.remove(min(lista))

lista = [1,2,3,4]
poistapienin(lista)
print(lista)


# Tehtävä 120-3: Tee funktio, joka kääntää 3x3 matriisin.
# 1 2 3		    1 4 7
# 4 5 6  --> 	2 5 8
# 7 8 9		    3 6 9

# https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy

def kaanteismatriisi(lista:list) -> list:
    tulos = [[0,0,0],[0,0,0],[0,0,0]]
    rivi = 0
    for matriisinrivi in lista:
        sarake = 0
        for elementti in matriisinrivi:
            tulos[sarake][rivi] = elementti
            sarake += 1
        rivi += 1

    return tulos

lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(kaanteismatriisi(lista))
#print(lista)


# Tehtävä 120-4: Tee ohjelma, jolla lasketaan risti-nolla...
lista = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

PARVO = 0
OARVO = 1
XARVO = 2

ALKU = 0
LOPPU = 2

def piirra(numero:int) -> str:
    if numero == XARVO:
        return "X"
    elif numero == OARVO:
        return "O"
    else:
        return "."

def piirrapelaaja(arvo:bool) -> str:
    if arvo == True:
        return "X"
    else:
        return "O"

def piirratilanne(lista:list):
    for rivi in lista:
        print(f" {piirra(rivi[0])} {piirra(rivi[1])} {piirra(rivi[2])} ")

def kysynumero() -> int:
    while True:
        try:
            numero = int(input(f"Anna {piirrapelaaja(pelaaja)} numero välillä 0 ja 2? "))
            if numero >= ALKU and numero <= LOPPU:
                return numero
            else:
                print(f"{numero} ei ollut välillä 0 ja 2! ")            
        except:
            print(f"Tuo ei ollut numero!")


pelaaja = True # X aloittaa

pelipaalla = True
while pelipaalla:
    # otsikko
    print(f"pelaaja {piirrapelaaja(pelaaja)} vuoro!")

    piirratilanne(lista)

    # kysy arvot
    x = kysynumero()
    y = kysynumero()

    if pelaaja == True:
        lista[y][x] = XARVO
    else:
        lista[y][x] = OARVO

    # päätä onko voitettu
    for rivi in lista:
        if max(rivi) == min(rivi) and min(rivi) > 0:
            print(f"voitto pelaajalle {piirrapelaaja(pelaaja)}")
            piirratilanne(lista)
            pelipaalla = False
    dummy = kaanteismatriisi(lista)
    for rivi in dummy:
        if max(rivi) == min(rivi) and min(rivi) > 0:
            print(f"voitto pelaajalle {piirrapelaaja(pelaaja)}")
            piirratilanne(lista)
            pelipaalla = False
    # ortogonaalinen
    dummy = [lista[0][0], lista[1][1], lista[2][2]]
    if max(dummy) == min(dummy) and min(dummy) > 0:
        print(f"voitto pelaajalle {piirrapelaaja(pelaaja)}")
        piirratilanne(lista)
        pelipaalla = False
    dummy = [lista[0][2], lista[1][1], lista[2][0]]
    if max(dummy) == min(dummy) and min(dummy) > 0:
        print(f"voitto pelaajalle {piirrapelaaja(pelaaja)}")
        piirratilanne(lista)
        pelipaalla = False

    pelaaja = not pelaaja


