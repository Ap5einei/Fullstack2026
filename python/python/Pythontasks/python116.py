# python 116
# ==========
"""
# listat

# Lista voi aina olla tyhjä
lista = []

# listassa voi olla numeroita tai merkkijonoja
lista = [11,22,33]
lista = ["kokeilu","pirtti"]

print(lista[0]) # näytä listan ensimmäinen elementti
print(lista[0][0]) # näytä listan ekan elementin eka elementti
print(len(lista[0]))

# Listalla voi olla sekaisin erityyppisiä elementtejä
lista = ["Aku", 616, "Ankkalinna"]

# Lisää listaan
lista.append(123) # loppuun
lista.insert(0,111) # (X,Y) X indeksiin Y arvo

print(lista)

# Poista listasta
lista.pop() # poistaa aina viimeisen
lista.pop(1) # poistaa indeksin mukaan

print(lista)

# remove poistaa arvon
if 616 in lista:
	lista.remove(616) # poistaa arvon

print(lista)

# listan voi järjestellä

lista = [33,55,11,99,22]

uusilista = sorted(lista)

lista.sort()
print(uusilista)
print(lista)

lista = ["Aku", "Iines", "Ankkalinna"]
uusilista = sorted(lista)
print(uusilista)

# entä jos numeroita ja merkkijonoja sekaisin?
# lista = ["Aku", 616, "Ankkalinna"] ei toimi

lista = [3,2,6,8,1]
uusilista = list(reversed(lista))
lista.reverse()
print(uusilista)
print(lista)

# max ja min funktioilla voit ottaa listan suurimman ja pienimmän arvon

print(max(lista))
print(min(lista))
"""
# Tehtävä 116-1: Tee ohjelma, johon kuuluu lista = [0,0,0,0,0,0,0,0,0,0] 
# syötetään indeksi 0+ ja luku arvoksi. Täytä listaa ja tulosta joka syötön jälkeen listan sisältö.
lista = [0,0,0,0,0,0,0,0,0,0]
while True:
    indeksi = int(input("Anna indeksi? "))
    arvo = int(input("Anna arvo? "))
    if indeksi == -1:
        break
    lista[indeksi] = arvo
    print(lista)


# Tehtävä 116-2: Tee ohjelma, johon syötetään X kappaletta numeroita. 
# Tulosta luotu lista lopuksi.
lista = []
laskuri = 0
while laskuri < 5:
    arvo = int(input("Anna arvo? "))
    lista.append(arvo)
    laskuri += 1

print(lista)

# Tehtävä 116-3: Tee ohjelma, jossa on lista, johon voi lisätä ja poistaa arvoja.
lista = []
while True:
    toiminta = int(input("-1 = poista, 0 = lopeta, 1 = lisää? "))
    arvo = int(input("Anna arvo? "))
    if toiminta == 0:
        break
    elif toiminta == 1:
        lista.append(arvo)
    else:
        if arvo in lista:
            lista.remove(arvo)
    print(lista)

# Tehtävä 116-4: Tee ohjelma, johon syötetään sanoja. Pysäytä se, jos sama sana tuli kahdesti.
lista = []
while True:
    sana = input("anna sana? ")
    if sana in lista:
        break
    lista.append(sana)
    print(lista)


# Tehtävä 116-5: Tee ohjelma, johon syötetään numeroita. 
# Tulosta joka numeron jälkeen lista sekä sen järjestetty versio.
lista = []
while True:
    numero = int(input("anna numero? "))
    if numero == -1:
        break
    lista.append(numero)
    print(f"lista on {lista} ja järjestetty lista on {sorted(lista)}")

# Tehtävä 116-6: Tee ohjelma, johon syötetään numeroita. 
# Tulosta joka numeron jälkeen suurin ja pienin arvo.
lista = []
while True:
    numero = int(input("anna numero? "))
    if numero == -1:
        break
    lista.append(numero)
    print(f"listan suurin numero on {max(lista)} ja pienin numero on {min(lista)}")

# Tehtävä 116-7: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. 
# Järjestä lista ja anna se paluuarvona

def jarjestalista(lista):
    return sorted(lista)

lista = [3,7,1,5,3]
print(jarjestalista(lista))

# Tehtävä 116-8: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. 
# Palauta listan pituus paluuarvona.
def ilmoitalistanpituus(lista):
    return len(lista)

lista = [3,7,1,5,3]
print(ilmoitalistanpituus(lista))

# Tehtävä 116-9: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. 
# Palauta listan keskiarvo paluuarvona.
def laskekeskiarvo(lista):
    return sum(lista)/len(lista)

lista = [3,7,1,5,3]
print(laskekeskiarvo(lista))

# Tehtävä 116-10: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. 
# Palauta listan vaihteluväli (suurin miinus pienin arvo) paluuarvona.
def laskevaihteluvali(lista):
    return max(lista) - min(lista)

lista = [3,7,1,5,3]
print(laskevaihteluvali(lista))
