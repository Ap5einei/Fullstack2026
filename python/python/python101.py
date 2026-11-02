import keyword

# luo yksi rivisen kommentin

"""
Tämä taas on monirivinen
kommentti.
"""

#
# print
#

# You can simply write text using print
print("tekstiä")

# print can be used with variables
variableA = 123
variableB = variableA + 456
print("variableA = ", variableA)
print("variableA = ", variableA, "variableB = ", variableB)


# print have sep and end arguments
# sep is what is printed between previous statements
# end is what is printed at end of everything
#print("Jukolassa on ", 7, "veljestä", sep="\n", end=".\n")
print("Jukolassa on", 7, "veljestä", sep=" ", end=".\n")

# print uses special characters
print("My name is O'Malley")
print("This is \"fun\" training!")
print("This is 'fun' training!")

# print uses r to denote raw string
# this causes warning!
print('C:\some\name')  # \name is shown as \n 
print('C:\\some\\name')  # shows correctly
print(r'C:\some\name')  # r before the quote shows info correctly

# ääkköset
tämämuuttuja = 1234
print(tämämuuttuja)

# string literals
# allows writing multiline raw text
print(
"""
    this is
7
    brothers.
"""
)


# You can combine strings with + and even without any sign
print("This is " + "7 brothers!")
print("This is " "7 brothers!")

#
# input
#

# input returns a string
# here it is changed to integer

#variableA = int(input("Give me a number "))
#print(variableA)


#
# list
#

# lists are arrays of data
# Each element is actually list class object!
# list uses [] syntax
mylistA = [11,22,33,44,55,66]

# list content can be anything
mylistB = [11,"Aku",33,"Ankka",55,66]

print(mylistA)
print(mylistB)
# <class 'list'>
print(type(mylistA))
print(type(mylistB))

# you can change values of list!
mylistB[0] = "Kukka" 
print(mylistB)



#
# tuples
#

# tuple is a immutable list
# tuple uses () syntax
# you cannot change, add or remove elements
mytupleA = ("Tupu", "Hupu", "Lupu")
print(mytupleA)
print(type(mytupleA))

# you cannot change values of tuple!
# mytupleA[0] = "Kukka" # causes error
print(mytupleA)


#
# dictionary
#

# dictionary is a key-value paring
# key must be unique!
# uses {} syntax

studentdict = {
    "Tupu" : 111,
    "Hupu" : 122,
    "Lupu" : 130   
}
print(studentdict)
print(studentdict["Lupu"]) # value to this key is 130

studentdict["Aku"] = 313 # you can add new key-value pair
studentdict["Aku"] = 131 # you can change key-value pair
studentdict.pop("Hupu") # you can remove key-value pairs
print(studentdict)


# This is the end of Python basics

#
# Variables
#
# variable stores value
# python considers how long variable exists
# it frees memory when we go outside "visibility area"

# variable is automatically created and has unique id
# this is not memory location
# this is value identifier, it is not memory location
aaa = 123
print(aaa)
print(id(aaa)) # prints out unique id of aaa
aaa = 555
print(aaa)
print(id(aaa)) # prints out unique id of aaa
bbb = 555
print(bbb)
print(id(bbb)) # prints out unique id of bbb

# Note! You can actually create variables with
# reserved names. This is very bad idea!!!!
# int = 444

# You can set multiple variables with same value
aaa = bbb = ccc = 0

# you can set multiple values to multiple variables
# in same line
aaa, bbb, ccc = 123, 456, 789

# python uses local variables and global variables
# local variables are declared inside a function
# they have scope of that function
# they may have same name as global variables
# but this is stupid coding

# you can use and change values of global variables
# within function if you redeclare variable within
# function using keyword global
aaa = 12345
bbb = 67890

def myfunc():
    # this is a local variable
    # it cannot be used outside function
    qqq = 999
    print(qqq)

    # here we create a local variable with same
    # name as global variable (aaa)
    aaa = 11111
    print(aaa)

    # local variable will be destroyed at the end
    # of function
    # thus 11111 will not be value of global variable aaa

    # when you need to change value of global variable inside function...
    # use keyword global <variablename>
    # this tells python that you are using global variable
    # thus it will not create a local variable of same name
    global bbb
    print(bbb) # prints out global value
    bbb = 4444 # this change occurs in global setting too

myfunc()
print(aaa)
print(bbb)
# print(qqq)  # locaL variable cannot be used in global context

# You can destroy variable using keyword del
del bbb
#print(bbb) # causes error as bbb has been destroyed

#
# Python data types
#
# numbers: integer, complex numer, float
# sequence types: string, list, tuple, dictionary
# boolean
# set
 
# numbers: integer, complex number, float
aaa = 123 # integer
bbb = 123.456 # float
ccc = 11 + 22j # complex

# sequence types: string, list, tuple
ddd = "Hulabaloo" # string
print(ddd)
#ddd[0] = "G" # string is immutable
print(ddd[0]) # H
print(ddd[0:4]) # Hula
print(ddd*2) # print string twice

# list see above
eee = [11,22,33]
print(eee)
print(eee[0]) # 11
print(eee[0:2]) # 11,22
print(eee*2)

# tuple works like list but it immutable
mytuple = (11,22,33)
print(mytuple)

# dictionary
fff = {1:"Aarne", 2:"Bertta", 3:"Celsius"}
print(fff)
print(fff.keys())
print(fff.values())

# boolean
print(type(True))
print(False)
print(True)

# set
# set is an unordered list
# set does not have an index
# every element must be unique!
ggg = set()
ggg.add(111)
ggg.add("jussi")
ggg.add("jussi")
ggg.add("jussi")
ggg.add("jussi")
print(ggg) # 111, jussi
ggg.remove(111)
print(ggg) # jussi

#
# keywords
#

# keywords (aka reserved words) change with
# python versions
# you can ask if a word is keyword using
# keyword library (see first line of this code)
# import keyword

# print out all keywords
print ( keyword.kwlist )

# reserved keywords?
print( keyword.iskeyword("False") ) # True
print( keyword.iskeyword("kukkaruukku") ) # False

# None is Python's null value
# null means no value
print(None == None) # True
print(None == 0) # false
print(None == 111) # false
print(None == False) # false

asdf = None
print(asdf)

print("---")

def numcheck( numarg ):
    if numarg % 4 == 0:
        return False

print ( numcheck(4) ) # False
print ( numcheck(5) ) # None

print("---")

#
# and, or, not, in, is
#

hhh = iii = 25

if hhh == 25 and iii == 25:
    print("same")

hhh = 30

if hhh == 30 or iii == 30:
    print("one of them")

hhh = 15

if not hhh == 20:
    print("something else")

if hhh != 20:
    print("something else")

# in is used to see if something is in something
jjj = "kukkakeppi"

if "k" in jjj:
    print("k found out!")

if "ö" in jjj:
    print("ö found out!")

if 11 in [22,44,66,11]:
    print("found out number 11 !")

# is is used to check identification
kkk = True
#kkk = 111 
if type(kkk) is bool:
    print("It is Boolean...")

if type(kkk) == bool:
    print("It is Boolean value...")


print ( 5+6 is 12 ) # False
print ( 5+7 is 12 ) # True

# what is difference between is and == ?
# is will return True if two variables point 
# to the same object (in memory)
# == will return True if the objects referred 
# to by the variables are equal.
# https://mail.python.org/pipermail/python-list/2001-November/094920.html
# https://stackoverflow.com/questions/26595/is-there-any-difference-between-foo-is-none-and-foo-none

# two lists are presented.
# They cannot be identical as they are stored independently in memory
# thus:
if ( [] == [] ):
    print("true 1") # true
if ( [] is [] ):
    print("true 2") # false
if ( {} == {} ):
    print("true 3") # true
if ( {} is {} ):
    print("true 4") # false

# nonlocal is rare keyword used with function in function
# nonlocal works like global if you have defined a function within function
def func1():
    # outer function has variable
    func1variable = 111
    def func2():
        # inner function variable is defined as nonlocal
        # thus it works as global within func1 and func2
        nonlocal func1variable
        func1variable = 222
        print("func2 says ", func1variable)
    func2()
    print("func1 says ", func1variable)

func1()

print("----")

# other keywords include:
# for, while, break, continue
for i in range(0,10,1):
    print(i, end= " ")
    if i == 8:
        break

print("\n")

iter = -1
while iter < 10:
    iter += 1
    if iter == 8 or iter == 7:
        continue
    else:
        print(iter, end= " ")

# exceptions use try, except, raise, finally, assert

# pass is used to create a null function

# pass is used to create a function that does nothing
# it is thus placeholder

def notreadyfunc():
    pass

notreadyfunc()

# pass can be set with class

class notreadyclass:
    pass

# functions can have return to return a value
def myreturnfunc(arg):
    return "\nYou said " + arg

print(myreturnfunc("Hello!!!"))

# keyword del is used to destroy a variable
del mylistB

#
# literal
#
# you can use """ """ to create multiline comments
"""
This is a comment that is not official comment.
It does work like that as this literal is not used
in the code in any way.
Please use this when you define your functions and
classes...
"""


# literals
var1 = 0b01001100 # binary literal
var2 = 1234 # decimal literal
var3 = 0o123 # octal literal
var4 = 0x12ed # hexadecimal literal
print(bin(var1))
print(var2)
print(oct(var3))
print(hex(var4))

# f merkkijonolla tulostus

tulos = 111 * 2
print(f"Tulos: {tulos}")


# afternoon tasks:



print("end")

