
#  
# Classes continue...
#
# Inheritance
# 
# Luokka ei välttämättä pysty venymään kaikkeen
# Toimintojen kasautuminen lisää monimutkaistumista!
# Yleensä se tarkoittaa erikoistapauksia ja -tilanteita.
# --> Tällöin käytetään perintää, jotta itse luokka 
# pysyy yksinkertaisena.
# --> Lapsiluokkaan tehdään ne muutokset, jotka 
# mahdollistavat erikoistapauksen.

class Kissa:
    def __init__(self, rotu, nimi, sukupuoli, ikä) -> None:
        # Tässä on olion ominaisuuksia, joille annetaan alkuarvo
        # arvo määritetään kutsuessa Kissa() 
        self.rotu = rotu
        self.nimi = nimi
        self.sukupuoli = sukupuoli
        self.ikä = ikä

    # toimintoja tehdessä self määrittää, että voidaan käyttää omia ominaisuuksia
    def kävelee(self):
        print(f"{self.nimi} kävelee")
    # toiminnoilla voi olla myös parametrejä
    def kehrää(self, kuvaus):
        print(f"Kissa kehrää {kuvaus}...")

kissa1 = Kissa("","Jenny","F",13)

# kutsussa sanaa self ei tarvita
kissa1.kävelee()
kissa1.kehrää("iloisesti")

# Luodaan kaksi kissaa lisää
kissa2 = Kissa("Katti","Kali","M",16)
kissa3 = Kissa("Katti","Galileo","M",16)
kissa3.ikä = 14
kissa3.kävelee()
kissa3.kehrää("")

# lapsiluokka luodaan <lapsiluokan nimi> (<äitiluokan nimi>)
# Siamilainen luokka perii Kissa luokan
class Siamilainen (Kissa):
    def __init__(self, rotu, nimi, sukupuoli, ikä, laatu) -> None:
        # lapsiluokkaa luodessa, se kutsuu aluksi äitiluokan konstruktoria
        # Tämä käyttää funktiota super(), joka viittaa äitiluokkaan
        super().__init__(rotu, nimi, sukupuoli, ikä)
        # tämän jälkeen konstruktori rakennetaan lapsiluokan asioille.
        # Tekniikka on sama kuin yhden luokan yhteydessä.
        self.rotu = "Siamilainen"
        self.laatu = laatu

    # Leijonanosa perivän luokan koodista on äiti-luokan muokkausta.
    # Tämä tarkoittaa kahta asiaa:
    # 1) override eli uudelleen implementointi
    # --> äitiluokan metodi kirjoitetaan uusiksi
    # 2) uusien metodien lisääminen
    # --> kirjoitetaan aivan uusia metodeja
    # 3) "Turhiin metodeihin" ei tarvitse ottaa kantaa.
    # --> ne toimivat kuten äiti toimii

    # tämä on uusi toiminto, jota EI ole äitiluokassa
    # it is simply added just like any other function.
    def kilpailee(self):
        print(f"{self.nimi} kilpailee ja laatu on {self.laatu}!")

    # perivä luokka voi myös muuttaa toiminnallisuutta äidistä
    # overriden idea on yleensä säilyttää sama function signature.
    # Tällöin funktion nimi ja argumentit ovat samat sekä
    # äidillä että lapsella.
    # Tämä puolestaan mahdollistaa polyformismin.
    # Tällöin sama funktiokutsu toimii sekä äitiluokan 
    # että lapsiluokan metodikutsuissa. 
    # Katso esimerkki alla.
    def kehrää(self, kuvaus):
        # Yleensä teemme omaa toiminnallisuutta!
        print(f"Siamilainen {self.nimi} kehrää {kuvaus}...")
        # Joskus halutaan kuitenkin kutsua äitiluokan metodeja
        # tällöin otetaan kiinni äitiluokkaan super() metodilla.
        # tässä kutsutaan äitiluokan kehrää(kuvaus) funktiota
        super().kehrää(kuvaus)  

siamilainen1 = Siamilainen("Siamilainen","Leonardo","M", 1, "erinomainen")
# perivä luokka perii äidin ominaisuudet ja toiminnat
siamilainen1.kävelee()
# perivällä luokalla voi olla uusia toimintoja, 
# joita käytetään kuten toimintoja yleensäkin
siamilainen1.kilpailee()
siamilainen1.kehrää("kauniisti")

# perintää voi ketjuttaa loputtomasti.
# lapsen alla voi olla toinen lapsi...
class ErikoisSiamilainen (Siamilainen):
    def __init__(self, rotu, nimi, sukupuoli, ikä, laatu) -> None:
        super().__init__(rotu, nimi, sukupuoli, ikä, laatu)

    def kehrää(self, kuvaus):
        print("Erikoissiamilainen näyttää!")
        super().kehrää(kuvaus)

erikoissiamilainen = ErikoisSiamilainen("Erikoissiamilainen","Galileo","M",111,"Excellent")
erikoissiamilainen.kehrää("erikoissiamilaisesti")

# Polymorphismi liittyy perintään.
# Se tarkoittaa toiminnallisuuden periytymisen vaikutuksia.
# Perusajatus on, että lapsiluokilla on yhteisiä toimintoja 
# Esimerkiksi kaikilla graafisilla elementeillä se on piirtäminen!

# Polyforphismin idea on rakentaa perinnän mukaisesti
# funktioita, joilla on sama signature ja joita voidaan
# näin kutsua helposti.

print("-------------------------")
kissalista = []
kissaluokat = (Kissa, Siamilainen, ErikoisSiamilainen)

def lisääoliolistaan(olio: object, lista: list, luokat: tuple) -> bool:
    if isinstance(olio, luokat):
        lista.append(olio)
        return True
    return False

lisääoliolistaan(kissa1,kissalista,kissaluokat)
lisääoliolistaan(kissa2,kissalista,kissaluokat)
lisääoliolistaan(kissa3,kissalista,kissaluokat)
lisääoliolistaan(siamilainen1,kissalista,kissaluokat)
lisääoliolistaan(erikoissiamilainen,kissalista,kissaluokat)

for kissa in kissalista:
    kissa.kehrää("kauniisti")

#
# Multiple mother classes
#
 
# We need to do a lot of classes first

class Fish:
    def __init__(self, weight, species):
        self.weight = weight
        self.species = species
    # This function is inherited to child classes
    # They use this function
    def swim(self):
        print("Fish swims...")
    # This function is inherited by child
    # however, it is overridden by child (see Shark)
    def eat(self):
        print("Fish eats plankton")
    
# child class uses syntax:
# class <childclassname> (<motherclassname>):     
class Shark(Fish):
    # This function is inherited from mother
    # however, it is overridden by child
    # Thus this function is used instead 
    def eat(self):
        print("Shark eats Fish")        
    # this function is present only in Shark
    # it is thus usable only in Shark
    def test(self):
        print("test message")

happyfish = Fish(1,"fish")
happyshark = Shark(10, "shark")
print(happyfish.species)
print(happyshark.species)
# child uses same method as parent
happyfish.swim() # Fish swims...
happyshark.swim() # Fish swims...
# child overrides mother's method
happyfish.eat() # Fish eats plankton
happyshark.eat() # Shark eats fish
# child has special function not present in mother
# happyfish.test()
happyshark.test() # test message

# 2) child class is aggregate of multiple mothers
# we assume there is a class Bird
class Bird:
    def __init__(self) -> None:
        self.birdlife = "Yes"

    def fly(self):
        print("Bird flies...")
    # this command is present in both Bird and Fish
    # Order of preference in case of same method is 
    # order of mother classes in class definition
    # here it is Fish, Bird
    def eat(self):
        print("Bird eats worm")


# This is a case of multiple inheritance
# child class inherits from two mother classes
# class <childclassname> (<list of mothers>):
# Most important decision is order of mothers
# first mother of list has priority.
# See example after this example.
class BirdFish(Fish, Bird ):
    def lookstrange(self):
        print("BirdFish looks strange...")

flyingshark = BirdFish(111, "lentohai")
flyingshark.eat() # Fish eats plankton, Bird is ignored
flyingshark.fly() # Bird flies...
flyingshark.lookstrange() # BirdFish looks strange...
flyingshark.swim() # Fish swims...

# multiple inheritance is dangerous! Do you know why?
# Well, yes and no.
# Python does not have problem here because first mother
# is given preference in inheritance
class MotherA:
    def name(self) -> str:
        return "MotherA"

class MotherB:
    def name(self) -> str:
        return "MotherB"

class ChildAB (MotherA, MotherB):
#class ChildAB (MotherB, MotherA):
    pass

mychildAB = ChildAB()
print(mychildAB.name()) # MotherA
del mychildAB

# Howabout diamond inheritance?
# lets see same again using diamond inheritance...
# https://stackoverflow.com/questions/46199975/resolving-diamond-inheritance-within-python-classes

# It works in diamond as well! Happy times?

class GrandMother:
    def name(self) -> str:
        return "Grandmother"
    def nameToo(self) -> str:
        return "Grandmother222"

class MotherAToo(GrandMother):
    def name(self) -> str:
        return "MotherAToo"

class MotherBToo(GrandMother):
    def name(self) -> str:
        return "MotherBToo"

class ChildABToo (MotherAToo, MotherBToo):
    def nameB(self) -> str:
        # you can select which mother you call
        # You must set self to point mother class you want to use
        return MotherBToo.name(self=MotherBToo)

mychildABToo = ChildABToo()
print(mychildABToo.nameToo()) # Grandmother222
print(mychildABToo.name()) # MotherAToo
print(mychildABToo.nameB()) # MotherBToo

# Well, no...

# Can I get to MotherBToo material?
# not really. It requires some changing of self.
#https://stackoverflow.com/questions/3810410/python-multiple-inheritance-from-different-paths-with-same-method-name

# miten käytän __new__ taikasanaa
# käytännössä kaksiosainen olion luonti
# https://builtin.com/data-science/new-python
# https://stackoverflow.com/questions/70287105/what-are-the-other-uses-of-new-method-in-python

#
# encapsulation
#

# Python has support for hidden attributes but 
# no elaborate support for public, protected 
# and private visibility.

# use __<variablename> to create attribute that
# can only be used within class
# This is similar to "private" in other languages

# here employee count increases by one
# whenever we add a new employee
class Employee:
    # this is a hidden value
    __count = 0
    
    def __init__(self):
        Employee.__count += 1

    # attribute value can only be accessed indirectly
    def showemployeeinfo(self):
        print("Headcount: ", Employee.__count)

aku = Employee()
hannu = Employee()
hannu.showemployeeinfo() # Headcount: 2
# print(hannu.__count) # causes error
# print(Employee.__count) # causes error

# does it work with object level attributes?
# lets try... (and yes it does!)

class Thing:
    def __init__(self,name,value) -> None:
        self.name = name
        self.__value = value

    def statevalue(self):
        return self.__value

koe = Thing("esine",12345)
print(koe.name) # esine
# print(koe.__value) # causes error
print(koe.statevalue()) # 12345

#
# data abstraction, aka interface and abstract classes
#

# requires use of abc module (see above)
# use syntax class <classname>(abc.ABC):
#from abc import ABC, abstractmethod
import abc

# Python implements "abstract class" in computer science.
# It means class that cannot be instantiated.
# However, it is used to form a common template
# which is implemented by multiple roughly similar classes.
# I.e. we define that certain functionality is implemented
# with functions that have certain signature.
# abstract class can have normal and abstract methods.

# Car is abstract class that forms a common template
# to all different car types.
# All abstract classes are created by inheriting 
# from ABC helper class of abc module.
class Car(abc.ABC):
#class Car(ABC):
    # abstract classes do not need constructor (__init__) method.
    # Objects are not created.
    # Python creates default constructor that inheriting classes
    # will refer to.
    
    # abstract classes have always some methods that must
    # be implemented in child classes:
    # 1) abstract methods
    # 2) ordinary methods

    # Abstract methods must be declared with 
    # @abc.abstractmethod attribute.
    # Each attribute is added before each method.
    # Abstract method has no implementation because it 
    # is always overridden in the inheriting class.
    # Thus we always use pass.

    @abc.abstractmethod
    #@abstractmethod
    def mileage(self):
        pass

    # Ordinary methods work as methods in general. :)
    # They may or may not be overridden in inheriting classes.
    # They have ordinary function body and implementation.
    def drives(self):
        print("Car drives...")

# this is a car type MyCar inheriting from abstract class Car
class MyCar(Car):
    # Child class must implement abstract class method
    def mileage(self):
        print("Mileage is 10 liters per 100km")

# this is another car type (actually class)
class SmallCar(Car):
    # Child class must implement abstract class method
    def mileage(self):
        print("Mileage is 5 liters per 100km")

mycar = MyCar()
smallcar = SmallCar()

# Here we call
# abstract method implemented in child class
mycar.mileage()
smallcar.mileage()

# here we call
# ordinary method implemented in mother class
mycar.drives()
smallcar.drives()

# Using Classname(ABC) allows creation
# of both abstract classes and interfaces.

# 1) abstract class typically has:
# --methods with implementation
# --methods without implementation that must be implemented
# in inheriting class.

# 2) interface typically has:
# --methods without implementation that must be implemented
# in inheriting class.

# What is this interface? (rajapintaluokka)
# C++ call it "pure abstract class"

# They are used to create definitions for interaction
# They are agreed and enforced methods used to employ
# activities.
# for instance, I/O activities and DB opening use agreed methods.
# These agreed method signatures are shown in interfaces

# The logic is that coder adds interactions wanted to code
# on case by case basis.
# Thus you can have interface for DB interaction and I/O interaction.

# Class A ja Class B need to interact.
# Thus A inherits suitable interface needed 
# for Class B to interact with A.

class MyInterface(abc.ABC):
    # function kuvaus
    @abc.abstractmethod
    def functioA(self,arg1,arg2) -> int:
        pass

    # function kuvaus
    @abc.abstractmethod
    def functioB(self):
        pass


