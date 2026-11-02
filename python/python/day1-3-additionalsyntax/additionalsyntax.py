
#
# keywords
#

# keywords (aka reserved words) change with
# different python versions
# you can ask if a word is keyword using keyword library
import keyword

# print out all keywords
print ( keyword.kwlist )

# reserved keywords?
print( keyword.iskeyword("False") ) # True
print( keyword.iskeyword("kukkaruukku") ) # False

#
# null values in Python
#

# None is Python's null value
# null means no value
print(None == None) # True
print(None == 0) # false
print(None == 111) # false
print(None == False) # false

# You can give variable value None
# it is often a good choice
asdf = None
print(asdf)

# This function returns either False or None.
# function thus returns None if it has no return value.
def numcheck( numarg ):
    if numarg % 4 == 0:
        return False

def printsomething():
    print("printsomething")

print ( numcheck(4) ) # False
print ( numcheck(5) ) # None
print ( printsomething() ) # None

#
# and, or, not, in, is
#

# and or not are used in comparisons
hhh = iii = 25

if hhh == 25 and iii == 25:
    print("same")

hhh = 30

# comparisons go from left to right
if hhh == 30 or iii == 30:
    print("one of them")

hhh = 15

if not hhh == 20:
    print("something else")

if hhh != 20:
    print("something else")

# in is used to see if something is in something
# use case is sequence types: string, list, tuple
jjj = "kukkakeppi"

if "k" in jjj:
    print("k found out!")

if "ö" in jjj:
    print("ö found out!")

if 11 in [22,44,66,11]:
    print("found out number 11 !")

# is is used to check identification
# it checks out data type (class)
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

# PLEASE USE is TO COMPARE FOR CLASS (data type)
# PLEASE DO NOT USE is TO COMPARE OBJECTS

# PLEASE USE == TO COMPARE VALUE EQUALITY BETWEEN OBJECTS

#
# nonlocal
#

# nonlocal is rare keyword used with function in function
# nonlocal works like global if you have defined 
# a function within function

# This is used when writing your own libraries.
def func1():
    # outer function has variable
    func1variable = 111
    def func2():
        # inner function variable is defined as nonlocal
        # thus it works as global within func1 and func2
        nonlocal func1variable
        print("func2 says ", func1variable) # 111
        func1variable = 222
        print("func2 says ", func1variable) # 222
    print("func1 says ", func1variable) # 111
    func2()
    print("func1 says ", func1variable) # 222

func1()

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

# This allows creation of necessary functions during
# development phase allowing other programmers do their
# own work in participation.

def notreadyfunc():
    pass

notreadyfunc()

# pass can also be set with class

class notreadyclass:
    pass

#
# function can have return value
#

# functions can have return to return a value
def myreturnfunc(arg):
    return "\nYou said " + arg

print(myreturnfunc("Hello!!!"))

#
# del 
#

# keyword del is used to destroy a variable
# it is advisable to destroy variables you no longer use
mylistB = [11,22,33]
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
print(f"Tulos: {tulos} {111*2}")

#
# bitwise operations
#

aaa = 0b01001000
bbb = 0b10001110
# or  0b11001110
# xor 0b11000110
# and 0b00001000

# a and b have or operation with |
print(aaa|bbb) # 206
print(0b11001110)

# a and b have xor operation wth ^
print(aaa^bbb) # 198
print(0b11000110)

# a and b have and operation with &
print(aaa&bbb) # 8
print(0b00001000)

# bit shifting used << and >> operators
print((aaa&bbb) >> 1) # 4
print((aaa&bbb) << 1) # 16

# bit shifting with compliment numbers
# allows setting process controls 
# tick from central positions are small
# this allows easily done human control
