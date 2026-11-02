#
# pandas cleaning
#
 
import matplotlib.pyplot as plt

import pandas as pd
print(pd.__version__)

# Asetukset
# Näytetään kaikki sarakkeet
pd.set_option('display.max_columns', None)

# STEP 1: Lue materiaali

# luodaan dataframe, jossa materiaali on
df = pd.read_csv("vaestolaskenta.csv")

# monta rivia on luettu ja onko data ja sarakkeet OK?
# Optio A: Tämä tulostaa ekat ja vipat rivit
print(df) 
# Optio B: Tämä tulostaa ekat rivit
print(df.head(5))
# Optio C: Tämä tulostaa vipat rivit
print(df.tail(5))

# STEP 2: Jalosta materiaali

# STEP 2.1: Miten toimimme tyhjien arvojen kanssa?

# Optio A: Poistetaan kaikki tyhjät rivit
# Ei hyvä, jos tyhjiä rivejä on paljon
df2_01a = df.dropna()

# Optio B: Korvataan tyhjät arvot sarakkeissa
# Luodaan omia "dummy arvoja". Ongelma on, mikä on hyvä?
# Esimerkiksi valitaan jokin sarake ja annetaan sille dummyarvo
df2_01b = df["ututku"].fillna(111)

# Vaihtoehto dummyarvolle on valita joko mean, median tai mode
# mean on keskiarvo
# median on mediaani eli puolet luvuista tätä suurempi/pienempi
# mediaani on stabiili vaihtoehto, luo "hyvin käyttäytyvän käyrän"
# mode on useinmiten tullut arvo
# mode sopii, jos arvo on laadullinen suure (ja laatuja on vähän)
df2_01b_mean = df["ututku"].mean()
df2_01b_median = df["ututku"].median()
df2_01b_mode = df["ututku"].mode()

# STEP 2.2: Väärän muotoisien arvojen käsittely

# 99% tapauksissa tämä on "timestamppien jumppausta"
# Näin poistetaan esimerkiksi "1900 vuoden luvut"
#df['Date'] = pd.to_datetime(df['Date'])

# toinen usein tarvittava käsittely on arvon muuttaminen 
# numeroksi to_numeric()
df['ututku'] = pd.to_numeric(df["ututku"])

# joskus koko aikakäsittely pitää asettaa erikseen
# Näin tehdään lähinnä sensoreissa
# to_timedelta()

# STEP 2.3: Väärän tiedon poistaminen ja muuttaminen käsin

# Joskus tuloksia on pakko säätää käsin
# Voi olla esimerkiksi syöttövirhe
# Tietyn rivin tietty sarake saa uuden käsin asetetun arvon
# Rivi 7, sarake "ututku" saa arvoksi 45
df.loc[7, 'ututku'] = 45

# Osa tuloksista voidaan poistaa kokonaan tietyillä ehdoilla
# Tämä on hyvin vaarallista mutta joskus huonot arvot on
# pakko poistaa
# esimerkiksi sensorin ensimmäiset sekunnit poistetaan
# Tässä poistetaan "karkulaiset" eli liian pitkät mahdottomat
# pituudet viallisina mittauksina

for laskuri in df.index:
  dummy = df.iloc[laskuri].to_list()
  if dummy[0] > 120:
    df.loc[laskuri, 'ututku'] = 120

# STEP 2.4: Duplikaattien käsittely

# Datassa voi olla duplikaatteja eli sama tieto on kahdesti
# jokainen mittaus olisi oltava vain kerran!

# tämä näyttää duplikaatit
# true = duplikaatti
print(df.duplicated())

# tämä poistaa duplikaatit
df.drop_duplicates()

# STEP 3: Esitä materiaali

# STEP 4: Analysoi materiaali tuloksien löytymiseksi

# Korrelaatio kertoo riippuuko joku arvo toisesta
# niin, että 0 tarkoittaa ettei korrelaatiota ole
# ja -1 tai 1 tarkoittaa että korrelaatio on 
# täsmälleen sama
# positiivinen arvo tarkoittaa että arvon nousu nostaa
# myös toista arvoa
# negatiivinen arvo tarkoittaa että arvon nousu laskee
# myös toista arvoa
# Korrelaatio ei kerro mikä on syy-seuraussuhde
# eli mikä johtaa toisen nousuun.
# SYY ON AINA ETSITTÄVÄ ERIKSEEN.
# Tässä voi käyttää esimerkiksi Kohosen karttaa.

print(df.corr())


df.plot(kind = 'scatter', x = 'vuosi', y = 'ika')
plt.show()

print(df.loc[0])
