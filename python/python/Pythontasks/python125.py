# Python 125
# ==========

# Errors

"""
ValueError
TypeError
IndexError
ZeroDivisionError

FileNotFoundError
io.UnsupportedOperation
PermissionError 


try:
	jotain
	raise ValueError("juttua...")
	
except FileNotFoundError:
	jotain

except TypeError:
	jotain

except:
	jotain

else:

finally:
"""

# perustapaus on tryn sisällä yrittää jotain
# ja virheen tullessa esittää se except sisällä
# tryn sisällä oleva virhe EI kaada konetta vaan
# se hyppää virhekohdasta suoraan jatkamaan except kohtaa.
try:
    x = 5 / 0
    print("Koodi, johon ei mennä?")
except:
    print("Errori tuli")

# erilaisia virheilmoituksia on valtavasti
# tässä käsitellään muutama
# virheilmoitukset asetetaan jonoksi ja lopuksi tulee
# ilmoitus ilman virhetyyppiä
# ---> se on "general error"
try:
    x = 5 / 0
    print("Koodi, johon ei mennä?")
except ZeroDivisionError:
    print("yritit jakaa nollalla!")
except:
    print("Errori tuli")

# Virheilmoitus voidaan luoda tyhjästä.
# Näin tehdään, kun halutaan omanlainen ilmoitus
# raise luo virheen ja sen tyyppi voidaan määrittää
try:
    x = 5 / 2
    raise ValueError(x)
    print("Koodi, johon ei mennä?")
except ValueError:
    print("raisella tullut value error")
except:
    print("Sain special errorin? ")
    
# try - except on kaksi muuta termia
# except kun jokin epäonnistuu try sisällä
# else kun kaikki onnistuu tryn sisällä
# finally, johon mennään aina
try:
    x = 5 / 2
#    x = 5 / 0
except ZeroDivisionError:
    print("Virhe tuli")
except:
    print("Virhe tuli")
else:
    print("Kaikki OK!")
    try:
        y = 5 / 0
    except:
        print("toinen virhe!")
finally:
    print("Lopuksi mennään aina tänne")




# Tehtävä 125-1: Lisää tiedoston käsittelyyn try - except rakenne

# Tehtävä 125-2: Tee numeron luku, joka sallii luvut välillä 1-100 ja nostaa virheen muuten


