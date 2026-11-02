#
# numpy arrays
#

import matplotlib.pyplot as plt
import numpy as np
"""

# Array can be a single value
# yksittäisellä arvolla ei tarvita [] merkkejä
myarrayA = np.array(123) 

# Array can be 1-axis vector
# This is a group of points
# If you have two arrays, you can draw plots.
myarrayB = np.array([111,222,333,444,555,666])
print(myarrayB[1]) # toinen elementti
print(myarrayB[3:5]) # tulostaa neljännen ja viidennen elementin

# numpy array is not a list but NDArray class object
# it is, however, sequentical structure
# thus you can iterate through it
for laskuri in myarrayB:
    print(laskuri)


# array voi olla myös vaikkapa kaksiulotteinen vektori
# Voimme ajatella X ja Y akselien muodostavan pareja.
# Tässä on kolme lukua kahdessa ulottuvuudessa eli 
# X-akselilla on luvut 1, 10, ja 100. 
# Y-akselilla luvut ovat vastaavasti 2, 20 ja 200.
myarrayC = np.array([[1,10,100],[2,20,200]])
print(myarrayC[1,2]) # 200 eli toinen akseli, kolmas elementti
print(myarrayC[0,0:2]) # 1 ja 10 X-akselin ensimmäiset kaksi arvoa

for laskuri in myarrayC:
    # get arrays
    print("myarrayC is ", laskuri)
    # get points within arrays
    for laskuri2 in laskuri:
        print(laskuri2)


# array voi olla myös kolmiulotteinen matriisi
# Tässä on kaksi kolmessa ulottuvuudessa olevaa vektoria, 
# kussakin pisteessä on kolme lukua vastaten X, Y ja Z-akseleita
# eli tässä esitetään 2 kpl kolmessa ulottuvuudessa olevaa vektoria.
# vektoreilla on alkupiste(X,Y,Z) ja loppupiste (X,Y,Z).
matriisi = np.array([[[1, 2, 3], [4, 5, 6]], [[4, 2, 2], [4, 5, 6]]])
#print(matriisi.ndim) # 3 monta ulottuvuutta arrayssa on
#print(matriisi[0,1]) # [4,5,6] eli ensimmäisen vektorin loppupiste
#print(matriisi[1,0]) # [4,2,2] eli toisen vektorin alkupiste


# array voidaan kopioida. tämä luo uuden uuden arrayn.
# copy() on deep copy --- KÄYTÄ AINA TÄTÄ KOPIOIDESSASI JOTAIN!
# view() on shallow copy
matriisi2 = matriisi.copy()

# array voidaan liittää toiseen
dummyarrayA = np.array([1,2,3,4,5])
dummyarrayB = np.array([6,7,8,9,10])
finalarray = np.concatenate((dummyarrayA,dummyarrayB))
print(finalarray)

# split and array_split

# array voidaan luoda toisesta arraysta
# numeroarvo jakaa X osaan
# split ei salli epätasaista jakoa ja array_split sallii 
# split used as 10 elements divided into 2
anotherfinalarray = np.split(finalarray,2) 
print(anotherfinalarray)
anotherfinalarray = np.array_split(finalarray,3) 
print(anotherfinalarray)

# split and array_split are used when you have enormous
# data masses and splitting them into smaller and more
# manageable arrays makes sense.

# filter

# filter on komento, joka käy läpi arrayn ja palauttaa sieltä
# ne arvot jotka täyttävät jonkun ehdon
# täytetään esimerkiksi pohja-arvon settamiseen datasetissä

# tässä on filteröintiehto
# hyväksytään vain numerot, joiden arvo on suurempi kuin 6
# finalarray nimisestä arraysta
filtteriehto = finalarray > 6

# kutsutaan filtteröitävää arrayta ehdolla
haluttuarray = finalarray[filtteriehto]
haluttuarray2 = finalarray[finalarray > 6]
print(haluttuarray)
print(haluttuarray2)

# Bottom value allows filtering out unnecessary
# empty data before actual measurement.
"""

# If you need to filter out situations where
# both X and Y are filtered out if X is <= 25

dummyarrayA = np.array([11,33,66,11,33,88,33])
dummyarrayB = np.array([66,77,88,99,11,44,55])

testarrayA=dummyarrayA[dummyarrayA>25]
testarrayB=dummyarrayB[dummyarrayA>25]

print(testarrayA)
print(testarrayB)

"""
# random values

# luodaan 7 kappaletta sattumanvaraisia lukuja
# joiden arvo on välillä A ja B (kumpikin mukana)
# sama numero on mahdollinen
A = 1
B = 40
lottorivi = np.random.randint(A,B,size=7)
print(lottorivi)

# voidaan valita sattumanvarainen arvo arraysta
print(np.random.choice(lottorivi,replace=False))



# valitaan sattumanvarainen luku välillä 0 ja X-1
X = 100
print(np.random.choice(X))
# valitaan sattumanvarainen luku välillä 1 ja X
print(np.random.choice(X)+1)

# random noise is used a lot in indistry to simulate 
# noise in radio communications.

randomnoise = np.random.rand(7)
print(randomnoise)

# numpylla voidaan luoda array, jonka alkaa arvolla X ja päättyy arvoon Y-1
# tämä luo array -5,-4,-3,-2,-1,0,1,2,3,4,5
vapaamuotoinenarray = np.arange(-5,6)

# Thus we create finnish lottery with:
lotteryballs = np.arange(1,41) # set possible values as 1 to 40
lottorivi = []
for ball in range(7):
    lottorivi.append(np.random.choice(lotteryballs,replace=False))
print(lottorivi)

# distributions

# jakauma tarkoittaa tilastollista analyysia tilanteesta, jossa on
# otanta (suuri joukko havaintoja), joille lasketaan keskiarvo ja hajonta
# nämä arvot lasketaan kaavoilla, jotka riippuvat valitusta jakaumasta
# esimerkiksi Poisson käytetään usein odotusaikoja tutkittaessa.

# Tuhat henkeä jonottaa konserttiin (otanta = 1000)
# keskimääräinen jonotusaika on 10 minuuttia
# jonotus on Poisson jakauman mukainen
jonotus = np.random.poisson(lam=10, size=1000)


# Jonotin 8 minuuttia, moniko jonotti minua pitempään?
# vaatii seabornin asennuksen (pip install seaborn)

import seaborn as sns
sns.histplot(np.random.poisson(lam=10, size=1000), kde=False)
plt.show()
# Nyt katsotaan käyrää.... :)

# numpyssa on monta erilaista jakaumaa
# this is normal distribution
jakauma = np.random.normal(0)

#
# numpyharjoitus
#

# Tehkää kaksi arrayta
# Toinen saa määräämiänne arvoja (50-100 välillä)
# Toinen saa sattumanvaraisia arvoja (1-100 välillä)
# Yhdistäkää arrayt uudeksi arrayksi
# filteröikää pois alle 25 olevat arvot
# käyttäkää matplotlibiä ja näyttäkää käyrä

import matplotlib.pyplot as plt
import numpy as np


# 1) Tehkää kaksi arrayta
# Toinen saa määräämiänne arvoja (50-100 välillä)
# Toinen saa sattumanvaraisia arvoja (1-100 välillä)

# kirjoitan listan, josta teen arrayn
Xarvo = np.array([43,76,98,2,5,73,2,75,24,54])
# arvon joukon Yarvoja välillä 1-100
Yarvo = np.random.randint(1,100,size=10)

# 2) Yhdistäkää arrayt uudeksi arrayksi

# yhdistä X ja Y listat concatenate
sumarray = np.concatenate((Xarvo,Yarvo))

# 3) filteröikää pois alle 25 olevat arvot

# filteröi pois alle 25 olevat arvot
finalarray = sumarray[sumarray >= 25]
print(finalarray)

# 4) käyttäkää matplotlibiä ja näyttäkää käyrä

# piirrän arrayn
# tarvitsen X tasossa olevan akselin
# koska yksiulotteinen array ei voi esittää käyrää

#print(finalarray.size)
Xtaso = np.array([*range(0,finalarray.size,1)])

plt.title("numpy harjoitus")
plt.xlabel("Aika")
plt.ylabel("Arvot")

plt.plot(Xtaso, finalarray, color='black', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)

plt.show()

"""
