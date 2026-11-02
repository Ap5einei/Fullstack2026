
# python 103

# Milloin luku ei ole luku?
# muuttujilla on tietotyyppi
# tietotyyppi tarkoittaa muuttujan olevan esimerkiksi:
# merkkijono
# numero, esim liukuluku (float) tai kokonaisluku

from tokenize import Number


muuttujaAAA = 123
muuttujaBBB = "123"

# numeron ja merkkijonon aritmetiikka ei toimi
# print(muuttujaAAA + muuttujaBBB)

# merkkijonon ja numeron merkkijono ei toimi
# print(muuttujaBBB + muuttujaAAA)

# f merkkijonolla tulostaminen
# tämä mahdollistaa tulostuksen "fiksusti"

# vanha tapa käyttää castausta
# str() luo merkkijonon
# Number() luo numeron
print("Numero on " + str(muuttujaAAA))

# f merkkijonoa käyttäessä ei tarvita castauksia
print(f"Numero on {muuttujaAAA}")
# periaatteessa {} sisällä voi tehdä aritmetiikkaa
print(f"Numero on {muuttujaAAA + 111}")

# Tehtävä 103-1: Kirjoita ohjelma, joka tulostaa seuraavan f-merkkijonoilla
# Hei olen etunimi sukunimi ja olen X-vuotias.
etunimi = "Aku"
sukunimi = "Ankka"
ika = 313
print(f"Hei olen {etunimi} {sukunimi} ja olen {ika}-vuotias.")

# Tehtävä 103-2: Kirjoita ohjelma, jossa on kaksi muuttujaa x = 123 ja y = 456
"""
Se tulostaa
x + y =
x - y =
x * y =
x / y =
"""
x = 123
y = 456
print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")


