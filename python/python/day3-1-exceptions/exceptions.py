
# Virheenhallinnan lähtökohta on päättää milloin 
# ohjelma saa kaatua ja milloin se ei saa kaatua.

# Oman koodin virheet saa ja pitää kaataa järjestelmän.
# --Koska näin omat virheet ja bugit löytyy heti ja
# --ne saadaan poistettua mahdollisimman nopeasti.
# --Tämä parantaa koodin laatua kehityksen aikana.
# 
# Oman koodin ulkopuolella oleva koodi ja järjestelmät 
# ei saa kaataa omaa kodia missään tapauksessa.
# --Emme voi taata, että rajapintojen ulkopuoliset asiat toimivat.
# --Esim tietokoneen käyttöjärjestelmä, hardware, ostokoodi.
# --Käyttäjälle ilmoitetaan ongelmasta.

# Virheen hallinnassa ei käsitellä oman järjestelmän vikoja.
# Rajapintojen toiminta laitetaan virheenhallintaan.
# Virheenhallinnassa koodin on pysyttävä pystyssä ja 
# ohjelma ei saa missään tapauksessa kaatua.

# Virheenhallinta perustuu ajatukselle, että:
# 1) Tärkeä (rajapinnan) koodi erotetaan try komennon alle
# 2) Vian tullessa mennään except osioon
# 3) Sitten except osiossa vika tiedotetaan raise komennolla.
# 4) Tiedotettu vika käsitellään virheen käsittelyssä.

# Seuraava funktio kuvaa tehtävää, jossa epäonnistuminen
# ei saa kaataa konetta. 
# -Tällaisia tehtäviä ovat tyypillisesti
# rajapinnan yli menevät tehtävät, esim:
# printtaus, IO-tehtävät, tietokantaoperaatiot

# Seuraavassa testissä yritetään avata tiedosto, jota ei ole
# Tiedoston luku on rajapinnan ylittävä toiminta, joten
# tarvitaan virheenkäsittely.
def seurattavafunktio():
   try:
      # Tässä on rajapinnan käsittelyyn liittyvä koodi
      print("Try seurattavafunktio")
      # Tämä käsky luo virheen, koska tiedostoa ei ole
      # virhe on open komennolla aina OSError
      open("roskaajotaeiole")
   except OSError:
      # Except osioon mennään vain, jos try epäonnistui.
      print("Except seurattavafunktio")
      # except osiossa lähetetään virheilmoitus
      # käytetään raise komentoa
      # ilmoituksen tyyppi ja lähetettävä tieto vaihtelevat
      # Tässä se olisi OSError
      raise OSError
      # RuntimeError on "general error"
      # raise RuntimeError
      # TypeError mahdollistaa tietojen siirron ilmoituksen mukana
      # Käytä tätä, jos annat tietoja virheen käsittelylle
      # raise TypeError("Type Error created")
      # Exception on yleistermi erilaisille keskeytyksille
      # Tähän ryhmään kuuluu kaikki toiminnan jotenkin keskeyttävät
      # tapahtumat. Käytetään paljon testauksessa.
      # raise Exception(666)
      # raise Exception(666,"selitys")
   finally:
      # HUOM! Tämä koodi ajetaan oli virhe tai ei.
      # Se ajetaan exceptin jälkeen mutta
      # ennen raisen käsittelyä (virheenkäsittelyssä).
      print("Finally seurattavafunktio")

def seurattavafunktiotoo(arg):
    # https://stackify.com/python-assert-definition-and-best-practices/
    assert arg == 10, "arg must be 10 or less"
    # Periaatteessa raise voidaan käyttää ilman try rakennetta.
    # Tekniikalla voidaan haarukoida mihin koodi kaatuu.
    # Funktion suoritus loppuu siihen.
    raise Exception(0,"ilmoitus")
    # tähän koodiin ei mennä ikinä
    print("koodi, johon ei mennä")


# virheenkäsittelijä osuus

# Virheen käsittelijässä määritetään mitä toimia seurataan.
# Virheestä lmoitus käyttäjälle ja mahdollisia muita toimia.
try:
   seurattavafunktio()
   seurattavafunktiotoo(10)
   #seurattavafunktiotoo(15)

# Saatu except määrää mitä tehdään.
# tavallisesti ilmoitus käyttäjälle, logitus, jne.
except OSError:
   print("I got OSError")
except RuntimeError:
   print("I got RunTimeError")
except TypeError as nimitys:
   print("I got exception", repr(nimitys))
except Exception as exc:
   print(f"Exception oli {exc}")
   print(f"Exception oli {exc.args[0]}")
except:
   print("some other error perhaps?")

finally:
   print("Finally virheenkäsittelijä")

