#
# tuple
#
# tuple is essentially immutable list
# specific order, can use index
# tuple syntax is () 

mytupleA = ()
print("my empty tuple is ",mytupleA)

mytupleB = (4,7,32,5,121,5,56)
                              
print(mytupleB.count(5)) # 2
# first occurrence index
print(mytupleB.index(5)) # 3
print(mytupleB.index(5,4)) # 5
  
mytupleC = (4, "Hello", 9.123)
print("my tuple is ",mytupleC)

# tuple is immutable
# mytupleC[0] = 111 # causes error

# tuple creation problems - ei nykyisillä versioilla
mytupleD = ("one") # creates a string!
print(mytupleD)
print(type(mytupleD))
mytupleD = ("one",) # creates a tuple
print(mytupleD)
print(type(mytupleD))

print(mytupleC[1]) # Hello
print(mytupleC[-1]) # 9.123

# destroy tuple with del
#del mytupleC[-1] # error 
del mytupleC
#print(mytupleC) # error!

# tuple can be iterated
for element in mytupleB:
    print(element, end=" ")
print("")

# immutable tuple cannot be changed
# you can change mutable objects within tuple
mytupleE = ([1,2,3], 33, 44)
print(mytupleE)
mytupleE[0][2] = 66666
print(mytupleE)

# concatenation works
mytupleF = mytupleE + (111,222,333)
print(mytupleF)

#
# Set eli suomeksi joukko
#
# unordered list so it has no index
# every element must be unique

mysetA = { "tupu", "hupu", "lupu" }
mysetA.add("tupu")
mysetA.add("hessu")
# did not add tupu as it already was there
# adds hessu as it was not there
# when printing the order changes randomly
print(mysetA)

# individual elements are immutable
# except: list, set, dictionary...

# you can remove elements
mysetA.remove("hessu")
print(mysetA)
# you can add multiple element with update()
# update must hold iterable (list, set)
mysetA.update(["aku", "ankka"])
print(mysetA)
set.update(mysetA,["hannu", "hanhi"])
print(mysetA)

# Varoitus! string käsitellään iterable tyyppisesti
# eli alla oleva käsky jakaa stringin charactereiksi
mysetA.update("qwerty")
# correct way of adding single element via update
mysetA.update(["qwerty"])
# mysetA.update("ankka")
print(mysetA)

# you can remove values with discard() and remove()
# discard() does not raise alarm
# remove() raises alarm, error stops program
# # mysetA.discard("Kukka")
# mysetA.remove("Kukka")

# main use of sets is set theory (joukko-oppi)
# union, intersection, difference 

mysetAAA = {11,22,33,44,55,66}
mysetBBB = {44,55,66,77,88,99}

# union shows what exist in both
# no duplicates are shown
# 11,22,33,44,55,66,77,88,99
print(mysetAAA|mysetBBB)
print(mysetAAA.union(mysetBBB))

# intersection shows what is same in both
# 44,55,66
print(mysetAAA&mysetBBB)
print(mysetAAA.intersection(mysetBBB))

# difference shows A without elements common with B
# 11,22,33
print(mysetAAA-mysetBBB)
print(mysetAAA.difference(mysetBBB))

# symmetric difference shows A and B values which
# are not common to both
# 11,22,33,77,88,99
print(mysetAAA^mysetBBB)
print(mysetAAA.symmetric_difference(mysetBBB))

# frozenset() immutable set
# effectively a constant variable
# has no add() method
mysetCCC = frozenset([11,22,33])


#
# Dictionary
#
"""
mydictAAA = {
    "Name" : "Aku",
    "Age": 616 
}
"""

mydictAAA = dict({"Name" : "Aku", "Age": 616})

print(type(mydictAAA))
print(mydictAAA)

# dictionary can be empty
mydictBBB = {}
print(mydictBBB)

mydictCCC = {1: "Aku", 2: "Iines", 4:"Kukka", 3: "Hevonen"}
print(mydictCCC) # näyttää luomisjärjestyksessä

# dictionaryjen arvot löytyvät avaimilla
# print(mydictCCC[0]) # avain 0 ei ole olemassa
print(mydictCCC[1])
print(mydictCCC[2])
print(mydictCCC[3]) # "Hevonen"

# you can change values
# initial value {"Name" : "Aku", "Age": 616}
mydictAAA["Name"] = "Hannu" 
print(mydictAAA) # {"Name" : "Hannu", "Age": 616}

# you can add new key-value pairs
mydictBBB[0] = "Eka"
mydictBBB[1] = "Toka"
mydictBBB[666] = "Outoa"
print(mydictBBB)

# you can delete individual keys-value pairs
# or whole dictionary
del mydictBBB[666]
del mydictBBB

# typical use case is to have multiple objects
# as key to object pairs
# then destroy them as needed
mydictDDD = {}
mydictDDD[112] = "aaa"
mydictDDD[122] = "ggg"
mydictDDD[212] = "ccc"

# destroy object as you store it to result for
# some use
result = mydictDDD.pop(212)
print(result) # ccc

# Note! you can do same thing with lists
# lets make FIFO and LIFO 
listAAA = [11,22,33,44,55,66]

# FIFO aka queue aka jono
# add to end of list 
listAAA.append(777)
# remove from beginning of list
result = listAAA.pop(0)
print(result) # 11
print(listAAA)

# LIFO aka stack aka pino
# add to end of list 
listAAA.append(888)
# remove from end of list
result = listAAA.pop()
print(result) # 888
print(listAAA)

#
# Functions
#
# def functionname (<parameters>):
#   <code statements>
# 
# käytä funktion argumenttia aina, 
# paitsi jos haluat muuttaa globaalin muuttujan arvoa funktiossa

# you can use argumentname: <datatype>
def calculatesquare(arg: int):
# def calculatesquare(arg):
    return arg**2

print(calculatesquare(4)) # 16

result = calculatesquare(4)
print(result) # 16

# python does not enforce data type of argument!
# you must write your own datatype enforcement functions

# you can give wrong data type arguments...
# argument definition is expectation of datatype
# Python allows inserting anything
# thus code may or may not work
# Kääntäjä sallii seuraavan vaikka se kaataa
# ohjelman suorituksen aikana
# result = calculatesquare("kukka")
# "punainen ohjelman kaatava virhe"
# result = calculatesquare(4.44)
# print(result) # 19.7136

# argument may be a default argument
#
# thus arguments are compulsory
# unless you define it a default argument
# here arg2 is default argument
def calculatesumtwo(arg1 : int, arg2 : int = 10):
# def calculatesumtwo(arg1, arg2 = 10):
    return arg1*arg2

print(calculatesumtwo(5,20))  # 100
print(calculatesumtwo(5))  # 50
# print(calculatesumtwo())  # Error
# print(calculatesumtwo(5,20, 10))  # Error

# order of arguments is immutable
# It can only be changed using keyworded arguments
# you can set keyword arguments, aka
# freely set values to different arguments
# here values are set to arg1 and arg2
print(calculatesumtwo(arg2 = 5, arg1 = 5))  # 50

# Python allows sending as many arguments as needed
# this requires setting *args or **kwargs
# *args are non keyword arguments
# **kwargs are keyword arguments
# you create a list of arguments and use them:

def specialfunc(*arg_list):
    finallist = []
    for arg in arg_list:
        finallist.append(arg)
    return finallist

result = specialfunc("aa","bb","cc")
print(result)

result = specialfunc(mysetA, None,"Kielo")
print(result)

def keywordspecialfunc(**kwargs_list):
    finallist = []
    for key, value in kwargs_list.items():
        finallist.append([key,value])
    return finallist

result = keywordspecialfunc(Target = "Kielo", End = None, Payload = mytupleB)
print(result)
print(result[0][1]) # Kielo

print

# python function can be anonymous
# we typically use lambda (arrow) functions
# lambda <argument1> : <code expression>
# https://realpython.com/python-lambda/
# https://www.tutorialsteacher.com/python/python-lambda-function


kukka = lambda aaa, bbb : aaa+bbb
kukka2 = lambda aaa, bbb : calculatesumtwo(aaa,bbb)

print(kukka(123,456)) # 579
print(kukka2(5,5)) # 25

# vaihteleva määrä argumentteja
kukka3 = lambda *arg : specialfunc(arg)
print(kukka3(1, 2, 3, "a", None, "b", "c")) # [(1, 2, 3, 'a', None, 'b', 'c')]

# ei argumentteja
kukka4 = lambda : print("parametriton lambda!")
kukka4()

kukka5 = lambda : "myös parametriton lambda!"
print(kukka5())

# tämä on anonyymi lambda funktio
(lambda arg1,arg2 : print(arg1 + arg2))(111,222) # 333

# calback funktio toteutus A
def myfuncAResult(nimi):
    print("myfuncAResult tuli arvolla " + nimi)
    
def teejotain(nimi, callbackfunktio):
    print(nimi)
    tulos = "Kalle"
    callbackfunktio(tulos)

teejotain("Jukka",myfuncAResult)

# callback ja anomnyymifunktio
def myfuncAResult(nimi):
    print("myfuncAResult tuli arvolla " + nimi)
    return 1234
    
def teejotain(nimi, callbackfunktio):
    print(nimi)
    tulos = "Kalle"
    return callbackfunktio(tulos)

aaa = lambda arg, func : teejotain(arg,func)

print(aaa("Jukka",myfuncAResult))

# lambdaa käytetään paljon callback funktioissa
def mycallbackfunc1(arg: int):
    print("mycallbackfunc1: ", arg)

def mycallbackfunc2(arg: int):
    print("mycallbackfunc2: ", arg)

def mycallbackfuncfail(arg: int):
    print("mycallbackfuncfail: ", arg)

def funktioA(arg:int, callable):
    print("funktioA: ", arg)
    result = 2222
    if arg < 2000:
        callable(result)
    else:
        mycallbackfuncfail(result)

funktioA(1234, mycallbackfunc1)
funktioA(1234, mycallbackfunc2)
funktioA(5678, mycallbackfunc2)

# another example of use of lambda functions
mylambda = lambda arg : print(f"mycallbackfunction got value: {arg}")

def mycallbackfunction(arg):
    print(f"mycallbackfunction got value: {arg}")

def teejotainjollaoncallbackfunktio(arg1,arg2,callback):
    #funktio tekee jotain
    dummy = arg1+arg2
    if dummy > 0:
        callback(dummy)
    else:
        print("action failed")

teejotainjollaoncallbackfunktio(-1,0,mycallbackfunction)
teejotainjollaoncallbackfunktio(11,22,mycallbackfunction)
teejotainjollaoncallbackfunktio(11,22, mylambda )
teejotainjollaoncallbackfunktio(11,22, lambda arg : print(f"mycallbackfunction got value: {arg}") )

# functions within functions
# this is called encapsulation
# https://realpython.com/inner-functions-what-are-they-good-for/

globalvariable = "!"

def outerfunc():
    global globalvariable
    outervariable = "Hello"

    def innerfunc():
        nonlocal outervariable
        innervariable = "World"
        print(outervariable, innervariable, globalvariable)
        return "testi"
    
    return innerfunc()

print(outerfunc())

# Python have few built-in functions()
# abs() absolute number
# all() returns true if all elements in iterable are valid
# bin() show decimal as binary
# callable() if object can be called

print(abs(-123.45)) # 123.45

mylistQ = [1,2, None]
mylistZ = [1,2, 3]
print(all(mylistQ)) # False
print(all(mylistZ)) # True

print(bin(5)) # 0b0101 --> 0b101

print(callable(5)) # False
print(callable(mylistZ)) # False
print(callable(outerfunc)) # True

