
# python 107

muuttujaAAA = 123

if muuttujaAAA > 200:
	print("200+")
elif muuttujaAAA > 100:
	print("100-200")
else:
	print("alle 100")

# Merkkijonoissa voidaan verrata myös aakkosjärjestystä välillä a-z.
# pienet kirjaimet ovat suurempia kuin isot kirjaimet
# ÅÄÖ on suurempi kuin ABC

muuttujaBBB = "äiti"
muuttujaCCC = "Äiti"

if muuttujaBBB >= muuttujaCCC:
    print(muuttujaBBB)
else:
    print(muuttujaCCC)


# Tehtävä 107-1: Tee ohjelma, joka ilmoittaa monta pistettä tuli jääkiekossa voiton, tasapelin tai tappion tullessa.
# arvot ovat 3, 1 ja 0
pelitulos = "voitto" # voi olla voitto, tasapeli tai tappio
if pelitulos == "voitto":
    print(f"Peli oli {pelitulos}. Se tarkoittaa 3 pistettä.")
elif pelitulos == "tasapeli":
    print(f"Peli oli {pelitulos}. Se tarkoittaa 1 pistettä.")
else:
    print(f"Peli oli {pelitulos}. Se tarkoittaa 0 pistettä.")


# Tehtävä 107-2: Tee ohjelma, johon syötetään 2 lukua, kerro kumpi on suurempi vai oliko kyseessä sama luku.
lukuA = int(input("Anna luku A? "))
lukuB = int(input("Anna luku B? "))
if lukuA > lukuB:
    print(f"{lukuA} on suurempi kuin {lukuB}.")
elif lukuB > lukuA:
    print(f"{lukuB} on suurempi kuin {lukuA}.")
else:
    print(f"{lukuA} ja {lukuB} ovat yhtäsuuret.")

# Tehtävä 107-3: Tee ohjelma, johon syötetään 2 nimeä ja ikää. Kerro kumpi henkilö on vanhempi.
nimiA = int(input("Anna nimi A? "))
lukuA = int(input("Anna ikä A? "))
nimiB = int(input("Anna nimi B? "))
lukuB = int(input("Anna ikä B? "))

if lukuA > lukuB:
    print(f"{nimiA} on vanhempi kuin {nimiB}.")
elif lukuB > lukuA:
    print(f"{nimiB} on vanhempi kuin {nimiA}.")
else:
    print(f"{nimiA} ja {nimiB} ovat yhtä vanhat.")

# Tehtävä 107-4: Tee, ohjelma, johon syötetään kaksi merkkijonoa. Kerro kumpi on ensimmäinen ja viimeinen.
merkkijonoA = input("Anna merkkijono A? ")
merkkijonoB = input("Anna merkkijono B? ")

if merkkijonoA > merkkijonoB:
    print(f"{merkkijonoA} on suurempi")
elif merkkijonoB > merkkijonoA:
    print(f"{merkkijonoB} on suurempi")
else:
    print(f"Kumpikin on yhtä suuri")

