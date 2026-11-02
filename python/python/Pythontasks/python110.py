
# python 110

# alustus
luku = int(input("Anna luku: "))

# tulosta
while luku < 10:
    print(luku)
#muutos luupin kierroksien välillä
    luku += 1

luku = 1
while luku < 5:
    print(luku)
    luku += 1

# Tehtävä 110-1: Tulosta joka kolmas luku välillä 1 ja 50.
luku = 1
while luku <= 50:
    print(luku)
    luku += 3

# Tehtävä 110-2: Tee uusiksi lähtölaskentatehtävä niin että siinä ei ole 
# while True: riviä vaan jotain muunlainen rivi.
iteraattori = 8
while iteraattori > 0:
	print(iteraattori)
	iteraattori -= 1
print("Laukaisu!")

# Tehtävä 110-3: Tulosta luvut 1stä eteenpäin käyttäjän antamaan lukuun asti.
luku = int(input("Anna luku: "))
iteraattori = 1
while iteraattori < luku:
    print(iteraattori)
    iteraattori+=1

# Tehtävä 110-4: Tulosta aluksi 1 ja sitten seuraava luku niin että se on edellisen luvun arvo kerrottuna kahdella.
iteraattori = 1
while iteraattori < 1000:
    print(iteraattori)
    iteraattori*=2


# Tehtävä 110-5: kysy kaksi lukua ja tulosta sen potenssit arvosta 0 toiseen lukuun asti
lukuA = int(input("Anna lukuA: "))
lukuB = int(input("Anna lukuB: "))
iteraattori = 0
while iteraattori <= lukuB:
    print(f"{lukuA} potenssi {iteraattori} on {lukuA**iteraattori}")
    iteraattori+=1

# Tehtävä 110-6: Kysy käyttäjältä luku ja tee ohjelma joka laskee 1+2+3... kunnes summa on käyttäjältä saatu luku tai sitä pienempi edellinen luku. Näytä tiedot "1+2+3..." tavalla.
luku = int(input("Anna luku: "))
iteraattori = 0
summa = 0
teksti = ""
while summa <= luku:
    summa += iteraattori    
    if (iteraattori == 0):
        teksti = str(iteraattori)
    else:
        teksti = teksti + f"+{iteraattori}" 
    print(f"{iteraattori}: {teksti} = {summa}")
    iteraattori += 1

