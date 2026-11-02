# Python 102

# input on komento, joka palauttaa merkkijonon
# Tässä tulos on merkkijono
from email.errors import FirstHeaderLineIsContinuationDefect
from tkinter import N


tulos = input("Kirjoita jotain")
print(tulos)
print("Kirjoitit tekstin: " + tulos)

# muuttuja on koodarin antama nimi muistipaikalle,
# jonne talletetaan jokin tieto (esimerkiksi merkkijono)

# Merkkijonoilla on ominaisuus, että niitä voidaan 
# yhdistää + merkillä
merkkijonomuuttuja = "Oulun " + "Lippo"
print(merkkijonomuuttuja)

# Muuttuja voi saada uuden arvon
# Muuttujan ilmaisema muistipaikka saa uuden arvon
# tämä mahdollistaa muuttujan arvon muuttamisen
merkkijonomuuttuja = "Aku Ankka"
print(merkkijonomuuttuja)

# Tehtävä 102-1: Kirjoita ohjelma, joka kysyy oman nimesi ja tulostaa sen.
nimi = input("Anna nimesi? ")
print(nimi)

# Tehtävä 102-2: Kirjoita ohjelma, joka kysyy oman nimesi kerran ja tulostaa sen kahdesti.
nimi = input("Anna nimesi? ")
print(nimi)
print(nimi)

# Tehtävä 102-3: Kirjoita ohjelma, joka kysyy kaksi kertaa nimen ja tulostaa sitten annetun nimen.
etunimi = input("Anna etunimesi? ")
print(etunimi)
sukunimi = input("Anna sukunimesi? ")
print(sukunimi)

# Tehtävä 102-4: Kirjoita ohjelma, joka kysyy nimen ja tulostaa jonkin erikoismerkin ja nimen ja toisen erikoismerkin.
# Esimerkiksi: !Aapeli@
nimi = input("Anna nimesi? ")
print("!" + nimi + "@")

# Ohjelmassa voi olla monta muuttujaa ja tulostuksessa voidaan käyttää useita muuttujia.

# Tehtävä 102-5: Kirjoita ohjelma, joka kysyy etunimen ja sukunimen ja kirjoittaa "nimesi on <etunimi> sukunimi>."
etunimi = input("Anna etunimesi? ")
sukunimi = input("Anna sukunimesi? ")
print("Nimesi on "+ etunimi + " " + sukunimi+".")

# Tehtävä 102-6: Kirjoita ohjelma, joka kysyy nimesi ja osoitteesi ja tulostaa sen kuten osoite kirjoitetaan kirjeessä
nimi = input("Anna nimesi? ")
osoite = input("Anna osoitteesi? ")
print(nimi)
print(osoite)

# Tehtävä 102-7: Kirjoita ohjelma, joka kysyy 2-3 asiaa ja tulostaa lyhyen muutaman rivin tarinan, jossa näitä asioita on käytetty.
sankari = input("Kuka on tarinan sankari? ")
roisto = input("Kuka on tarinan roisto? ")
print(sankari + " ratsasti karjatilalle. " + roisto + " ratsasti myös karjatilalle.\n" + sankari + " puhui roistolle, joka lähti karkuun.")

