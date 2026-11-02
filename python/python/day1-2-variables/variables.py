
#
# Variables
#
# whole reason to use variables is to stores value
# variable stores value dfor duration of program
# it is not permanent storage

# Python has automagically working "garbage collection"
# python considers how long variable exists
# it frees memory when we go outside "visibility area"

# when variable is created it will be issued id.
# This id is a value identifier, it is not memory location
aaa = 123
print(aaa)
print(id(aaa)) # prints out unique id of 123
aaa = 555
print(aaa)
print(id(aaa)) # prints out unique id of 555
bbb = 555
print(bbb)
print(id(bbb)) # prints out unique id of 555

#
# variable naming
#

# Note! You can actually create variables with
# reserved names. This is very bad idea!!!!
# int = 444

# You can set multiple variables with same value
aaa = bbb = ccc = 0

# you can set multiple values to multiple variables
# in same line
aaa, bbb, ccc = 123, 456, 789

#
# global and local variables
#

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
    print("local variable qqq within myfunc() is ",qqq)

    # here we create a local variable (aaa) with same
    # name as global variable (aaa)
    aaa = 11111
    # it is local variable rather than global variable
    # i.e. local variable "overrides" global variable of
    # same name within function.
    print("local variable aaa within myfunc() is ",aaa)

    # local variable will be destroyed at the endvof function
    # thus 11111 will not be value of global variable aaa

    # There are huge number of use cases where we want to use
    # global variables within function.
    # usually it is case of using common values used by all functions.
    # use keyword global <variablename>
    # this tells python that you are using global variable
    # thus it will not create a local variable of same name

    # this does not create local variable, uses global variable
    global bbb 
    print("global variable bbb within function has value ",bbb)
    bbb = 4444 # this change occurs in global setting too

myfunc()
print("global variable aaa has value ",aaa)
print("global variable bbb has value ",bbb)
# Local variable cannot be used in global context
#print("value of local variable qqq in global context is ", qqq)  

# You can destroy variable using keyword del
del bbb
# causes error as bbb has been destroyed
# print("global variable bbb has value ",bbb)

#
# variable data types are not fixed
#

aaa = "1"
print(aaa)
print(type(aaa))
aaa = 1
print(aaa)
print(type(aaa))

# In theory every variable is generic and can be used
# in any data type and context dynamically
# PLEASE DO NOT CODE LIKE THAT!

#
# data types
#

# Python uses following data types:
#   numbers: integer, complex numer, float
#   sequence types: string, list, tuple, dictionary
#   boolean
#   set

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

# set (joukko)
# set is an unordered list, thus no index
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

