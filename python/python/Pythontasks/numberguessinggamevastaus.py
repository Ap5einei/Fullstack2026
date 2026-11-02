#
# Tee pythonilla number guessing game
# Kone arpoo luvun välillä 1-100
# tämän jälkeen pelaaja arvaa
# Kone ilmoittaa onko oikea luku suurempi tai pienempi
# jos on lähellä -+5 niin sanoo että polttaa...
#
# Lisätkää itse seuraavat:
# Laskuri, joka kertoo monta arvausta tehtävään meni
# Peli kysyy halutaanko uusi peli
#


import random

# randomille voidaan antaa numero, jolloin se toimii aina
# samalla tavalla, esim 42.
# jos seed jätetään tyhjäksi otetaan arvo systeemin kellosta
random.seed() 

# Vakiot
ALKU = 1
LOPPU = 100
POLTTAA = 5


# pelataanko peliä yleensäkään?
pelataanko_OK = True
while pelataanko_OK:
    # komea otsikko
    print("N U M B E R   G U E S S I N G   G A M E !")
    print("=========================================")

    # kehitellään arvonta
    arvottuluku = random.randint(ALKU, LOPPU)
    print(arvottuluku)

    # resetoidaan laskuri
    laskuri = 0

    # pelillä on luuppi, jossa:
    # kysytään arvaus
    # arvioidaan arvaus
    peli_Voitettu_OK = False
    while not peli_Voitettu_OK:
        # kysely eli pelaajan arvaus
        # jotenkin talteen arvaus
        arvaus_OK = False
        while not arvaus_OK:
            # try except (vastaa try - catch rakennetta)
            # try sisällä on koodi, joka saattaa epäonnistua mutta halutaan
            # että ohjelma pysyy pystyssä.
            # Tämä tehdään yleensä rajapinnoissa (tietokanta, internet, printteri...)
            # except toteuttaa tilanteen, jos tryn sisällä oleva koodi on epäonnistunut
            # hyppy try --> except tapahtuu sillä rivillä, jossa vika tapahtuu
            try:
                arvaus = int(input(f"Anna luku välillä {ALKU} ja {LOPPU}: "))
                # vaihtoehtoinen vertaus
                # if ALKU <= arvaus <= LOPPU:
                if arvaus >= ALKU and arvaus <= LOPPU:
                    arvaus_OK = True
                    laskuri += 1
                else:
                    print(f"Luvun on oltava välillä {ALKU} ja {LOPPU}")
            except:
                print("Syötetty arvo ei ollut numero!")
        
        print(arvaus)

        # vertailu
        # palaute onko lähellä
        print(f"Arvauksia on nyt tehty {laskuri} kappaletta")
        if arvaus == arvottuluku:
            print(f"Luku on {arvottuluku}, jota etsittiin!")
            peli_Voitettu_OK = True
        else:
            if arvaus > arvottuluku:
                print("Luku on pienempi!")
            else:
                print("Luku on suurempi")
            if abs(arvaus - arvottuluku) <= POLTTAA: # abs() tarkoittaa itseisarvoa
                print("Polttaa!!!")

        if laskuri > 10:
            print("Hävisit pelin!")
            break

    dummy = input("Pelataanko uusi peli? K tai k")
    if dummy != 'k' and dummy != 'K':
        pelataanko_OK = False




