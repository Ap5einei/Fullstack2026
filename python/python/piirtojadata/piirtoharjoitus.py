#
# Piirtoharjoitus
#

# Piirretään 6 taulua, joissa on
# histogrammi, piirakka, pylväs, jakauma ja käyrä
# ja yksi vapaavalinnainen....
# Data on itse keksimänne, jossa on 5 arvoparia

import matplotlib.pyplot as plt
import numpy as np

Xdata = [1,2,3,4,5]
Ydata = [3,6,4,7,9]
varitys = ["red","red","green","blue","yellow"]

Xarvo = np.array(Xdata)
Yarvo = np.array(Ydata)
Carvo = np.array(varitys)

plt.subplot(2,3,1)
plt.bar(Xarvo,Yarvo,color=Carvo)

plt.subplot(2,3,2)
plt.title("Piirakka",loc='left')
plt.pie(Yarvo,[0,0,1,0,1],labels=['','','talo','','auto'])

plt.subplot(2,3,3)
plt.title("pylväsdiagrammi")
plt.barh(Xarvo,Yarvo,color=varitys)

plt.subplot(2,3,4)
plt.title("jakauma")

plt.boxplot([Xarvo,Yarvo])

plt.subplot(2,3,5)
plt.title("käyrä")

plt.plot(Xarvo,Yarvo, color='red', marker='+', linestyle='solid',
     linewidth=2, markersize=12)

plt.subplot(2,3,6)
plt.title("pylväsdiagrammi")
plt.bar(Xarvo,Yarvo,color=varitys)

plt.show()
