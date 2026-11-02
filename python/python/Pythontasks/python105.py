"""
# python 105

# Ehtolauseen idea on tarkastaa, jotain ja toimia sen mukaan
# Tarkastus on aina joko tosi (True) tai epätosi (False)
# Tarkastuksen toimitaan halutulla tavalla.

muuttujaAAA = 15

if muuttujaAAA >= 10:
    print(f"MuuttujaAAA on suuri")
# kirjoitettaessa useita komentoja sisennyksen on oltava sama!
    print("vika!")

# Tarkastuksessa tehdään aina vertailu
# >
# <
# >=
# <=
# ==    yhtäsuuri kuin
# !=    erisuuri kuin

muuttujaBBB = 5
if muuttujaBBB == 5:
    print("Sama!")

# tarkastuksessa tutkittavalla muuttujalla on aina oltava arvo!
# Koska tarkastus on aina tosi tai epätosi
# voidaan miettiä vertailuun tilanne jossa toimitaan näin tai noin
# tämä tehdään else: rakenteella

muuttujaCCC = 6
if muuttujaCCC == 5:
    print("Sama!")
else:
    print("Ei sama arvo")

# Boolean arvot ovat tosia tai epätosia
# logiikka toimii samoin kuin yllä

muuttujaBoolean1 = True

if muuttujaBoolean1 == True:
    print("TRUE")

if muuttujaBoolean1:
    print("TRUE")

# Tehtävä 105-1: Tee ohjelma, joka kysyy vuoden ja sanoo syntymävuotesi, jos kyseessä on vuosi jolloin synnyit.
vuosi = int(input("Mikä vuosi? "))
syntymavuosi = 1969
if vuosi == syntymavuosi:
    print("Tämä on syntymävuoteni!")

# Tehtävä 105-2: Tee ohjelma, joka kysyy luvun itseisarvon. Sen on katsottava onko luku pienmpi kuin 0 ja tällöin kertoo luvun -1:llä.
luku = int(input("Anna luku? "))
if luku >= 0:
    print(f"{luku} on positiivinen ja sen itseisarvo on {luku}")
else:
    print(f"{luku} on negatiivinen ja sen itseisarvo on {-luku}")

# Tehtävä 105-3: Tee ohjelma, joka kysyy nimen ja lukumäärän. Nimen ollessa Aapeli, ohjelma sanoo että tässä ilmainen ruoka. Muuten ohjelma sanoo, että annokset maksavat lukumäärä kertaa 5,90 euroa.
nimi = input("Anna nimi? ")
lukumaara = int(input("Anna lukumaara? "))

if nimi == "Aapeli":
    print("Tässä on ilmainen ruoka!")
else:
    print(f"{nimi}! Annokset maksavat {lukumaara} kertaa 5,90 euroa eli {lukumaara*5.90} euroa.")

# Tehtävä 105-4: Ohjelmalle syötetään luku. Se ilmoittaa että luku on pienempi kuin 10/100/1000/10000
luku = int(input("Anna luku? "))
if luku < 10:
    print(f"{luku} on pienempi kuin 10")
if luku < 100:
    print(f"{luku} on pienempi kuin 100")
if luku < 1000:
    print(f"{luku} on pienempi kuin 1000")
if luku < 10000:
    print(f"{luku} on pienempi kuin 10000")
"""

# Tehtävä 105-5: Ohjelmalle syötetään kaksi lukua ja laskentatapa (plus, miinus, kerto, jako). 
# Ohjelma laskee laskentatavan mukaisen tuloksen ja tulostaa sen.
lukuA = int(input("Anna luku A? "))
lukuB = int(input("Anna luku B? "))
laskentatapa = input("Anna laskentatapa? ")

if laskentatapa == "plus":
    print(f"{lukuA} + {lukuB} = {lukuA+lukuB}")
if laskentatapa == "miinus":
    print(f"{lukuA} - {lukuB} = {lukuA-lukuB}")
if laskentatapa == "kerto":
    print(f"{lukuA} * {lukuB} = {lukuA*lukuB}")
if laskentatapa == "jako":
    print(f"{lukuA} / {lukuB} = {lukuA/lukuB}")



