# Python 123
# ==========

# yksinkertaisin ratkaisu on lukea koko tiedosto kerralla
# pysäyttää muun toiminnan, suurilla tiedostoilla vaikea
with open("testi.txt") as tiedosto:
    teksti = tiedosto.read()
    print(teksti)

lista = []
with open("C:\\opikoodiaK2022oulu\\python\\testi.txt") as tiedosto:
    for rivi in tiedosto:
        lista.append(rivi)
        print(rivi)

lista =[]
with open("testi.csv") as tiedosto:
    for rivi in tiedosto:
        sanalista = rivi.split(";")
        dummy = []
        for sana in sanalista:
# \n pääsee eroon .strip() lauseella voit kokeilla myös .replace lausetta
#            dummy.append(sana.replace("\n",""))
            dummy.append(sana.strip())
        lista.append(dummy)
print(lista)	

# Tehtävä 123-1: Tee tiedosto, jossa on monta riviä numeroita. Lue se ja tulosta numerot.
lista = []
with open("numero.txt") as tiedosto:
    for rivi in tiedosto:
        lista.append(int(rivi))
        print(rivi)
print(lista)

# Tehtävä 123-2: Tee .csv tiedosto, jossa on monta riviä ";" erotettuja sanoja. 
# Lue se ja luo lista sanoista.

# katso vastaus alla

# Tehtävä 123-3: Tee .csv tiedosto, jossa on monta riviä ";" erotettuja 
# sanoja sekä välilyöntejä. Lue se ja luo lista sanoista. Poista 
# rivinvaihdot ja turhat välilyönnit.

lista =[]
with open("teksti.csv") as tiedosto:
    for rivi in tiedosto:
        sanalista = rivi.split(";")
        dummy = []
        for sana in sanalista:
            dummy.append(sana.strip())
        lista.append(dummy)
print(lista)	

# Tehtävä 123-4: Yhdistä kahden .csv tiedoston sisällöt 
# ja tee niistä listan arvoja.

# nyrkkisääntönä tiedosto on resurssi
# monen käyttäjän tapauksessa, kukin käyttäjä 
# pitäisi käyttää sitä mahdollisimman vähän.
# Eli avataan, luetaan ja suljetaan yksi kerrallaan
	
lista =[]
with open("testi.csv") as tiedosto:
    for rivi in tiedosto:
        sanalista = rivi.split(";")
        dummy = []
        for sana in sanalista:
            dummy.append(sana.strip())
        lista.append(dummy)

with open("teksti.csv") as tiedosto:
    for rivi in tiedosto:
        sanalista = rivi.split(";")
        dummy = []
        for sana in sanalista:
            dummy.append(sana.strip())
        lista.append(dummy)

print(lista)	

