# Python 121
# ==========

# dictionary
# perustuu avain - arvo pareihin

muuttuja = {}

muuttuja["A"] = "Aku"
muuttuja["I"] = "Iines"
muuttuja["R"] = "Roope"

print(muuttuja)
print(muuttuja["A"])

muuttuja["A"] = "Jukka"
muuttuja["A"] = "Pekka"
muuttuja["A"] = "Pekka"
muuttuja["A"] = "Pekka"
print(muuttuja)

# aiheuttaa kaatumisen ilman oikeaa avainta
#print(muuttuja["B"])

for avain, arvo in muuttuja.items():
	print(f"{avain} ja {arvo}")

# tuhoaminen tapahtuu 
# del muuttuja["G"]
del muuttuja["A"]
print(muuttuja)


# Tehtävä 121-1: Tee funktio, jolle syötetään luku X ja funktio asettaa 
# sille arvoksi X*123

def syota(luku:int):
    muuttuja[luku] = luku*123

muuttuja = {}
syota(5)
syota(10)
print(muuttuja)

# Tehtävä 121-2: Tee funktio, jolle syötetään merkkijonoja. Funktio ei salli duplikaatteja.
def syotamerkkijono(merkkijono:str):
    muuttuja[merkkijono] = merkkijono

muuttuja = {}
syotamerkkijono("Aarne")
syotamerkkijono("Bertta")
syotamerkkijono("Bertta")
print(muuttuja)


# Tehtävä 121-3: Tee funktio, jolle syötetään merkkijono. Se 
# ottaa talteen merkkijonon kirjaimet ja tulostaa "*" merkkejä 
# yhtä monta kertaa kuin kirjain löytyy merkkijonosta.
def syotamerkkijonotulosta(merkkijono:str):
    for merkki in merkkijono:
        muuttuja[merkki] = ""
    for merkki in merkkijono:
        muuttuja[merkki] += "*"

muuttuja = {}
syotamerkkijonotulosta("saippuakauppias")
print(muuttuja)

# Tehtävä 121-4: Tee ohjelma, johon syötetään puhelinnumeroita ja henkilöitä. 
# Tulosta lopuksi kaikki tiedot.

def syotapuhelinluettelo(nimi:str, luku:int):
    muuttuja[nimi] = luku

muuttuja = {}
syotapuhelinluettelo("Aku",616)
syotapuhelinluettelo("Iines",919)
syotapuhelinluettelo("Roope",313)

for avain, arvo in muuttuja.items():
    print(f"{avain} on puhnumero {arvo}")


# Tehtävä 121-5: Tee ohjelma, johon syötetään ja poistetaan 
# puhelinnumeroita ja henkilöitä. Tulosta lopuksi kaikki tiedot.

def tuhoapuhelinluettelo(nimi:str, luku:int):
    del muuttuja[nimi]

muuttuja = {}

while True:
    toiminta = int(input("-1 = poistu, 0 = tuhoa, 1 = lisää? "))
    nimi = input("Anna Nimi? ")
    luku = int(input("Anna puhnumero? "))
    if toiminta == -1:
        break
    elif toiminta == 1:
        syotapuhelinluettelo(nimi,luku)
    else:
        tuhoapuhelinluettelo(nimi,luku)
print(muuttuja)

# Tehtävä 121-6: Tee ohjelma, jolle syötetään dictionary. Muuta avaimet arvoiksi ja päinvastoin.
def muuta(muuttuja:dict) -> dict:
    dummy = {}
    for avain, arvo in muuttuja.items():
        dummy[arvo] = avain
    return dummy

muuttuja = { "A": "Aku", "I": "Iines", "R":"Roope"}
print(muuttuja)
muuttuja = muuta(muuttuja)
print(muuttuja)


# Tehtävä 121-7: Tee ohjelma, johon syötetään kirjan nimi ja tekijä sekä vuosi niin, että kukin kirja on yksi dictionary.
# Tee lista dictionaryista ja tulosta niiden sisältö.
lista = []

while True:
    nimi = input("Anna Nimi? ")
    if nimi == "":
        break
    tekija = input("Anna Tekijä? ")
    luku = int(input("Anna vuosi? "))
    dummy = {"nimi": nimi, "tekija": tekija, "vuosi": luku}
    lista.append(dummy)

for teos in lista:
    print(teos)


