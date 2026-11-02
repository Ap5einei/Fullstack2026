# Python 109

# ikiluuppi

while True:
    luku = int(input("Anna luku? "))
    if luku == -1:
        break
    print(luku)

# sama käyttämällä boolean operaattoreita

runningloop = True
while runningloop:
    luku = int(input("Anna luku? "))
    if luku == -1:
        runningloop = False
    print(luku)


# nouseva luku
iteraattori = 0
while True:
	print(iteraattori)
	iteraattori = iteraattori + 1
	if iteraattori > 5:
		break

# Kun suunnitellaan luuppia...
#   Ikuinen? 
#   Lähdetäänkö kun ehto tulee täyteen? 
#       Haetaanko montaa asiaa?
#       Riittääkö yksi osuma?
#   Kun X iteraatiota suoritettu?

# Tehtävä 109-1: Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa "ei"
while True:
    vastaus = input("Anna kommentti? ")
    if vastaus == "ei":
        break
    print(vastaus)

# Tehtävä 109-2: Tee toistolause, joka jatkuu kunhan käyttäjä kirjoittaa luvun välillä 1 ja 100.
# 0 lopettaa ja 101+ pitäisi antaa moitteita!

runningloop = True
while runningloop:
    luku = int(input("Anna luku (0 lopettaa)? "))
    if luku == 0:
        print("Hei hei!")
        runningloop = False
    elif luku > 100 or luku < 0:
        print("Luvun pitää olla välillä 1-100...")
    else:
        print(f"Sain luvun {luku}")


# Tehtävä 109-3: Syötä salasana. Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa <salasana>.
salasana = input("Anna salasana? ")
while True:
    vastaus = input("Anna salasana? ")
    if vastaus == salasana:
        break
print("pääsit eteenpäin...")



# Tehtävä 109-4: Syötä salanumero. Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa <salanumero>.
# Pysäytä tehtävä, jos yrityksiä on enemmän kuin kolme.
salanumero = int(input("Anna salanumero? "))
arvauksia = 0
while True:
    vastaus = int(input("Anna salanumero? "))
    arvauksia += 1
    if vastaus == salanumero:
        print("OK")
        break 
    elif arvauksia >= 3:
        print("liikaa yrityksiä")
        break

# Tehtävä 109-5: Tee lähtölaskenta arvosta 8 arvoon 1, jonka jälkeen kirjoita "Laukaisu!"
iteraattori = 8
while True:
	print(iteraattori)
	iteraattori -= 1
	if iteraattori == 0:
		break
print("Laukaisu!")


# Tehtävä 109-5: Tee toistolause, johon syötetään lukuja kunnes käyttäjä kirjoittaa -1. Laske tämän jälkeen keskiarvo.
iteraattori = 0
summa = 0
while True:
    luku = int(input("Anna numero? "))
    if luku == -1:
        break
    summa += luku
    iteraattori += 1
print(f"Keskiarvo on {summa/iteraattori}")

