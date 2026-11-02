
# lotto

import random

ALKU = 1
LOPPU = 40
KAPPALEITA = 7

lottopallot = list(range(ALKU,LOPPU+1,1))
random.shuffle(lottopallot)

lotonarvonta = lottopallot[0:KAPPALEITA]
lotonarvonta.sort()

lottorivi = []
while True:
    try:
        numero = int(input("Anna numero välillä 1 ja 40? "))
        if numero >= ALKU and numero <= LOPPU:
            if numero not in lottorivi:
                lottorivi.append(numero)
            else:
                print(f"{numero} on jo listassa! ")
        else:
            print(f"{numero} ei ollut välillä 1 ja 40! ")            
        if len(lottorivi) >= KAPPALEITA:
            lottorivi.sort()
            break
    except:
        print(f"Tuo ei ollut numero!")

print(lotonarvonta)
print(lottorivi)

osumia = 0
for rivinumero in lottorivi:
    if rivinumero in lotonarvonta:
        print(f"{rivinumero} on lotonarvonnassa!")
        osumia += 1
print(f"Sait {osumia} oikein! ")
