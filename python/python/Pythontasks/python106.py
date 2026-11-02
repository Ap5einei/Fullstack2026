
# Python 106

# len() ilmoittaa pituuden

muuttujaAAA = "kukkakauppias"
muuttujaBBB = ""
muuttujaCCC = 1234
muuttujaDDD = 1234.56
muuttujaEEE = True

print(len(muuttujaAAA))
print(len(muuttujaBBB))
# print(len(muuttujaCCC)) kokonaisluvulla EI ole pituutta
# print(len(muuttujaDDD)) liukuluvulla EI ole pituutta
# print(len(muuttujaEEE)) boolean arvoilla ei ole pituutta

muuttujaKKK = "aarne"
muuttujaLLL = "123"
muuttujaMMM = "123.45"
muuttunaNNN = 123
muuttunaOOO = 123.45

# cast "caastaus" on termi, joka kutaa tietotyypin
# muuttamista yhdestä tyypistä toiseksi
# int() muuttaa tietotyypin kokonaisluvuksi
# float() muuttaa tietotyypin liukuluvuksi
# str() muuttaa tietotyypin merkkijonoksi

# tulosAAA = float(muuttujaKKK) kirjaimia ei voi muuttaa numeroksi
tulosBBB = float(muuttujaLLL)
tulosCCC = float(muuttujaMMM)
tulosDDD = int(muuttujaLLL)
# tulosEEE = int(muuttujaMMM) # muutos "123.45" -> ei onnistu
# tämä on mahdollista, koska komento, joka palauttaa jotain, voi 
# olla seuraavan komennon syöttöarvo
tulosEEE = int(float(muuttujaMMM)) # muutos "123.45" -> 123.45 -> 123

# käytännössä muutos stringiksi onnistuu aina
print(str(tulosEEE))

# VAROITUS Tässä näkyy että cast voi muuttaa tulosta!
luku = 123.55
print(float(int(luku)))

# Tehtävä 106-1: Tee ohjelma, jossa kirjoitetaan merkkijono ja ilmoitetaan sen pituus.
merkkijono = "Ankkalinna"
print(f"{merkkijono} merkkijonon pituus on {len(merkkijono)}.")

# Tehtävä 106-2: Tee ohjelma, jossa kirjoitetaan liukuluku ja ohjelma ilmoittaa sen pyöristyksen kokonaisluvuksi.
liukuluku = 5678.89
print(f"{liukuluku} liukuluvun pyöristys on {int(liukuluku)} ja oikeasti {round(liukuluku)}.")

# Tehtävä 106-3: Tee ohjelma, jolle syötetään luku Celsiusasteina. Ohjelma ilmoittaa arvon Fahrenheitteina. Etsi kaava netistä.
# kaava on (Celsius * 1.8) + 32 = Fahrenheit
celsius = float(input("Anna lämpötila Celsius-asteina? "))
print(f"{celsius} astetta Celsiusta on { (celsius*1.8) + 32 } astetta Fahrenheit.")

