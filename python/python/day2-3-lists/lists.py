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

#
# list copying
#

listAarne = [1,2,3,4]

# this is a shallow copy
# it only copies references
#listBertta = listAarne
#listAarne[0] = 111
#print(listAarne)
#print(listBertta)

# this is also imperfect copy
# in sense it does not copy objects within objects
#listBertta = listAarne.copy()
#listAarne[0] = 111
#print(listAarne)
#print(listBertta)


# Python 3.11.4 introduces the deepcopy()
# it copies also objects within objects
import copy
listBertta = copy.deepcopy(listAarne)
listAarne[0] = 111
print(listAarne)
print(listBertta)
# see also: https://docs.python.org/3.11/library/copy.html
