# this is my very first python program
# // and /*  */ do not work in Python
# instead we use #

# otetaan kirjastot ja modulit käyttöön
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([11, 20, 30])
ypoints = np.array([0, 25, 100])

muuttujajonoX = [14,16,22,28,31,39,44,46,58]

x2points = np.array(muuttujajonoX)
y2points = np.array([55,52,57,54,58,55,58,52,54])

plt.subplot(2,2,1)
plt.title("Duo Otsanappi bändin musiikin kuuntelu")
plt.xlabel("X-akselin label")
plt.ylabel("Y-akselin label")

plt.plot(xpoints, ypoints, color='blue', marker='*', linestyle='dashed',
     linewidth=1, markersize=2)

plt.subplot(2,2,2)
plt.title("Punamulta bändin levymyynti")

plt.plot(x2points, y2points, color='red', marker='+', linestyle='solid',
     linewidth=2, markersize=12)

plt.subplot(2,2,3)

plt.scatter(x2points, y2points)

plt.subplot(2,2,4)
plt.title("Asiakastyytyväisyys")
plt.ylabel("Palaute")

x = np.array(["Aarne", "Bertta", "Celsius", "Daavid"])
y = np.array([3, 8, 1, 10])

varitys = np.array(["red","green","black","blue"])

plt.bar(x,y,color=varitys)


plt.show()


