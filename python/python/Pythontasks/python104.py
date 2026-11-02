
# Python 104

# Aritmetiikkaa
# perusasiat ovat + - * /
# // jako kokonaisluvuksi
# % modulo eli jakojäännös
# ** potenssi

aaa = 5
bbb = 2
print (aaa / bbb)
print (aaa // bbb)
print (aaa % bbb)

aaa = 4
bbb = 7
print (aaa / bbb)
print (aaa // bbb)
print (aaa % bbb)

print (aaa ** bbb)

# muista että () ovat aina korkein laskemisjärjestyksessä!

# Python 104-1: Laske painoindeksi BMI eli paino jaettuna pituuden neliöllä (pituus metreinä).
paino = 112
pituus = 1.77
print(f"Painoindeksisi on {paino/(pituus**2)}")

# Python 104-2: Kerro minä vuonna synnyit ja laske näin kuinka vanha olet
syntymavuosi = int(input("Milloin synnyit? "))
print(f"Ikäsi on {2022-syntymavuosi}")

# Python 104-3: Kerro nimesi ja minä vuonna synnyit ja kirjoita seuraavaa:
# Nimesi on <nimi> ja olet <X> vuotta vanha.
nimi = input("Mikä on nimesi? ")
syntymavuosi = int(input("Milloin synnyit? "))
print(f"Nimesi on {nimi} ja olet {2022-syntymavuosi} vuotta vanha.")

# Python 104-4: Määritä luku ja ilmoita sen potenssi kahteen.
luku = 4
print(luku**2)

# Python 104-5: Määritä kaksi lukua ja laske niiden potenssi.
lukuAAA = 4
lukuBBB = 2
print(lukuAAA**lukuBBB)

# Python 104-6: Kerro tietokoneelle monta päivää on kyseessä ja laske niiden minuuttien lukumäärä
paivienlukumaara = int(input("Monta paivää? "))
print(f"Minuutteja on {paivienlukumaara*24*60}")

# Python 104-7: Syötä kolme lukua ja laske niiden tulo
lukuEka = int(input("Anna luku? "))
lukuToka = int(input("Anna luku? "))
lukuKolmas = int(input("Anna luku? "))
print(lukuEka*lukuToka*lukuKolmas)

# Python 104-8: Syötä kolme lukua ja laske niiden summa
lukuEka = int(input("Anna luku? "))
lukuToka = int(input("Anna luku? "))
lukuKolmas = int(input("Anna luku? "))
print(lukuEka+lukuToka+lukuKolmas)

# Python 104-9: Syötä kolme lukua ja laske niiden keskiarvo
lukuEka = int(input("Anna luku? "))
lukuToka = int(input("Anna luku? "))
lukuKolmas = int(input("Anna luku? "))
print((lukuEka+lukuToka+lukuKolmas)/3)

