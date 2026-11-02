#
# Functions
#

# Funktiota voidaan kutsua uudestaan ja uudestaan.
# Funktion tarkoitus on tehdä uudelleenkäytettävää koodia.
# Funktiossa voidaan kutsua muita funktioita.

# Mikä on funktion oikea koko?
# Funktion oikea koko on yksi ohjelmalohko.
# Ohjelmalohko on yksi asia, jonka ohjelma toteuttaa.

# Hyvä funktio on sellainen joka tekee vain yhden tietyn 
# asian kerrallaan ja on tarpeeksi iso tehdäkseen sen, 
# ei pienempi eikä suurempi. 

# def functionname (<parameters>):
#   <code statements>
# 
# käytä funktion argumenttia aina, kun voit.
# Käytä global keywordia, vain jos haluat muuttaa 
# globaalin muuttujan arvoa.
# Muuten käytä globaaleja muuttujia argumenttejen kautta.

# you can use argumentname: <datatype>
# tietotyyppi on hurskas toivomus, se ei pakota toimimaan.
#def calculatesquare(arg):
def calculatesquare(arg: int) -> int:
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
result = calculatesquare(4.44)
print(result) # 19.7136

# Coder is responsible for both arguments 
# and return value types.
# use asserts and force return type with casting.
def calculatesquare(arg: int) -> int | None:
    if type(arg) is int:
        return int(arg**2)
    else: 
        return None

print(calculatesquare(4)) # 16
print(calculatesquare(4.5)) # None
print(calculatesquare("kukka")) # None

# you may also notice that rewriting function
# is entirely legal and possible.
# PLEASE DO NOT CODE LIKE THAT!

# argument may be a default argument

# thus arguments are compulsory
# unless you define it a default argument
# here arg2 is default argument
def calculatesumtwo(arg1 : int, arg2 : int = 10):
# def calculatesumtwo(arg1, arg2 = 10):
    return arg1*arg2

print(calculatesumtwo(5,20))  # 100
print(calculatesumtwo(5))  # 50
# You must give arguments that are NOT default arguments
# print(calculatesumtwo())  # Error
# You cannot give too many arguments
# print(calculatesumtwo(5,20, 10))  # Error

# Order of arguments is immutable

# It can only be changed using keyworded arguments
# you can set keyword arguments, aka
# freely set values to different arguments
# here values are set to arg1 and arg2
print(calculatesumtwo(5, 10))  # 50
print(calculatesumtwo(arg2 = 10, arg1 = 5))  # 50

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

result = specialfunc("aa","bb","cc","dd","ee")
print(result)

result = specialfunc()
print(result)

mysetA = { "tupu", "hupu", "lupu" }
result = specialfunc(mysetA, None,"Kielo")
print(result)

def keywordspecialfunc(**kwargs_list):
    finallist = []
    for key, value in kwargs_list.items():
        finallist.append([key,value])
    return finallist

mytupleB = (4,7,32,5,121,5,56)
result = keywordspecialfunc(Target = "Kielo", End = None, Payload = mytupleB)
print(result)
print(result[0][1]) # Kielo
print(result[2][1]) # mytubleB


