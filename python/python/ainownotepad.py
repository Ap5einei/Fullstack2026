#print("Hello world!")
import abc
import enum

class LIIKENNEVALOT (enum.Enum):
    Undefined = 0 #käytä tätä jos signaalia ei tule
    Punainen = 1
    Keltainen = 2
    Vihreä = 3
    Error = -1 # käytä, jos havaittu järjestelmävika

arvo = 3
if arvo == 3:
    print("Liiku eteenpäin VIHREÄ")

if arvo == LIIKENNEVALOT.Vihreä.value:
    print("Liiku eteenpäin VIHREÄ")
if "Vihreä" == LIIKENNEVALOT.Vihreä.name:
    print("Liiku eteenpäin VIHREÄ")

LIIKENNEVALOTIETO = dict()
LIIKENNEVALOTIETO["Punainen"] = 1
LIIKENNEVALOTIETO["Keltainen"] = 2
LIIKENNEVALOTIETO["Vihreä"] = 3

arvo = 3
if arvo == LIIKENNEVALOTIETO["Vihreä"]:
    print("Liiku eteenpäin koska dict arvo")

print(list(LIIKENNEVALOTIETO.keys())[list(LIIKENNEVALOTIETO.values()).index(3)])

