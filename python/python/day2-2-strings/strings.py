
#
# strings
#

mystring = "saippuakauppias"

# string is an immutable list of characters
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

def returnstring(str, start, end):
    dummy = []
    for elementti in range(start,end,1):
        dummy.append(str[elementti])
    return dummy

print("".join(returnstring(mystring,2,4)))


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


