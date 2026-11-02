# python 117
# ==========

# listat

lista = [12,44,66,44]

for elementti in lista:
    print(elementti)

lista = ["Tupu","Hupu","Lupu"]

listaA = []
for elementti in lista:
    print(elementti)
    print(elementti[0])
    listaA.append(elementti[0])
print(listaA)

lista = []

for elementti in range(5):
    print(elementti)
    lista.append(elementti)
print(lista)

range(2, 5)
range(2, 11, 2) # 2,4,6,8,10...

lista = list(range(5))
lista = list(range(2,5))
lista = list(range(2,11,2))

# tehdään lista jossa on 5 nollaa
lista = [0]*5
print(lista)

listaB = [1]*3

# yhdistetään kaksi listaa
lista = lista + listaB
print(lista)


# Tehtävä 117-1: Tulosta merkkijono niin että kukin kirjain tulee omalle rivilleen ja kirjainten väliin tulee "%" merkki.
merkkijono = "Kasvi"
for elementti in merkkijono:
    print(elementti)
    print("%")

# Tehtävä 117-2: Tulosta luku niin että luku pienenee luvusta -lukuun asti.
luku = int(input("Anna luku? "))
if luku > 0:
    print(list(range(luku,-luku,-1)) + [-luku])
else:
    print(list(range(luku,-luku,1)) + [-luku])


# Tehtävä 117-3: Tulosta "*" niin, että kullekin riville tulee se lukumäärä, 
# joka on sanottu listan elementin arvona.
lista = [2,4,1]
for elementti in lista:
    print("*"*elementti)


# Tehtävä 117-4: ilmoita onko merkkijono anagrammi (täsmälleen samat kirjaimet) toisen merkkijonon kanssa
merkkijonoA = "bad"
merkkijonoB = "dab"
if sorted(merkkijonoA) == sorted(merkkijonoB):
    print(f"merkkijonot {merkkijonoA} ja {merkkijonoB} ovat anagrammeja")

# Tehtävä 117-5: ilmoita onko merkkijono palindromi (täsmälleen sama käännettynä toisinpäin) toisen merkkijonon kanssa
merkkijonoA = "bad"
merkkijonoB = "dab"
if list(merkkijonoA) == list(reversed(merkkijonoB)):
    print(f"merkkijonot {merkkijonoA} ja {merkkijonoB} ovat palindromeja")
# toinen vaihtoehto
if merkkijonoA == merkkijonoB[::-1]:
    print(f"merkkijonot {merkkijonoA} ja {merkkijonoB} ovat palindromeja")


# Tehtävä 117-6: laske yhteen ainoastaan negatiiviset numerot, jotka ovat listassa.
lista = [-1,3,6,-4]
summa = 0
for elementti in lista:
    if elementti < 0:
        summa += elementti
print(summa)

# Tehtävä 117-7: ilmoita parilliset luvut listasta.
lista = [-1,3,6,-4]
tulos = []
for elementti in lista:
    if elementti % 2 == 0:
        tulos.append(elementti)
print(tulos)

# Tehtävä 117-8: Laske yhteen kahden listan elementit.
listaA = [-1,3,6,-4]
listaB = [-3,2,-2,0]
# simppeli tekniikka
laskuri=0
lista = []
for elementti in listaA:
    lista.append(elementti+listaB[laskuri])
    laskuri += 1
print(lista)

# zip mahdollistaa monien listojen looppauksen
lista = []
for elementtiA, elementtiB in zip(listaA, listaB):
    lista.append(elementtiA+elementtiB)
print(lista)

# Tehtävä 117-9: Hae listasta ne elementit, joille ei ole paria.
lista = [1,4,2,8,5,2,8,5,2,9,6,8,7]
tulos = []
laskuri =0
for elementti in lista:
    if elementti in lista[laskuri+1:]:
        tulos.append(elementti)
    laskuri += 1
print(tulos)

# Tehtävä 117-10: Ilmoita lyhin listan merkkijono
lista = ["Hillo","Aapeli","Johannes"]
tulos = lista[0]
for elementti in lista:
    if len(elementti) < len(tulos):  
        tulos = elementti
print(tulos)

# Tehtävä 117-11: Ilmoita pisimmän listan merkkijonon pituus 
# ja näytä se
lista = ["Hillo","Aapeli","Johannes"]
tulos = lista[0]
for elementti in lista:
    if len(elementti) > len(tulos):  
        tulos = elementti
print(f"Pisin elementti oli {tulos}. Sen pituus on {len(tulos)}.")

