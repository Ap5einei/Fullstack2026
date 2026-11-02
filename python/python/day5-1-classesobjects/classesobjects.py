#
# object oriented programming
#

# olio-ohjelmointi = object oriented programming (tai OOP)
# luokka = class
# olio = object

# Luokalla on aina ominaisuuksia ja toimintoja
# 1) ominaisuudet ovat luokassa määritettyjä muuttujia
# 2) toiminnat ovat funktioita, joilla luokan jäsenet 
# tekevät jotain

# Luokkien käytön ensimmäinen sääntö:
# luokan avulla rakennetaan olioita.
# luokka on siis malli, sapluuna eli jigi.
# olio on mallin mukaan luotu yksittäinen asia.

# Luokkien käytön toinen sääntö:
# Olio on aina erillinen toisesta oliosta.
# Oliot elävät omaa elämää muista olioista riippumatta.
# Olion ominaisuudet voivat saada uusia arvoja sen elinaikana.

#Luokkien käytön kolmas sääntö:
# Luokissa määritetään myös toimintoja (funktioita/metodeita).
# Näin kukin erillinen olio tekee mitä sen pitää tehdä.
# Olion toiminta on muista olioista riippumatonta.
# Toimnnoilla olion sisäisiä tietoja käytetään halutun 
# toiminnan saavuttamiseksi.
# Toiminnat keskittyvät siihen mitä olion pitäisi pystyä tekemään.
# Muita toimintoja ei tarvitse eikä pidä tukea!

# Olio-ohjelmoinnin A ja O on suunnittelu
# Periaatteessa kaikki luokat on suunniteltava etukäteen
# SUUNNITTELUSSA MENNÄÄN TOIMINNAT EDELLÄ.
# OMINAISUUDET VALITAAN NIIN, ETTÄ NE MAHDOLLISTAVAT TOIMINNAT

# esimerkiksi teemme kirjaston, jossa on asiakkaita.
# Asiakas luokka
# Sen on pystyttävä:
# Etsiä kirjoja
# Lainata ja palauttaa kirjoja
# Maksaa sakot
# --> Jokainen näistä asioista on toiminnallisuus eli metodi/funktio

# Seuraavaksi mietitään ominaisuudet, jotka tukevat toimintoja
# Esim Kirja luokka:
# Tekijä
# sivujenmäärä
# julkaisuvuosi
# Nimi
# ISBN/ISSN numero

# Olio ohjelmoinnin perusta on luokkien suunnittelu.
# Suunnittelu toimii yksinkertaisesti seuraavasti:
# 1) Kuka on toimija tai toiminto/prosessi? --> Luokka
# 2) Mitä toimija tekee? --> Luokalle määritettävät metodit
# 3) Millä arvoilla tehdään? --> Luokalle määritettävät ominaisuudet

# Onko muita ominaisuuksia? 
# --> Luokalle määritetään "elämää helpottavat" ominaisuudet
# ---> Nämä ominaisuudet liittyvät "työpaikan hiljaiseen tietoon"
# ---> Hiljaista tietoa saa vain haastattelemalla toimijoita.

# you can approach class in different ways

# CASE 1: an object with class that has only properties
class Kokeilu:
    # you can create an object with class
    # that has only properties
    someproperty = ""

myObject = Kokeilu()
myObject.someproperty = "Aku Ankka"

myObjectB = Kokeilu()
myObjectB.someproperty = "Iines Ankka"

# however, can you create additional properties dynamically?
# nowadays this is possible, not in old Python versions
myObject.somepropertytoo = "Aku Ankka too"
print(myObject.someproperty)
print(myObject.somepropertytoo) # did not always work

print(myObject.someproperty, myObject.somepropertytoo)
print(myObjectB.someproperty)

# We can thus create class that has only properties.
# it can also add dynamically new properties.
# this is fairly similar to "struct" in most programming languages

# You can actually give function as property
# this allows functionality with use of properties
myObject.funktio = lambda aa,bb : aa + " " + bb
print(myObject.funktio("Hello","World!"))
print(myObject.funktio("Minni","Hiiri"))
del myObject

# the combination of properties and functionality is b asis
# of all classes and most structs ssupport this in languages
# However, this is bad python coding

"""
Miksi käyttäisit luokkaa, jos siinä on vain ominaisuuksia?
Dictionary tekee saman asian ja siihen voi dynaamisesti lisätä
avain-arvo pareja!
esimerkki alla:
"""

myObj = {
#    "Hello": "World"
}
# dictionary allows adding properties dynamically
# Modifying the "Hello" property
myObj["Hello"] = "Python"
# Adding testi property
myObj["testi"] = "Kalle"

# Printing the modified property
print(myObj["Hello"])
print(myObj["testi"])
del myObj

# You can even give functions as properties to dictionaries
myObj = {
    "Hello": lambda aa,bb : aa + " " + bb
}
print(myObj["Hello"]("Hello","World!"))


# Thus avoid using class if you already can use dictionary
# instead you should use class when most important aspect
# of classes should be used: inheritance

#
# Now we create a class and object 
#

# luokka määritetään sanalla class
# Luokan nimi on vapaa ja kirjoitetaan yleensä isolla etukirjaimella.
# class on varattu sana. Sitä ei saa käyttää.
class kokeiluluokka:
    # This is a constructor for creation of object of class
    def __init__(self) -> None:
        # Here we initialize properties
        self.koe = ""

kokeiluluokanolio = kokeiluluokka()
kokeiluluokanolio.koe = "koe"
print(kokeiluluokanolio.koe)

class Eläin:
    # luokalla on aina konstruktori eli kuinka se rakennetaan.
    # oliota luodessa konstruktori ajetaan luodulle oliolle
    def __init__(self) -> None:
        # Tähän laitetaan kaikki alustamiseen liittyvät asiat
        # eli ominaisuudet esitellään ja annetaan alkuarvot
        self.nimi = "Eläin"

elukka1 = Eläin()
elukka1.nimi = "Sylvi"
print(elukka1.nimi)
elukka2 = Eläin()
print(elukka2.nimi)

#
# class constructors and functionality
#

# Konstruktorin käytön perusajatus on asettaa arvoja
# oliota luodessa.
# Periaatteessa konstruktorin argumentit voi jättää 
# kokonaan pois, jos luokka sisältää aina samat alkuarvot. 
# Tämä on kuitenkin hyvin harvinaista.

class Kissa:
    def __init__(self, rotu, nimi, sukupuoli, ikä) -> None:
        # Tässä on olion ominaisuuksia, joille annetaan alkuarvo
        # arvo määritetään kutsuessa Kissa() 
        self.rotu = rotu
        self.nimi = nimi
        self.sukupuoli = sukupuoli
        self.ikä = ikä

    # toimintoja tehdessä self määrittää, että voidaan käyttää 
    # olion omia ominaisuuksia
    def kävelee(self):
        print(f"{self.nimi} kävelee")
    # toiminnoilla voi olla myös parametrejä
    def kehrää(self, kuvaus):
        print(f"Kissa kehrää {kuvaus}...")

kissa1 = Kissa("","Jenny","F",13)

# kutsussa sanaa self ei tarvita
kissa1.kävelee()
kissa1.kehrää("iloisesti")


# Tehtävä 1 - luo kaksi kissaa lisää
# anna niille ominaisuuksia, muuta niitä ja kutsu funktioita
kissa2 = Kissa("Katti","Kali","M",16)
kissa3 = Kissa("Katti","Galileo","M",16)
kissa3.ikä = 14
kissa3.kehrää("")

# Use of constructor arguments thus allows using same 
# class template to create different kinds of objects.

# as a matter of fact Python has Default Constructor
# It creates object of class
class MyExampleD:
    # attributes
    # This class level property is actually copied into
    # object level property too.
    name = "Iines"
    # thus any object will have both instance and class
    # level variables of same name!

    def sayname(self):
        print("Hello", self.name)

ex5 = MyExampleD()
print(MyExampleD.name) # Iines
print(ex5.name) # Iines
ex5.sayname() # Hello Iines

ex6 = MyExampleD()
ex6.name = "Mikko"
print(MyExampleD.name) # Iines
print(ex5.name) # Iines
print(ex6.name) # Mikko
ex5.sayname() # Hello Iines
ex6.sayname() # Hello Mikko


# Conclusion!
# If you do not have default constructor,
# Python will create one

# It will create attributes that seem like
# class level attributes into object level 
# attributes

# Note! ALWAYS USE CONSTRUCTOR!
# It makes obvious what level attributes are!

#
# Note! MULTIPLE CONSTRUCTORS ARE NOT SUPPORTED!
# https://realpython.com/python-multiple-constructors/
#

#
# class ja instance level properties
#

# Periaatteessa property voidaan määrittää myös 
# class tasoisena eikä sitä tarvitse asettaa 
# konstruktorissa.

class Kokeilu:
    # Here we have two properties
    someproperty = "Aku Ankka"
 
    # this function is constructor again
    def __init__(self):
        # we set initial value as Iines Ankka
        self.someproperty = "Iines Ankka"
    
    def sanonimi(self):
        print(f"Nimeni on {self.someproperty}!")

myObject = Kokeilu()
myObject.sanonimi()
myObject.someproperty = "Hessu Hopo"
myObject.sanonimi()
myObject2 = Kokeilu()
myObject2.sanonimi()
myObject2.someproperty = "Hannu Hanhi"
myObject2.sanonimi()
del myObject
del myObject2
# Putting properties to class level allows setting 
print(Kokeilu.someproperty) # tämä on luokkatasoinen tieto

# Why we want class and instance level properties?

# 1) instance variables (oliotasoinen).
# They are object level and object based variables.
# thus every car has their own color.

# 2) class variable is used on class level (luokkatasoinen).
# they work independently of any class methods
# they are used by writing following:
# <classname>.<variablename>
# They are written directly under class

class Testi:
    mypropertyA = 111
    mypropertyB = 222
print(Testi.mypropertyA, Testi.mypropertyA)

# Thus we almost always use __init__ to set object level variables 
# and use class to set class level variables.

# there are two basic use cases:
# first, variable is same to all class objects 
# thus idea is to use it like a constant
# However, there is no constant in Python! BEWARE!
# This allows creation of key-value pairs similar 
# to enumerated lists or dictionaries

class JanneMath:
    PIINARVO = 3 # class level variable not constant!

    # vakio funktiolla
    def PII():
        return 3.14111

    # vakio funktiolla   
    MYPII = lambda : 3.14999

print(JanneMath.PIINARVO)
JanneMath.PIINARVO = 3.14
print(JanneMath.PIINARVO) # now it is 3.14

print(JanneMath.PII()) # 3.14111
print(JanneMath.MYPII()) # 3.14111

# importing pi from math library allows changing its value
# This is because Python does not have constants
import math
math.pi = 3 # Yes, this is legal but very stupid programming
print(math.pi) # 3

# second, it is used as internal counter for class
# see example belows
class MyExampleA:
    # this is a class variable
    number = 1

    # this is constructor
    def __init__(self, arg):
        # this is instance variable
        self.arg = arg
        # here we manipulate class variable
        # <classname>.<classvariablename>
        MyExampleA.number += 100        

# luokkatason muuttuja kutsutaan:
# <luokan nimi>.<muuttuja>        
print(MyExampleA.number) # 1

ex1 = MyExampleA(1234)
print(ex1.arg) # 1234
print(MyExampleA.number) # 101

ex2 = MyExampleA(5678)
print(ex2.arg) # 5678
print(MyExampleA.number) # 201

class CellPhone:
    sarjanumero = 1001
#    myserialnumber = 0
    def __init__(self) -> None:
        CellPhone.sarjanumero += 10
        self.myserialnumber = CellPhone.sarjanumero

cell1 = CellPhone()
cell2 = CellPhone()
cell3 = CellPhone()
cell4 = CellPhone()
cell5 = CellPhone()

print("Känny 2", cell2.myserialnumber) # 1021
print("Känny 5", cell5.myserialnumber) # 1051
print(CellPhone.sarjanumero) # 1051

# Eli mitä opimme tästä?
# 1) luokkatasoinen muuttuja ei voi olla vakio!
# Vakion luonti vaatii käytännössä aina funktion.

# 2) Luokka, jossa on vain luokkatasoisia muuttujia eikä toimintaa, on turha
# käytä tällöin joko dictionarya tai enumerated listaa.

# 3) Luokkatasoinen muuttuja on usein tarkoitettu kuvaamaan luokkaa yleensä.
# Eli sellaisia ominaisuuksia, jotka ovat samat kaikille luokan jäsenille.
# Tämä voisi olla esimerkiksi auton merkki, joka ei muutu auton olemassaolon aikana.

# 4) Luokkatason muuttuja on hyvä toimimaan sisäisenä laskurina.
# So toimii luokkien kanssa kuin funktioissa oleva yield

#
# built-in class functions
#

# getattr()
# setattr()
# delattr()
# hasattr()

# voit puukottaa frameworkkejä näillä
# hyvin harvinaisia tilanteita

# this shows functions
class MyExampleE:
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

ex7 = MyExampleE(123,456)

# get info based on attribute use
print(getattr(ex7,"arg1")) # 123
print(ex7.arg1)
print(getattr(ex7,"arg2")) # 456
print(ex7.arg2)

# ex7.arg1 = 11111
setattr(ex7,"arg1", 11111)
print(getattr(ex7,"arg1")) # 11111

print(hasattr(ex7,"arg1")) # True
print(hasattr(ex7,"arg3")) # False

delattr(ex7,"arg2")
print(hasattr(ex7,"arg2")) # False

# this prints out class documentation
print(ex7.__doc__) # None

# this prints out class data as attributes - value pairs
print(ex7.__dict__) # {'arg1': 11111}

# this prints out class name of object
print(ex7.__class__.__name__) # MyExampleE

# this prints out class module
print(ex7.__module__) # __main__
print(math.acos.__module__) # math


