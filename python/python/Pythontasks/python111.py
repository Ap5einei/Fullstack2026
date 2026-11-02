
# python 111

# Yhdistä merkkijonot + merkillä
print("aarne" + " " + "bertta")

# kerro merkkijonot * merkillä 
print("Aku"*3)

# merkkijonon pituus
print(len("Aku Ankka"))
print(len("         "))

# Merkkijono on lista, joka muodostuu merkeistä
# näin ollen sillä on listan ominaisuudet

# Tulosta merkkijonon eka merkki
# järjestys alkaa kohdasta 0 ja jatkaa siitä
muuttuja = "saippuakauppias"
print(muuttuja[0]) # ensimmäinen merkki
print(muuttuja[-1]) # viimeinen merkki
# muuttuja[X] kertoo yksittäisen merkin paikan

print(muuttuja[:6]) # jos :Y Ensimmäisestä merkistä Y merkkiä
print(muuttuja[4:]) # jos X: merkistä X loppuun asti 
print(muuttuja[4:10]) # jos X:Y X merkistä otetaan Y-1 merkkiin asti

print(muuttuja.find("a")) # palauttaa ensimmäisen sijainnin merkkijonolle

muuttuja = "joulukuusi"
print(muuttuja.find("kuu"))
print(muuttuja.find("z")) # palauttaa -1, koska ei löydy


# Tehtävä 111-1: Piirrä joulukuusi * merkeillä. Syötä ensin joulukuusen korkeus numerona.
korkeus = int(input("Anna kuusen korkeus: "))
iteraattori = 0
while (iteraattori <= korkeus):
#    malli = " "*(korkeus-iteraattori) + "*"*(iteraattori) + "*" + "*"*(iteraattori)
    malli = " "*(korkeus-iteraattori) + "*"*(iteraattori*2+1)
    print(malli)
    iteraattori += 1

# Tehtävä 111-2: Syötä merkkijono ja toistojen lukumäärä. Tulosta sitten merkkijono toistettuna.
merkkijono = input("Anna merkkijono: ")
toistojenlukumaara = int(input("Anna toistojen lukumäärä: "))
print(f"{merkkijono} kertaa {toistojenlukumaara} on {merkkijono*toistojenlukumaara}")

# Tehtävä 111-3: Syötä merkkijono ja tulosta se. Lisää vielä "=" merkeillä merkkijonon pituinen alleviivaus.
merkkijono = input("Anna merkkijono: ")
print(f"{merkkijono}\n{len(merkkijono)*'='}")

# Tehtävä 111-4: Syötä kaksi merkkijonoa ja kerro kumpi on pitempi
merkkijonoA = input("Anna merkkijono A: ")
merkkijonoB = input("Anna merkkijono B: ")
if len(merkkijonoA) > len(merkkijonoB):
    print("A on pitempi kuin B")
elif len(merkkijonoA) < len(merkkijonoB):
    print("B on pitempi kuin A")
else:
    print("A ja B ovat yhtä pitkät")

# Tehtävä 111-5: Syötä merkkijono ja tulosta sen merkit viimeisestä ensimmäiseen
merkkijono = input("Anna merkkijono: ")
iteraattori = len(merkkijono)
while (iteraattori > 0):
    print(merkkijono[iteraattori-1])
    iteraattori -= 1

# Tehtävä 111-6: Syötä merkkijono ja tulosta sen toinen ja toiseksi viimeinen merkki
merkkijono = input("Anna merkkijono: ")
print(f"toinen merkki on {merkkijono[1]} ja toiseksi viimeinen merkki on {merkkijono[-2]}")

# Tehtävä 111-7: Syötä merkkijono ja tee siitä uusi merkkijono, jonka merkit ovat päinvastoin
merkkijono = input("Anna merkkijono: ")
iteraattori = len(merkkijono)
tulos = ""
while (iteraattori > 0):
    tulos = tulos + merkkijono[iteraattori-1]
    iteraattori -= 1
print(tulos)

# Tehtävä 111-8: Syötä merkkijono ja tulosta se niin, että kullakin rivillä on yhdestä pituuteen verran kirjaimia
merkkijono = input("Anna merkkijono: ")
iteraattori = 0
while (iteraattori <= len(merkkijono)):
    print(f"{merkkijono[:iteraattori]}")
    iteraattori += 1

# Tehtävä 111-9: Tee 20 merkkinen merkkijono "=" merkeistä. Syötä merkkijono, jono korvaa = merkkejä. 
# Tämä merkkijono on lisäksi tasattu oikealle, vasemmalle tai keskelle valinnan mukaan.
merkkijono = input("Anna merkkijono: ")
tasaus = 2 # 0 = vasen, 1 = oikea, 2 = keskelle
if tasaus == 0:
    tulos = merkkijono + (20-len(merkkijono))*"="
elif tasaus == 1:
    tulos = (20-len(merkkijono))*"=" + merkkijono
else:
    tulos = (10-int(len(merkkijono)/2))*"=" + merkkijono + (10-int(len(merkkijono)/2))*"="
print(tulos)


# Tehtävä 111-10: Syötä merkkijono ja etsi kaikki vokaalit
merkkijono = input("Anna merkkijono: ")
iteraattori = 0
tulos = ""
while iteraattori < len(merkkijono):
    iteraattori2 = 0
    vokaalijono = "aeiouyäöAEIOUYÄÖ"
    while iteraattori2 < len(vokaalijono):
        if merkkijono[iteraattori].find(vokaalijono[iteraattori2]) != -1:
            tulos = tulos + merkkijono[iteraattori]
        iteraattori2 += 1
    iteraattori += 1
print(tulos)
