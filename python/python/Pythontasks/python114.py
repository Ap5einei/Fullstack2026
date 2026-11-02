# Python 114
# ==========
"""
# funktion määrittely:

def funktionnimi():
    print("Funktio!")

# funktiokutsu

funktionnimi()
funktionnimi()


#funktiolla voi olla parametrejä

def funktionnimi(etunimi,sukunimi):
		print(f"{etunimi} {sukunimi}")


funktionnimi("Aku","Ankka")
funktionnimi(sukunimi="Aku",etunimi="Ankka")

# muuttujan käyttöä funktion sisällä

muuttuja = 111

def funktionnimi():
    # global sana mahdollistaa funktion ulkopuolisen
    # muuttujan käytön funktiossa 
    global muuttuja 
    print(muuttuja)
    muuttuja += 111

funktionnimi()
print(muuttuja)


muuttuja = 111

# funktion käyttäessä parametria parametria käytetään
# vaikka olisi saman niminen ulkoinen muuttuja
# huom että tässä ei ole global sanaa
def funktionnimi(muuttuja):
	print(muuttuja)
	muuttuja += 111

funktionnimi(123456) # globaali muuttuja ajaa yli
print(muuttuja)


# funktiolla voi olla myös paikallisia muuttuja
# paikallisen funktion käyttö tapahtuu vain funktion sisällä
def funktionnimi(muuttuja):
    paikallinen = 111
    muuttuja += paikallinen
    print(muuttuja)

funktionnimi(123456) 
"""
#Tehtävä 114-1: Tee ohjelma, jossa on funktio, joka tulostaa syötetyn parametrin.
#Tulosta Akun veljenpojat.
def tulostamerkkijono(merkkijono):
    print(merkkijono)

tulostamerkkijono("Tupu")
tulostamerkkijono("Hupu")
tulostamerkkijono("Lupu")

# Tehtävä 114-2: Tee ohjelma, jossa on funktio, joka tulostaa syötetyn parametrin ensimmäisen merkin.
def tulostamerkkijononensimmainenmerkki(merkkijono):
    print(merkkijono[0])

tulostamerkkijononensimmainenmerkki("Tupu")
tulostamerkkijononensimmainenmerkki("Hupu")
tulostamerkkijononensimmainenmerkki("Lupu")

# Tehtävä 114-3: Tee ohjelma, jossa on funktio, joka tulostaa syötetyn numeron potenssiin kolme.
# Tee myös funktio, joka tulostaa syötetyn numeron potenssiin kaksi.
def kuutio(luku):
    print(luku**3)

def nelio(luku):
    print(luku**2)

luku = int(input("Anna luku? "))
kuutio(luku)
nelio(luku)

# Tehtävä 114-4: Tee ohjelma, jossa on funktio, joka tulostaa kolmen syötetyn parametrin keskiarvon.
eka = 111
toka = 234
kolmas = 555

def keskiarvo(eka,toka,kolmas):
    print(f"Arvojen {eka}, {toka} ja {kolmas} keskiarvo on {(eka+toka+kolmas)/3}.")

keskiarvo(eka,toka,kolmas)

# Tehtävä 114-5: Tee ohjelma, jossa on funktio, joka ottaa merkkijonon ja luvun ja tulostaa merkkijonon luku monta kertaa.

def toistamerkkijono(merkkijono,luku):
    print(merkkijono*luku)

merkkijono = "saippuakauppias"
luku = 3

toistamerkkijono(merkkijono,3)

# Tehtävä 114-6: Tee ohjelma, jossa on funktio, joka ottaa kaksi lukua ja piirtää XxY alueen "o" merkillä.
def piirranelio(merkki,x,y):
    laskuri = 0
    while laskuri < y:
        print(merkki*x)
        laskuri += 1

piirranelio('o',3,3)


# Tehtävä 114-7: Tee ohjelma, jossa on funktio, joka ottaa kaksi lukua ja piirtää XxY alueen aluksi "1" ja sitten "0" merkeillä shakkilautana.
def piirrashakkilauta(x,y):
    laskuriA = 1
    laskuriB = 1
    while laskuriA <= y:
        rivi = ""
        while laskuriB <= x + laskuriA:
            if laskuriB % 2 == 0:
                rivi = rivi + "1"
            else:
                rivi = rivi + "0"
            laskuriB += 1
        print(rivi)
        laskuriA += 1
        laskuriB = laskuriA

piirrashakkilauta(15,5)

# Tehtävä 114-8: Tee ohjelma, jossa on funktio, joka ottaa merkkijonon ja piirtää siitä sananeliön
def piirrasananelio(sana):
    laskuriA = 0
    laskuriB = 0
    rivi = sana*2
    while laskuriA < len(sana):
        print(rivi[laskuriA:len(sana)+laskuriA])
        laskuriA += 1

sana = "hillo"
piirrasananelio(sana)

