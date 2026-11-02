import math
# lambda funktiot
# funktionaalinen ohjelmointi
 

# Aiheesta lisää:
# https://medium.com/akava/functional-programming-in-python-e492f2ad1e37
# https://realpython.com/python-functional-programming/
# https://docs.python.org/3/howto/functional.html

# lambda funktiot
# lambda funktiot eli nuolifunktiot ovat anonyymejä funktioita
# Ne voivat ottaa argumentiksi funktion.
# <muuttuja> = lambda <argumentit>: <funktio>

# Lue lisää:
# https://www.javatpoint.com/python-lambda-functions

pytagora = lambda arg1,arg2: math.sqrt(arg1**2 + arg2**2) 

print(pytagora(2,3)) # about 3.6

myhelloworld = lambda arg: print("Hello {}".format(arg))

myhelloworld("Jussi!")

# lambdaa voi käyttää myös if lauseessa
# https://www.geeksforgeeks.org/ternary-operator-in-python/
iftesti = lambda arg1,arg2: arg1 if (arg1 > arg2) else arg2 

print(iftesti(5,3)) # 5
print(iftesti(10,18)) # 18

# Lambda on yhden käskyn sisältävä funktio.
# Monimutkainen toiminta vaatii: 
# 1) saman lambdan uudelleenkäyttöä
# 2) monta erillistä lambda funktiota

# Mikä on suurin A, B vai C?
aaa = 8
bbb = 14
ccc = 22
print(iftesti(iftesti(aaa,bbb),ccc))

# Hae kolmanneksi suurin luku, jokaisesta listasta
lista = [ 
    [ 11,33,44,55], # 44
    [ 88,55,33,22,77] # 77
]  

# step 1 : lamda funktio joka sorttaa listan  
sortattulista = lambda arg : ( sorted(n) for n in arg )  

# step 2 : hae kolmanneksi suurin 
haekolmasarvo = lambda arg, func : [ l[ len(l) - 2] for l in func(arg)]  

print(haekolmasarvo(lista, sortattulista) ) # 44, 77
  
# funktionaalinen ohjelmointi
# https://medium.com/akava/functional-programming-in-python-e492f2ad1e37
# funktionaalisessa ohjelmoinnissa: 
# 1) funktio voidaan antaa argumenttina muuttujalle
# 2) funktio voidaan palauttaa kutsujalleen (callback)

# 1) funktio voidaan antaa argumenttina muuttujalle
def myfunctionA(arg):
    print(arg)

# funktio annetaan muuttujalle arvoksi (argumentiksi)
myvariableA = myfunctionA
myvariableA("kokeilu")

# funktio voidaan antaa argumenttina myös toiselle funktiolle

# Tässä esimerkissä funktio B annetaan argumenttina funktio Clle

def myfunctionB():
    print("testifunktio")

def myfunctionC(functionname):
    functionname()

myfunctionC(myfunctionB)

# tässä esimerkissä funktio A annetaan argumenttina funktio Dlle
# D ottaa myös muita argumentteja, jotta A saa argumentin
def myfunctionD(functionname,arg):
    functionname(arg)

myfunctionD(myfunctionA,"Hello world!") # tulostaa "Hello world!"

# tässä esimerkissä luodaan funktio, joka palauttaa arvon kutsujalleen

def myfunctionE(arg):
    return arg*2

def myfunctionF(functionname,arg):
    return functionname(arg)

print(myfunctionF(myfunctionE,111)) # 222

# Seuraava koodi näyttää funktionaalista koodausta käytännössä:
# map() funktio on ylläolevan esimerkin kaltainen koodi.
# logiikka: <funktio eli map>(<ajettava funktio>, <argumenttilista>)
# map() tekee ajettavan funktion jokaiselle listan elementille
celsius_temps = [0, 12, 34, 100]

def myconverter(arg: int) -> float:
    return float(arg * 9/5 + 32)

def mymap(funktioarg, lista) -> list:
    dummylista = []
    for element in lista:
        dummylista.append(funktioarg(element))
    return dummylista

# Tämä on esimerkki funktionaalisesta ohjelmoinnista
# annamme funktion ja argumenttinä lista arvoja
# tämä on sama kuin map()
ancient_temps = mymap(myconverter, celsius_temps)
print(list(ancient_temps))  

# sama voidaan esittää myös lambda koodia käyttäen
fahrenheit_temps = mymap(lambda c: (c * 9/5) + 32, celsius_temps)
print(list(fahrenheit_temps))  

# Huom: Pythonissa on sama toiminnallisuus valmiilla map() funktiolla
normal_temps = map(myconverter, celsius_temps)
print(list(normal_temps))  

# map() lambda koodia käyttäen
lambda_temps = map(lambda c: (c * 9/5) + 32, celsius_temps)
print(list(lambda_temps))

