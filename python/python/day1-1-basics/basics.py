
#
# commenting your Python program
#


# This is a single line comment

"""
This is a way to do 
multi line comment.
"""

#
# print
#

# You can simply write text using print
print("Hello World!")

# print can be used with variables
variableA = 123
variableB = variableA + 456
print("variableA = ", variableA)
print("variableA = ", variableA, "variableB = ", variableB)


# print have sep and end arguments
# sep is what is printed between previous statements
# end is what is printed at end of everything
print("Jukolassa on ", 7, "veljestä", sep="\n", end=".\n")
print("Jukolassa on", 7, "veljestä", sep=" ", end=".\n")

# print uses special characters
print("My name is O'Malley")
print("This is \"fun\" training!")
print("This is 'fun' training!")

# print uses r to denote raw string
# this causes warning!
#print('C:\some\name')  # \name is shown as \n 
#print('C:\\some\\name')  # shows correctly
print(r'C:\some\name')  # r before the quote shows info correctly

# ääkköset
tämämuuttuja = 1234
print(tämämuuttuja)

#
# string literals
#

# allows writing multiline raw text
print(
"""
    this is
7
    brothers.
"""
)

# You can combine strings with + 
# and even without any sign
print("This is " + "7 brothers!")
print("This is " "7 brothers!")

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
#mytupleA[0] = "Kukka" # causes error
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


