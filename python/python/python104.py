import enum
import csv
 
#
# enumeration
#
# enumeration is intended to create numbers for a list
# in essense it sets a number of values that can be used with list values
mylistA = ["Aarne", "Bertta", "Celsius", "Daavid"]

# enumerate() creates key-value pairs of value iterable
# printing the tuples in object directly
for ele in enumerate(mylistA, start=101):
    print (ele)
 
# changing index and printing separately
for count, ele in enumerate(mylistA, 100):
    print (count, ele)
 
# getting desired output from tuple
for count, ele in enumerate(mylistA):
    print(count)
    print(ele)

# here we do again enumeratation from iterable list
# enumerate() creates enumerated object
result = enumerate(mylistA, 1001)
print(result) # shows object address
print(next(result)) # 1001, aarne
print(next(result)) # 1002, bertta

# string can also be enumerated
result = enumerate("Hukkaputki",1001)
for i,j in result:
    print(i,j)

# actually you should not use enumerate!
# use "normal for" instead with dictionary
mydict = { 112: "Aarne", 543: "Bertta", 673: "Celsius", 878: "Daavid"}
for key,value in mydict.items():
    print(key,value)
# Note! Do not use enumerate if you already have key-value pairs!

# You can also create enumeration with hand
class Mylista(enum.Enum):
    Aarne = 1
    Bertta = 2
    Celsius = 3
    Daavid = 999

print(Mylista)
print(Mylista.Celsius) # Mylista.Celsius
print(Mylista.Celsius.name) # Celsius
print(Mylista.Celsius.value) # 3
print(Mylista.Daavid.value) # 999

for elementti in Mylista:
    print(elementti.name, elementti.value)

print(Mylista(999)) # Mylista.Daavid
print(Mylista(999).name) # Daavid

# esim: tehdään liikennevalot

class LIIKENNEVALOT (enum.Enum):
    Undefined = 0 #käytä tätä jos signaalia ei tule
    Punainen = 1
    Keltainen = 2
    Vihreä = 3
    Error = -1 # käytä, jos havaittu järjestelmävika

arvo = 3
if arvo == LIIKENNEVALOT.Vihreä.value:
    print("Liiku eteenpäin VIHREÄ")
if "Vihreä" == LIIKENNEVALOT.Vihreä.name:
    print("Liiku eteenpäin VIHREÄ")

liikennevalot = dict()
liikennevalot["Punainen"] = 1
liikennevalot["Keltainen"] = 2
liikennevalot["Vihreä"] = 3

arvo = 3
if arvo == liikennevalot["Vihreä"]:
    print("Liiku eteenpäin koska dict arvo")

print(list(liikennevalot.keys())[list(liikennevalot.values()).index(3)])

mylistA = ["Punainen", "Keltainen", "Vihreä"]
liikennevalotenum = dict(enumerate(mylistA,1))
print(liikennevalotenum)

arvo = 3
if arvo in liikennevalotenum:
    print("Liiku eteenpäin koska enum arvo")


#
# I/O operations
#

# STEP 1
# open connection to file object
# This is effectively an pointer to location of file object
# open(<name of file>, <mode>)
# mode is r = read, r+ = read and write
# w+ read and write (and overwrite), a = append to end of file
fileobject = open("testfile.txt","r+")

if fileobject:
    print("open was successful")

# STEP 2
# close connection to file object
fileobject.close()

#
# usually file operations employ try 
#

try:
    # open file to append new line
    fileobject = open("testfile.txt","a")

    fileobject.write("Kukkakeppi")

finally:
    fileobject.close()



# next step is reading the file contents

try:
    fileobject = open("testfile.txt","r")

    # read() is used to read characters
    # result = fileobject.read(10) # gets 10 characters
    result = fileobject.read() # gets all characters
    print(result)

finally:
    fileobject.close()

# this teachnique also reads file but line by line
try:
    fileobject = open("testfile.txt","r")

    # run through fileobject
    for line in fileobject:
        print(line)

finally:
    fileobject.close()

# you can also read using readline()
try:
    fileobject = open("testfile.txt","r")

    # reads first line of fileobject
    # result = fileobject.readline()
    # print(result)

    # reads all lines of fileobject
    # and stores them to an list
    result = fileobject.readlines()
    print(result)

finally:
    fileobject.close()


# finally .... lets store tupu, hupu and lupu
# to a file called storagefile.txt
# then we read the data
# see also:
# https://stackoverflow.com/questions/53283718/reading-a-file-line-by-line-in-python

try:
    # mode is w+ because we want to create new file if necessary
    # if no file is present, file is created
    # w+ overwrites existing content
    fileobject = open("storagefile.txt","w+")

    # write 3 lines of material
    fileobject.write("Tupu\n")    
    fileobject.write("Hupu\n")    
    fileobject.write("Lupu\n")    

finally:
    fileobject.close()

try:
    # We open storagefile for reading.
    # thus r is selected as mode
    fileobject = open("storagefile.txt","r")

    # here we read it all into list
    # result = fileobject.readlines()
    # print(result)

    # here we read from fileobject line by line
    for myline in fileobject:
        print("I read: ", myline)

finally:
    fileobject.close()


# Lets read CSV file

try: 
    with open("testi.csv") as mycsvfile:
        inputstream = csv.reader(mycsvfile,delimiter=";")
        title = True
        for row in inputstream:
            if title:
                print(row)
                title = False
            else:
                print("{} tyäskentellöö {}".format(row[0], row[2]))

except OSError:
    print("Problem opening csvfile")

finally:
    mycsvfile.close()
