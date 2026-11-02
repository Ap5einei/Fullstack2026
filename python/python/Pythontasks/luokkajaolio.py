# Luokka ja olio
# ==============

# olio-ohjelmointi = object oriented programming (tai OOP)
# luokka = class
# olio = object

# Luokalla on aina ominaisuuksia ja toimintoja
# ominaisuudet ovat luokassa määritettyjä muuttujia
# toiminnat ovat funktioita, joilla luokan jäsenet tekevät jotain

# luokan avulla rakennetaan olioita.
# luokka on siis malli.
# olio on mallin mukaan luotu yksittäinen asia.

# Olio on aina erillinen toisesta oliosta.
# Oliot elävät omaa elämää muista olioista riippumatta.

# Olion ominaisuudet voivat saada uusia arvoja sen elinaikana.

# Luokissa määritetään myös toimintoja (funktioita/metodeita).
# Näin kukin erillinen olio tekee mitä sen pitää tehdä.
# Toiminta on muista olioista riippumatonta.
# Toimnnoilla olion sisäisiä tietoja käytetään halutun toiminnan saavuttamiseksi.
# Toiminnat keskittyvät siihen mitä olion pitäisi pystyä tekemään.
# Muita toimintoja ei tarvitse eikä pidä tukea.

from doctest import REPORT_UDIFF

class Henkilo:
    # konstruktori
    def __init__(self, nimi: str, ika: int) -> None:
        self.nimi = nimi
        self.ika = ika

    # jokainen funktio aloitetaan varatulla sanalla.
    # sana viittaa olioon itseensä.
    # Se on konventiona self mutta on vapaamuotoinen.
    # KÄYTÄ TÄSSÄ AINA self SANAA!!!!!
    def sanonimi(self) -> None:
        print(f"Nimeni on {self.nimi}!")

    def koe(kukkaruukku,arg):
        print(f"Vapaamuotoinen teksti {arg} {kukkaruukku.nimi}")

# tässä näkyy että kukin olio on luomisensa jälkeen itsenäinen toisista!
henkilo1 = Henkilo("Aku Ankka", 313)
henkilo2 = Henkilo("Iines Ankka", 123)
print(henkilo1.nimi)
print(henkilo2.nimi)
henkilo2.nimi = "Roope Ankka"
print(henkilo1.nimi)
print(henkilo2.nimi)
henkilo1.sanonimi()
henkilo2.sanonimi()
henkilo1.koe(1234)

print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")

# Olio-ohjelmoinnin A ja O on suunnittelu
# Periaatteessa kaikki luokat on suunniteltava etukäteen

# Asiakas luokka
# Sen on pystyttävä:
# Etsiä kirjoja
# Lainata ja palauttaa kirjoja
# Maksaa sakot
# --> Jokainen näistä asioista on toiminnallisuus eli metodi/funktio

# Seuraavaksi mietitään ominaisuudet, jotka tukevat toimintoja
# Esim Kirja luokka:
# Tekijä
# sivujenmäärä
# julkaisuvuosi
# Nimi
# ISBN/ISSN numero

# Suunnittelu toimii yksinkertaisesti seuraavasti:
# Kuka on toimija tai toiminto/prosessi? --> Luokka
# Mitä toimija tekee? --> Luokalle määritettävät metodit
# Millä arvoilla tehdään? --> Luokalle määritettävät ominaisuudet
# Onko muita ominaisuuksia? --> Luokalle määritetään "elämää helpottavat" ominaisuudet
# ---> Nämä ominaisuudet liittyvät "työpaikan hiljaiseen tietoon"
 


# luokka määritetään sanalla class
# Luokan nimi on vapaa ja kirjoitetaan yleensä isolla etukirjaimella.
# class on varattu sana. Sitä ei saa käyttää.
class kokeiluluokka:
    def __init__(self) -> None:
        self.koe = ""

kokeiluluokanolio = kokeiluluokka()
kokeiluluokanolio.koe = "koe"

class Eläin:
    # luokalla on aina konstruktori eli kuinka se rakennetaan
    # oliota luodessa konstruktori ajetaan luodulle oliolle
    def __init__(self) -> None:
        # Tähän laitetaan kaikki alustamiseen liittyvät asiat
        # eli ominaisuudet esitellään ja annetaan alkuarvot
        self.nimi = ""

elukka1 = Eläin()
elukka1.nimi = "Sylvi"
print(elukka1.nimi)
elukka2 = Eläin()
print(elukka2.nimi)

print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")

class Kissa:
    def __init__(self, rotu, nimi, sukupuoli, ikä) -> None:
        # Tässä on olion ominaisuuksia, joille annetaan alkuarvo
        # arvo määritetään kutsuessa Kissa() 
        self.rotu = rotu
        self.nimi = nimi
        self.sukupuoli = sukupuoli
        self.ikä = ikä

    # toimintoja tehdessä self määrittää, että voidaan käyttää omia ominaisuuksia
    def kävelee(self):
        print(f"{self.nimi} kävelee")
    # toiminnoilla voi olla myös parametrejä
    def kehrää(self, kuvaus):
        print(f"Kissa kehrää {kuvaus}...")

kissa1 = Kissa("","Jenny","F",13)

# kutsussa sanaa self ei tarvita
kissa1.kävelee()
kissa1.kehrää("iloisesti")

# Tehtävä 1 - luo kaksi kissaa lisää
# anna niille ominaisuuksia, muuta niitä ja kutsu funktioita
kissa2 = Kissa("Katti","Kali","M",16)
kissa3 = Kissa("Katti","Galileo","M",16)
kissa3.ikä = 14
kissa3.kehrää("")

# Perintä

# Luokka ei välttämättä pysty venymään kaikkeen
# Toimintojen kasautuminen lisää monimutkaistumista!
# Yleensä se tarkoittaa erikoistapauksia ja -tilanteita.
# --> Tällöin käytetään perintää

# Perintää voidaan käyttää kahteen ohjelmointitapaan:
# 1) aggregaatti
# Luokka koostuu useasta luokasta ja oliosta.
# Periaatteessa hyvin vapaa ja käsitellään 105 ja 106 luennoissa.
# 2) erikoistapauksen käsittelyä.
# Äärimmäisen yleinen, yli 99 % käyttötapauksista.
# Käsitellään tässä.
# Ideana on hoitaa erikoistilanne perityssä luokassa.
# --> äitiluokka pysyy yksinkertaisena
# --> lapsiluokka hoitaa erikoistapauksen

# lapsiluokka luodaan <lapsiluokan nimi> (<äitiluokan nimi>)
# Siamilainen luokka perii Kissa luokan
class Siamilainen (Kissa):
    def __init__(self, rotu, nimi, sukupuoli, ikä, laatu) -> None:
        # lapsiluokkaa luodessa, se kutsuu aluksi äitiluokan konstruktoria
        # Tämä käyttää funktiota super(), joka viittaa äitiluokkaan
        super().__init__(rotu, nimi, sukupuoli, ikä)
        # tämän jälkeen konstruktori rakennetaan lapsiluokan asioille.
        # Tekniikka on sama kuin yhden luokan yhteydessä.
        self.rotu = "Siamilainen"
        self.laatu = laatu

    # Leijonanosa perivän luokan koodista on äiti-luokan muokkausta.
    # Tämä tarkoittaa kahta asiaa:
    # 1) override eli uudelleen implementointi
    # --> äitiluokan metodi kirjoitetaan uusiksi
    # 2) uusien metodien lisääminen
    # --> kirjoitetaan aivan uusia metodeja

    # tämä on uusi toiminto, jota EI ole äitiluokassa
    def kilpailee(self):
        print(f"{self.nimi} kilpailee ja laatu on {self.laatu}!")

    # perivä luokka voi myös muuttaa toiminnallisuutta äidistä
    # overriden idea on yleensä säilyttää sama function signature.
    # Tällöin funktion nimi ja argumentit ovat samat.
    # Tämä puolestaan mahdollistaa polyformismin.
    # Tällöin sama funktiokutsuu toimii sekä äitiluokan 
    # että lapsiluokan metodikutsuissa. 
    # Katso esimerkki alla.
    def kehrää(self, kuvaus):
        # Yleensä teemme omaa toiminnallisuutta!
        print(f"Siamilainen {self.nimi} kehrää {kuvaus}...")
        # Joskus halutaan kuitenkin kutsua äitiluokan metodeja
        # tällöin otetaan kiinni äitiluokkaan super() metodilla.
        # tässä kutsutaan äitiluokan kehrää(kuvaus) funktiota
        super().kehrää(kuvaus)  

siamilainen1 = Siamilainen("","Leonardo","M", 1, "erinomainen")
# perivä luokka perii äidin ominaisuudet ja toiminnat
siamilainen1.kävelee()
# perivällä luokalla voi olla uusia toimintoja, 
# joita käytetään kuten toimintoja yleensäkin
siamilainen1.kilpailee()
siamilainen1.kehrää("kauniisti")

# perintää voi ketjuttaa loputtomasti.
# lapsen alla voi olla toinen lapsi...
class ErikoisSiamilainen (Siamilainen):
    def __init__(self, rotu, nimi, sukupuoli, ikä, laatu) -> None:
        super().__init__(rotu, nimi, sukupuoli, ikä, laatu)

    def kehrää(self, kuvaus):
        print("Erikoissiamilainen näyttää!")
        super().kehrää(kuvaus)

erikoissiamilainen = ErikoisSiamilainen("Erikoissiamilainen","Galileo","M",111,"Excellent")
erikoissiamilainen.kehrää("erikoissiamilaisesti")

# Polymorphismi liittyy perintään.
# Se tarkoittaa toiminnallisuuden periytymisen vaikutuksia.
# Perusajatus on, että lapsiluokilla on yhteisiä toimintoja 
# Esimerkiksi kaikilla graafisilla elementeillä se on piirtäminen!
print("-------------------------")
kissalista = []
kissaluokat = (Kissa, Siamilainen, ErikoisSiamilainen)

def lisääoliolistaan(olio: object, lista: list, luokat: tuple) -> bool:
    if isinstance(olio, luokat):
        lista.append(olio)
        return True
    return False

if isinstance(kissa1, kissaluokat):
    kissalista.append(kissa1)
if isinstance(kissa2, kissaluokat):
    kissalista.append(kissa2)
if isinstance(kissa3, kissaluokat):
    kissalista.append(kissa3)
if isinstance(siamilainen1, kissaluokat):
    kissalista.append(siamilainen1)
if isinstance(erikoissiamilainen, kissaluokat):
    kissalista.append(erikoissiamilainen)

for kissa in kissalista:
    kissa.kehrää("kauniisti")

