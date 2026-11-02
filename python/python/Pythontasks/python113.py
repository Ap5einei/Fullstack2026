# Python 113
# ==========

# break - hyppää ulos silmukasta
# continue - palaa silmukan alkuun

summa = 0
while True:
    luku = int(input("Anna luku "))
    if luku == -1:
        break
    summa += luku
	
summa = 0
luku = 0
while luku != -1:
    luku = int(input("Anna luku "))
    if luku != -1:
        summa += luku

summa = 0
while True:
    luku = int(input("Anna luku "))
    if luku == -1:
        break
    if luku >= 10:
        continue
    summa += luku


# Monien silmukoiden tapauksessa break hyppää aina seuraavaan ulommaiseen silmukkaan

# Tehtävä 113-1: Tee ohjelma, joka laskee kertotaulun lukuun X asti, eli (esim 2) 1x1, 1xX, Xx1, XxX...
luku = int(input("Anna luku? "))
laskuriA = 1
laskuriB = 1
while laskuriA <= luku:
    while laskuriB <= luku:
        print(f"{laskuriA} * {laskuriB} = {laskuriA*laskuriB}")
        laskuriB += 1
    laskuriB = 1
    laskuriA += 1


# Tehtävä 113-2: Tee ohjelma, jolle syötät lauseen. Tulosta jokaisen sanan ensimmäinen kirjain.
lause = input("Anna lause? ")
laskuri = 0
while laskuri < len(lause):
    if laskuri == 0:
        print(lause[laskuri])
    if (" " in lause[laskuri]):
        print(lause[laskuri+1])
    laskuri += 1


# Tehtävä 113-3: Tee ohjelma, joka laskee annetun luvun X kertoman (esim 4) 1*2*3*X = ...
luku = int(input("Anna luku? "))
laskuri = 1
tulo = 1
teksti = ""
while laskuri <= luku:
    teksti = teksti + str(laskuri) + "*"
    tulo *= laskuri
    print(f"{laskuri} saa arvoksi {teksti[:-1]} = { tulo }")
    laskuri += 1


# Tehtävä 113-4: Tee ohjelma, joka tulostaa kaikki luvut käyttäjän antamaan lukuun asti.
# Tee ohjelma niin, että kukin pari lukuja esitetään suurempi ensin.

luku = int(input("Anna luku? "))
laskuri = 1
teksti = ""
while laskuri <= luku:
    if laskuri % 2 != 0 and laskuri == luku:
        teksti = teksti + str(laskuri)
        print(f"{teksti}")
        break
    else:
        teksti = teksti + str(laskuri+1) + " "  + str(laskuri) + " "
        laskuri += 2
    print(f"{teksti}")

# Tehtävä 113-5: Tee ohjelma, joka tulostaa kaikki luvut käyttäjän antamaan lukuun asti.
# Tee ohjelma niin, että ensin esitetään 1, sitten X, sitten 2, sitten X-1 jne...


luku = int(input("Anna luku? "))
laskuri = 1
teksti = ""
while laskuri <= luku:
    teksti = teksti + str(laskuri) + " " + str(luku-laskuri+1) + " "
    print(f"{teksti}")
    if laskuri == luku-laskuri+1 or laskuri == luku-laskuri:
        break
    laskuri += 1

