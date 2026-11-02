
#
# numpyharjoitus
#

# Tehkää kaksi arrayta
# Toinen saa määräämiänne arvoja (50-100 välillä)
# Toinen saa sattumanvaraisia arvoja (1-100 välillä)
# Yhdistäkää arrayt uudeksi arrayksi concatenate
# filteröikää pois alle 25 olevat arvot
# käyttäkää matplotlibiä ja näyttäkää käyrä

import matplotlib.pyplot as plt
import numpy as np


# kirjoitan listan, josta teen arrayn
Xarvo = np.array([43,76,98,2,5,73,2,75,24,54])
# arvon joukon Yarvoja välillä 1-100
Yarvo = np.random.randint(1,100,size=10)

# yhdistä X ja Y listat concatenate
sumarray = np.concatenate((Xarvo,Yarvo))

# filteröi pois alle 25 olevat arvot
finalarray = sumarray[sumarray >= 25]
print(finalarray)

# piirrän arrayn
# tarvitsen X tasossa olevan akselin
# koska yksiulotteinen array ei voi esittää
print(finalarray.size)
Xtaso = np.array([*range(0,finalarray.size,1)])

plt.title("numpy harjoitus")
plt.xlabel("Aika")
plt.ylabel("Arvot")

plt.plot(Xtaso, finalarray, color='black', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)

plt.show()
