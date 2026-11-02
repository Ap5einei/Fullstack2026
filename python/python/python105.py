import math

#
# object oriented programming
#

# class and object make it possible to have properties and functionality


# You can use objects with classes



# CASE 1: an object with class that has only properties
class Kokeilu:
    # you can create an object with class
    # that has only properties
    someproperty = ""

myObject = Kokeilu()
myObject.someproperty = "Aku Ankka"

# however, can you create additional properties dynamically?
# nowadays this is possible, not in old Python versions
myObject.somepropertytoo = "Aku Ankka too"
print(myObject.someproperty)
print(myObject.somepropertytoo) # did not always work

# You can actually give function as property
# this allows functionality 
myObject.funktio = lambda aa,bb : aa + " " + bb
print(myObject.funktio("Hello","World!"))
print(myObject.funktio("Minni","Hiiri"))
del myObject

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

# You can even five functions as properties to dictionaries
myObj = {
    "Hello": lambda aa,bb : aa + " " + bb
}
print(myObj["Hello"]("Hello","World!"))
"""





"""
# CASE 2: an object with class that has properties and methods
# Periaatteessa property voidaan määrittää class tasoisena eikä
# sitä tarvitse asettaa konstruktorissa?
# Tässä tapauksessa konstruktorin määritys korvaa muuttujan arvon
# luokka ei periaatteessa tarvitse konstruktoria ollenkaan.

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

# konstruktorin käytön perusajatus on asettaa arvoja
# oliota luodessa.
# periaatteessa konstruktorin voi jättää kokonaan pois, 
# jos luokka sisältää aina samat alkuarvot

# class, object, method
# inheritance, polymorphism
# data abstraction, encapsulation

# Actually python uses classes extensively as
# python uses objects and every object has
# attributes and methods...

# lets make a class

# keyword class is used to make classes
# class is a model we use to create objects
# it has attributes -- what is the value?
# it has methods -- what it does?
# this allows us to define abstract things

# For instance, lets make a car
# what attributes car has?
# color
# enginepower
# model
# year
# what methods car has?
# onoff() - boolean
# movement(speed)
# turnleft()
# turnright()

# classes are created using keywords 
# class <classname>

class Car:
    # class constructor is function that is called
    # when object of class is created
    # we typically define attributes inside it
    # syntax is always: def __init__(self, <attributes>):
    def __init__(self, model, year, color):
        # attributes
        # color
        self.color = color
        # enginepower
        self.enginepower = 100
        # model
        self.model = model
        # year
        self.year = year

    # methods
    # methods are essentially functions within class
    # syntax is def <methodname>(self,<arguments>):

    # onoff(status) - boolean
    def onoff(self,status):
        # boolean value if engine is on or off
        if status == True:
            print(f"\nEngine of {self.enginepower} horsepower is on!")
        else:
            print("\nEngine is off!")

    # movement(speed)
    def movement(self,speed):
        if speed==0:
            print("\nCar has stopped!")
        else:
            print("\nCar is moving {} km/h!".format(speed))

    # turnleft()
    def turnleft(self):
        print("\nCar is turning left...")

    # turnright()
    def turnright(self):
        print("\nCar is turning right...")

# here we create an object based on class Car
mycar1 = Car("Audi", 2020, "White")
print(mycar1) # prints out address of mycar1
# class' objects use . notation
mycar1.enginepower = 120
print(mycar1.enginepower)

mycar1.onoff(True)
mycar1.movement(100)
mycar1.turnright()
mycar1.onoff(False)

#
# class variables and instance variables in classes
#

# instance variables (oliotasoinen).
# They are object level and object based variables.
# thus every car has their own color.

# class variable is used on class level (luokkatasoinen).
# they work independently of any class methods
# they are used by writing following:
# <classname>.<variablename>
# They are written directly under class

# Thus we almost always use __init__ to set object level variables 
# and use class to set class level variables.

# there are two basic use cases:
# first, variable is same to all class objects 
# thus idea is to use it like a constant
# However, there is no constant in Python! BEWARE!
# This allows creation of key-value pairs similar to enumerated lists
# or dictionaries

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

"""
# importing pi from math library allows changing its value
# This is because Python does not have constants
import math
#math.pi = 3
print(math.pi) # 3
"""

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
# Tämä voisi olla esimerkiksi auton merkki, joka ei muutu auton olemassaolon aikana.

# 4) Luokkatason muuttuja on hyvä toimimaan sisäisenä laskurina.
# So toimii kuin funktioissa oleva yield

#
# constructors
#
# parametrized constructor
# non-parametrized constructor 

class MyExampleB:
    # this is constructor
    def __init__(self):
        print("\nMyExampleB created")

    def saysomething(self,arg):
        print("Hello", arg)        

# ex3 here does not have any attributes
ex3 = MyExampleB()
ex3.saysomething("Aku")
ex3.saysomething("Ankka")

# this is non-parametrized constructor with
# attributes. can we do it?

class MyExampleC:
    # this is constructor
    def __init__(self):
        print("\nMyExampleC created")
        self.name = ""

    def saysomething(self,arg):
        print("Hello", arg)
        self.name = arg        

# ex4 here does have attributes
ex4 = MyExampleC()
ex4.saysomething("Aku") # Hello Aku
ex4.saysomething("Ankka") # Hello Ankka
print(ex4.name) # Ankka

# Thus we can draw conclusion __init__
# can have internal aka local variables 
# not given as arguments

# as a matter of fact Python has Default Constructor
# It creates object of class

class MyExampleD:
    # attributes
    name = "Iines"

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
# class level attributes 
# into object level attributes

# Note! ALWAYS USE CONSTRUCTOR!
# It makes obvious what level attributes are!

# Note! MULTIPLE CONSTRUCTORS ARE NOT SUPPORTED!
# https://realpython.com/python-multiple-constructors/


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
print(getattr(ex7,"arg2")) # 456

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

# this prints out class name
print(ex7.__class__.__name__) # MyExampleE

# this prints out class module
print(ex7.__module__) # __main__
print(math.acos.__module__) # math


# Task OOP-01
# Program your own class and objects
# Person class with name, age
# personstats()
# personsays(arg)
# Create 2 persons


"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def personstats(self):
        print(self.name)
        print(self.age)

    def personsays(self,say):
        print(say)

person1 = Person("Aku",55)
person2= Person("Hannu", 66)

person1.personstats()
person1.personsays("Terve")

person2.personstats()
person2.personsays("Moro") 
"""

# Task OOP-02
# change previous solution as follows:
# add class variable number
# its value is increased by 1 whenever new
# person is added
# print how many persons you have created
# i.e. how many Person objects you have
"""
class Person:
    number = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.number +=1

    def personstats(self):
        print(self.name)
        print(self.age)

    def personsays(self,say):
        print(say)

print(Person.number)
person1 = Person("Aku",55)
print(Person.number)
person2= Person("Hannu", 66)
print(Person.number,"näin monta henkilöä tehty")

person1.personstats()
person1.personsays("Terve")

person2.personstats()
person2.personsays("Moro") 
"""

# Task OOP-03
# create class PersonToo
# without default constructor
# attributes are name and age
# methods are personstats() and personsays(arg)
# Does it work properly?

class PersonToo:
    name=""
    age=1

    def personstats(self):
        print(self.name)
        print(self.age)

    def personsays(self,say):
        print(say)

person1 = PersonToo()
person1.name="Tupu"
person1.age=11
person2= PersonToo()
person2.name="Hupu"
person2.age=11


person1.personstats()
person1.personsays("Terve")

person2.personstats()
person2.personsays("Moro")
print(person1.name)
print(person2.name)
print(PersonToo.name)
print(PersonToo.age)

# Task OOP-04
# Use class functions and find out following...
# 1) Value of age in both persons.
# 2) Is qwerty a object variable?
# 3) Delete age of one of the persons.

# 1) Value of age in both persons.
print(getattr(person1,"age"))
print(getattr(person2,"age"))

# 2) Is qwerty a object variable?
print(hasattr(person1,"qwery"))

# 3) Delete age of one of the persons.
delattr(person2,"age")
print(hasattr(person2,"age")) 


# Task OOP-005
# afternoon's programming task.
# create a class BankAccount for accounts
# with attributes: 
#   name (string), 
#   saldo (float), 
#   id (int)
# with methods: 
#   changebalance(float) for X amount withdrawal/accumulation
#   accountinfo() that describes account info
# Then add all account objects to a list named accountlist.

# Next create a following bank interface to test out your class and list:
#
# MY BANK
# 1: Add account
# 2: Show account info for one account
# 3: Show account info for all accounts
# 0: Quit banking program

class BankAccount:
    def __init__(self, name, saldo, id):
        self.name = name
        self.saldo = saldo
        self.id = id
 
    def accountinfo(self):
        print(self.name, self.saldo, self.id)

    def changebalance(self, amount, choice):
        if choice == "w":
            self.saldo -= amount
        elif choice == "a":
            self.saldo += amount

account_1 = BankAccount("Aku", 313.00, 123456)
accountlist = []
accountlist.append(account_1)
for elementti in accountlist:
    elementti.accountinfo()

def addaccount():
    temp_name = input("Give accounts name: ")
    temp_saldo = float(input("Give accounts saldo: "))
    temp_id = int(input("Give accounts id: "))
    temp_account = BankAccount(temp_name, temp_saldo, temp_id)
    accountlist.append(temp_account)

def showoneaccount():
    name_search = input("Give the name of the account you want to find:\n")
    for elementti in accountlist:
        if elementti.name == name_search:
            elementti.accountinfo()

def cashactions():
    name_search = input("Give the name of the account you want to find:\n")
    for elementti in accountlist:
        if elementti.name == name_search:
            elementti.accountinfo()
            temp_action = input("Give action w or a\n") 
            temp_change = float(input("Give change of saldo\n"))
            elementti.changebalance(temp_change,temp_action) 

def showallaccounts():
    for elementti in accountlist:
        elementti.accountinfo()

while True:
    customer_input = int(input("\n1: Add account\n2: Show account info for one account\n3: Show account info for all accounts\n4: Cash actions to account\n0: Quit banking program\n"))

    if customer_input == 1:
        addaccount()
    elif customer_input == 2:
        showoneaccount()
    elif customer_input == 3:
        showallaccounts()
    elif customer_input == 4:
        cashactions()
    elif customer_input == 0:
        break
