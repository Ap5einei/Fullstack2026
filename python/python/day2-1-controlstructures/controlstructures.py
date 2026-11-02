#
# Control structures  
#

# We need to be able to decide how program behaves if 
# values change during program.
# In essense we want our program able to select 
# a plan of action or repeat action when necessary.

#
# if
#

# if carries out comparison that gives out boolean
# result of True or False.
# if <boolean comparison is true>:
#   <execure this>
# else:
#   <execute something else>

"""
mynumber = int(input("\nGive a integer number  "))
if mynumber % 2 == 0:
    print("\neven number")
else:
    print("\nodd number")
"""

# You can do more complex if structures if you use elif
# number of elif is not limited.
# 
# if <boolean comparison is true>:
#   <execure this>
# elif <another boolean comparison is true>:
#   <execute something else>
# else:
#   <execute something else>

"""
mynumber = int(input("\nGive a temperature number  "))
if mynumber <= 10:
    print("\nIt is cool outside")
elif mynumber > 10 and mynumber <= 15:
    print("\nIt is warm outside")
else:
    print("\nIt is hot outside")
"""

# What is correct size of if structure
# some kind of opinion is that more than 3 choices
# is too complex to intuitively understand.
# Most computer languages use switch case structure.

#
# switch case
#

# no support in python ... requires tricks

# case 1: use function
def myswitchfunction(value):
    #print(id(value))
    #print(id(1))
    match value:
        case 1:
            return 11
        case 2:
            return 22
        case 3:
            pass
        case 4 | 5: # or must use pipe!
            return 45
        # _ means everything else
        # equal to default
        case _:
            return 0

print(myswitchfunction(111)) # 0
print(myswitchfunction(1)) # 11
print(myswitchfunction(2)) # 22
print(myswitchfunction(3)) # ei mitään eli None
print(myswitchfunction(5)) # 45

# https://docs.python.org/3/tutorial/controlflow.html#match-statements
# https://peps.python.org/pep-0636/

class Point:
    x: int
    y: int

def mypointevaluation(point):
    match point:
        case Point(x=1, y=2):
            print("1 and 2")
        case _:
            print("Something else?")

mypoint = Point()
mypoint.x = 1
mypoint.y = 1
mypointevaluation(mypoint)

mypoint.x = 1
mypoint.y = 2
mypointevaluation(mypoint)

#
# loops
#
# while, for
# nested (loops within loops)
# break, continue, pass

# Loops allow executing same command again and again
# usually done for an array of elements
# alternatively going through user input again and again

numberlist = [4,7,3,1,8]
resultlist = []

# for goes through elements of an sequential structure.
# this requires some kind of index
for element in numberlist:
    dummy = element * 2
    resultlist.append(dummy)

print(resultlist)
resultlist.sort(reverse=True)
resultlist.pop(0) # takes avay first, which is 8 after sorting
resultlist.pop(-1) # takes avay last, which is 2 after sorting

print("for result is ",resultlist)

# for is usually used with range().  
# Range() is actually function used to create an object that
# is list of numbers
# range(start,end,iteration)
print(range(5))
print(list(range(5))) # 0,1,2,3,4
print(list(range(2, 5))) # 2,3,4
print(list(range(2, 10, 2))) # 2,4,6,8

# this is equal to:
# for (int i=1; i < 11; i++) in other languages
for element in range(1,11):
    print(element, end=" ") # 1,2,3,4,5,6,7,8,9,10
# for (int i=1; i < 11; i += 2) in other languages
print("")
for element in range(1,11,2):
    print(element, end=" ") # 1,3,5,7,9
print("")

# When you for?
# 1) Use for when you loop through existing sequence, usually list
# 2) Use it when you go through a set number of times, 
# usually using iiterator as index value

# while

# while <boolean comparison>:
#    <executing code here>

# you need external iterator
iter = 0
while iter < 5:
    iter += 1 # iterator should be first item in loop
    print(iter, end=" ")

print("")

# while is best when you have uncertain number of iterations
"""
carryloop = True
while (carryloop):
    # do something, until carryloop becomes False
    pass
"""

# Python has no support for do - while structure

#
# break and continue
#

# break leaves loop immediately
# Can be useful or problem depending on use case.
# Always check if loop must be executed to end before leaving!
# if you look for a hit in list, break out immediately
# if you need to carry loop to end, use boolean check in while

# continue returns to beginning of loop
# it does not always go next iteration
# therefor always iterate at first line with while

mystring = "kukkakeppi"

for element in mystring:
    if element == 'k':
        pass
        # you can actually write and execute lines in here
    else:
        print(element, end="")
print("")

for element in mystring:
    if element != 'k':
        print(element, end="")
print("")

# break leaves loop immediately
for element in mystring:
    if element == 'a':
        break
    print(element, end="")
else:
    # code never goes here as break
    # makes code leave loop immediately!
    print("Loop is over")
print("")

for element in mystring:
    if element == 'k':
        continue
        # code stops at continue, no lines are executed after it
    else:
        print(element, end="")
print("")

iter = 0
while iter < 5:
    iter += 1
    print(iter, end=" ")

print("")

iter = 0
while iter < 5:
    iter += 1
    print(iter, end=" ")
    # jos tässä olisi break, se heittää pois eikä elseä käydä läpi!
    if iter == 3:
        print("hit!")
        break
else:
    # else is fired for two reasons:
    # 2) loop ended without firing a break
    # ---> sopii tilanteisiin, joissa loopista ei löydy tuloksia
    print("While ended here!\n")

iter = 0
while iter < 5:
    iter += 1
    print(iter, end=" ")
else:
    # else is fired when loop ended without firing a break
    # ---> sopii tilanteisiin, joissa loopista ei löydy tuloksia
    print("While ended here!\n")

# while is very powerful
# First, you must fill the comparison before it goes to loop
# Have you considered scenarios where you do not execute
# loop at all?
# You can carry out else then.
looping = False
while(looping):
    print("looping")
else:
    # because looping was False, code goes here immediately
    print("looping ended so else")



