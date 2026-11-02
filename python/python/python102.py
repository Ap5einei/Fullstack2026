print("testi")

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


#
# if
#

"""
mynumber = int(input("\nGive a integer number  "))
if mynumber % 2 == 0:
    print("\neven number")
else:
    print("\nodd number")
"""

"""
mynumber = int(input("\nGive a temperature number  "))
if mynumber <= 10:
    print("\nIt is cool outside")
elif mynumber > 10 and mynumber <= 15:
    print("\nIt is warm outside")
else:
    print("\nIt is hot outside")
"""


#
# loops
#
# while, for
# nested (loops within loops)
# break, continue, pass

"""
numberlist = [4,7,3,1,8]
resultlist = []

for element in numberlist:
    dummy = element * 2
    resultlist.append(dummy)

resultlist.sort(reverse=True)
resultlist.pop(0) # takes avay first, which is 8 after sorting
resultlist.pop(-1) # takes avay last, which is 2 after sorting

print("for result is ",resultlist)
"""


mystring = "kukkakeppi"

for element in mystring:
    if element == 'k':
        pass
        # you can actually write and execute lines in here
    else:
        print(element, end="")
    print("#")

for element in mystring:
    if element == 'k':
        continue
        # code stops at continue, no lines are executed after it
    else:
        print(element, end="")
    print("#")


print("")

for element in mystring:
    if element != 'k':
        print(element, end="")


# range()
# starts with 0 and adds integer numbers
print("")
print(range(5))
print(list(range(5))) # 0,1,2,3,4
print(list(range(2, 5))) # 2,3,4
print(list(range(2, 10, 2))) # 2,4,6,8

print(list([0]*7)) # 0,0,0,0,0,0,0

# this is equal to:
# for (int i=1; i < 11; i++) in other languages
for element in range(1,11):
    print(element, end=" ") # 1,2,3,4,5,6,7,8,9,10

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
    if iter == 14:
        print("hit!")
        break
else:
    # else is fired for two reasons:
    # 2) loop ended without firing a break
    # ---> sopii tilanteisiin, joissa loopista ei löydy tuloksia
    print("While ended here!\n")

# continue
# return to beginning of loop 
# and select next element
for element in mystring:
    if element == 'k' or element == 'i':
        continue
    print(element, end=" ")
else:
    print("Loop is over")
print("")

# break
# leave loop immediately
for element in mystring:
    if element == 'a':
        break
    print(element, end=" ")
else:
    # code never goes here as break
    # makes code leave loop immediately!
    print("Loop is over")
print("")


#
# switch case
#
# no support in python ... requires tricks

# case 1: use function
def myswitchfunction(value):
    print(id(value))
    print(id(1))
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
# strings
#

mystring = "saippuakauppias"

print(mystring[0]) # s
print(mystring[1]) # a

# colon operator is commonly used
# https://www.askpython.com/python/examples/when-to-use-colon-python
# https://docs.python.org/3/tutorial/introduction.html#strings
print(mystring[:]) # saippuakauppias
print(mystring[:4]) # saip

print(mystring[0:4]) # saip
print(mystring[2:4]) # ip

mystring = "saippuakauppias"

for elementti in range(2,4,1):
    print(mystring[elementti], end="")
else:
    print("")

print(mystring[2:4])


# negative numbers start from last element
print(mystring[-1]) # s
print(mystring[-4:]) # pias
print(mystring[-3:-1]) # ia

# code to create immutable string as mystring[3] = 'Q'
def myfunc(arvo, uusi, numero):
    alku = arvo[0:numero]
    loppu = arvo[numero+1:]
    return alku + uusi + loppu

print(myfunc(mystring, 'Q', 3))


# format
print("hei {} ja {}\n".format("Aku","Ankka"))
print("hei {1} ja {0}\n".format("Aku","Ankka"))

aaa = "Aku"
bbb = "Ankka"
print("hei {aaa} ja {bbb}\n") # väärin
print(f"hei {aaa} ja {bbb}\n") # oikein

nimi = ['Kemppi', 'Janne', 'Tuomas']
print(f'Nimeni on {nimi[0]}, {" ".join(nimi[1:])}.')

# changing value of immutable string
# this requires use of lists and join()
mystring = "Hullo World!"
mylist = list(mystring)
print(mylist)
mylist[1] = "e"
print(mylist)
mystring = "".join(mylist)
print(mystring)

print(len(mystring)) # 12 is length of string
print(mystring.find("W")) # index is 6
print(mystring.find("Ö")) # index is -1

print("Wo" in mystring) # True
print("ÖÖ" in mystring) # False

#
# List
#

mylistA = [111,222,333]
mylistB = [444,555,666]
# colon commands work like they did with string
print(mylistA[0:2]) # 111,222

print(111 in mylistA) # True
print(112 in mylistA) # False

# concatenation works...
# https://www.digitalocean.com/community/tutorials/concatenate-lists-python
mylistC = mylistA + mylistB
print(mylistC)

mylistC = []
mylistC = mylistA
mylistC.extend(mylistB)
print(mylistC)
print(len(mylistC)) # 6



# adds to end
mylistC.append(1234)
print(mylistC)

# adds to index, here it is 1
mylistC.insert(1, 9999)
print(mylistC)

# remove first occurrence of some value
mylistC.remove(222)

mylistC.pop(-1) # takes out last element
print(mylistC)

print(max(mylistC)) # 9999

mylistC = [0]*5 # [0,0,0,0,0]
print(mylistC)
mylistC = [*range(0,5,1)] # [0,1,2,3,4]
print(mylistC)


listAarne = [1,2,3,4]

# this is a shallow copy
# it only copies references
#listBertta = listAarne
#listAarne[0] = 111
#print(listAarne)
#print(listBertta)

# this is also imperfect copy
# in sense it does not copy objects within objects
listBertta = listAarne.copy()
listAarne[0] = 111
print(listAarne)
print(listBertta)

# Python 3.11.4 introduces the deepcopy()
# it copies also objects within objects
# import copy
# listBertta = copy.deepcopy(listAarne)
# listAarne[0] = 111
# print(listAarne)
# print(listBertta)
# see also: https://docs.python.org/3.11/library/copy.html

