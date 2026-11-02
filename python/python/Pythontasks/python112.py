# Merkkijonoja

# osajono
osajono = "joki"
merkkijono = "Seinäjoki"

print("jo" in merkkijono) # true
print(osajono in merkkijono) # true

print(merkkijono.find("jo")) # ilmoittaa indeksin
print(merkkijono.find("xxx")) # ei löydy, palauttaa -1

# Tehtävä 112-1: Etsi toinen "i" sanasta "Seinäjoki"
merkkijono = "Seinäjoki"
tulos = 0
if ("i" in merkkijono):
    laskuri = 0
    while laskuri < len(merkkijono):
        if ("i" in merkkijono[laskuri]):
            tulos = laskuri
        laskuri += 1
print(tulos)

# Tehtävä 112-2: Etsi ja ilmoita kaikki indeksit "i" sanalle sanasta "saippuakauppias"
merkkijono = "saippuakauppias"
if ("i" in merkkijono):
    laskuri = 0
    while laskuri < len(merkkijono):
        if ("i" in merkkijono[laskuri]):
            print(laskuri)
        laskuri += 1

# Tehtävä 112-3: Etsi kaikki kolmemerkkiset osajonot, jotka alkavat kirjaimella "a" sanasta "saippuakauppias"
merkkijono = "saippuakauppias"
if ("i" in merkkijono):
    laskuri = 0
    while laskuri < len(merkkijono):
        if ("i" in merkkijono[laskuri]):
            print(merkkijono[laskuri:laskuri + 3])
        laskuri += 1

