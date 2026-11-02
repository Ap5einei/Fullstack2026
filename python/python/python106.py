#from abc import ABC, abstractmethod
import abc
 
#  
# Classes continue...
#
# inheritance
# 
# Inheritance is used for two basic cases
# 1) child class is a special case of mother class
# Over 90 % of the cases are these.
# 2) child class is aggregate of multiple mothers
# fairly rare.

# practical cases
# 1) child class is a special case of mother class
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

# rakenna tästä singleton esimerkki 
# ja immutable class 

# data abstraction
# principle is to make separation between:
# "what it does" and "how it does"
# abstraction hides internal variables

# hiding data
# use __<variablename> to create attribute that
# can only be used within class
# This is similar to "private" in other languages like C++

# here employee count increases by one
# whenever we add a new employee
class Employee:
    # this is a hidden value
    __count = 0
    
    def __init__(self):
        Employee.__count += 1

    def showemployeeinfo(self):
        print("Headcount: ", Employee.__count)

aku = Employee()
hannu = Employee()
hannu.showemployeeinfo() # Headcount: 2
# print(hannu.__count) # causes error
#print(Employee.__count) # causes error

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

# abstraction can also be done with classes
# "abstract class" ja "interface"

# requires use of abc module (see first lines)
# use syntax class <classname>(abc.ABC):

# This is known as "abstract class" in computer science.
# Class that cannot be instantiated.
# However, it forms a common template
# used by multiple roughly similar classes.
# abstract class can have normal methods
# abstract class can have abstract methods
 
# Car is abstract class that forms a common template
# to all different car types
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
# --methods without implementation

# What is interface? (rajapintaluokka)
# C++ call it "pure abstract class"
# They are used to create definitions for interaction
# They are agreed and enforced methods used to employ
# activities
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

#
# polymorphism
#
# polymophism means same functionality with different classes
# typically this means inheriting a method call from mother to child
# example below show how this works with bank account and credit account

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

# this is a special case of bank account
# here we have extra attributes in child class
# thus we need constructor in child class
# see:
# https://www.geeksforgeeks.org/calling-a-super-class-constructor-in-python/
class CreditAccount(BankAccount):
    def __init__(self, name, saldo, id, credit):
        super().__init__(name, saldo, id)
        self.credit = credit

    def accountinfo(self):
        print(self.name, self.saldo, self.id, self.credit)

    def setcredit(self, amount, choice):
        if choice == "r":
            self.credit += amount
        elif choice == "l":
            self.credit -= amount

accountlist = []

account_1 = BankAccount("Aku", 313.00, 123456)
accountlist.append(account_1)

account_2 = CreditAccount("Iines", 111.44, 111111, 12000.00)
accountlist.append(account_2)

for elementti in accountlist:
    elementti.accountinfo()

"""
# Task OOP-06:
# Change your bank so it includes code set above (polymorphism)
# It must have CreditAccount class
# Add code that shows all bank accounts and credit accounts

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
"""

# Task OOP-07:
# Change your bank so it includes code set above
# add at least following functionality to bank:
#   Raise or Lower Credit amount for a customer
#   Destroy account
#   Transfer money from one account to another
#   Change Bank account to credit account
#   Change credit account to bank account
#   add information field to account (text content)
#   Allow writing or removing text to information field
#   for instance, "credit risk"

"""

class BankAccount:
    def __init__(self, name, saldo, id, info_text = ""):
        self.name = name
        self.saldo = saldo
        self.id = id
        self.info_text = info_text
 
    def accountinfo(self):
        print(self.name, self.saldo, self.id, self.info_text)
    
    def changebalance(self, amount, choice):
        if choice == "w":
            self.saldo -= amount
        elif choice == "a":
            self.saldo += amount


class CreditAccount(BankAccount):
    def __init__(self, name, saldo, id, credit, info_text = ""):
        super().__init__(name, saldo, id, info_text)
        self.credit = credit
    
    def setcredit(self, amount, choice):
        if choice == "r":
            self.credit += amount
        elif choice == "l":
            self.credit -= amount

    def accountinfo(self):
        print(self.name, self.saldo, self.id, self.credit, self.info_text)

account_1 = BankAccount("Aku", 313.00, 123456)
accountlist = []
accountlist.append(account_1)

account_2 = CreditAccount("Iines", 111.44, 1111111, 12000.00)
accountlist.append(account_2)
for element in accountlist:
    element.accountinfo()

def addaccount():
    temp_name = input("Give accounts name: ")
    temp_saldo = float(input("Give accounts saldo: "))
    temp_id = int(input("Give accounts id: "))
    temp_account = BankAccount(temp_name, temp_saldo, temp_id)
    accountlist.append(temp_account)

def delaccount():
    name_search = input("Give accounts name to delete:\n")
    for element in accountlist:
        if element.name == name_search:
            accountlist.remove(element)
            break

def changeaccount():
    name_search = input("Give accounts name that is to be changed:\n")

    for element in accountlist:
        if element.name == name_search:
            if hasattr(element, "credit"):
                temp_account = BankAccount(element.name, element.saldo, element.id)
            else:
                temp_account = CreditAccount(element.name, element.saldo, element.id, 0.00)
            accountlist.remove(element)
            accountlist.append(temp_account)
            print(temp_account)
            break

def showoneaccount():
    name_search = input("Give the name of the account you want to find:\n")
    for elementti in accountlist:
        if elementti.name == name_search:
            elementti.accountinfo()
            break

def addinfotext():
    choice = input("Add info (a). Delete info (d):\n")
    name_search = input("Give accounts name to add information into:\n")
    for element in accountlist:
        if element.name == name_search and choice == "a":
            info_text = str(input("Give information for the account:\n"))
            element.info_text = info_text
            print(element.info_text)
            break
        elif element.name == name_search and choice == "d":
            element.info_text = ""
            print(element.info_text)
            break

def cashactions():
    name_search = input("Give the name of the account you want to find:\n")
    for elementti in accountlist:
        if elementti.name == name_search:
            elementti.accountinfo()
            temp_action = input("Give action w or a\n") 
            temp_change = float(input("Give change of saldo\n"))
            elementti.changebalance(temp_change,temp_action)
            break 

def creditactions():
    name_search = input("Give the name of the account you want to find:\n")
    for element in accountlist:
        if element.name == name_search:
            element.accountinfo()
            temp_action = input("Raise (r) or lower (l) the credit:\n")
            temp_change = float(input("Give the amount to raise/lower:\n"))
            element.setcredit(temp_change, temp_action) 
            break

def transfer():
    sender = input("Who is sending money:\n")
    recipient = input("Who is receiving the money:\n")
    amount = 0
    for element in accountlist:
        if element.name == sender:
            element.accountinfo()
            amount = float(input("Give the amount to send:\n"))
            element.changebalance(amount, "w")
            break
    for element in accountlist:
        if element.name == recipient:
            element.changebalance(amount, "a")
            break

def showallaccounts():
    for elementti in accountlist:
        elementti.accountinfo()


while True:
    customer_input = int(input("\n1: Add account\n2: Delete account\n3: Change account\n4: Show account info for one account\n5: Show account info for all accounts\n6: Add information unto an account\n7: Cash actions to account\n8: Credit actions to account\n9: Transfer money\n0: Quit banking program\n"))

    if customer_input == 1:
        addaccount()
    elif customer_input == 2:
        delaccount()
    elif customer_input == 3:
        changeaccount()
    elif customer_input == 4:
        showoneaccount()
    elif customer_input == 5:
        showallaccounts()
    elif customer_input == 6:
        addinfotext()
    elif customer_input == 7:
        cashactions()
    elif customer_input == 8:
        creditactions()
    elif customer_input == 9:
        transfer()
    elif customer_input == 0:
        break 
"""
