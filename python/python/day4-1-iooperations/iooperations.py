#
# I/O operations
#

# Lets read CSV file
import csv

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
