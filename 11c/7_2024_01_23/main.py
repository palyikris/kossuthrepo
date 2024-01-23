# prompt: ha a kód nem fut le, valami hiba van, nem kell aggodni meg lehet ra pontot kapni
# prompt: ha valahol elakadsz, kommentezd ki hogy ne zavarjon, es haladj a kovire
# prompt: 6 pont kell a ketteshez xd

# Def: Idő
# prompt: a dolgozatra 60 perc fog rendelkezésetekre állni

# Def: Pontozás
# prompt: feladatonként 7 pont
# prompt: 2p syntax, 3p gondolat, 2p ha elozokbol min 4, 1p ha elozokbol min 2

# Def: 5 feladat --> 5*7 --> 35 pontos doga
"""
35-29 --> 5
28-21 --> 4
20-14 --> 3
13-7 --> 2
6-0 --> 1
"""

# Task 1
print("Elso feladat")
szamok = [12, 567, 34]
szamok = [32, 93, 145]
# def: a listaban levo szamokat alakitsd at egy nagy int tipusu szamma
# def: es irasd ki. pl. [11, 22, 33] --> 112233
szam = ""
i = 0
while i < len(szamok):
    szam += str(szamok[i])
    i += 1
szam = int(szam)
print(szam)
print(type(szam))
print()

# Task 2
print("Masodik feladat")
szoveg = "NagYBetUk"
szoveg = "KIsBEtuK"
# def: szamold meg, hogy hany nagybetu van a szoban, es ird ki ezt a szamot, illetve
# def: gyujtsd ki a nagybetuket egy listaba es azt is ird ki
i = 0
nagybetuk = []
nagybetukszama = 0
while i < len(szoveg):
    if szoveg[i].upper() == szoveg[i]:
        nagybetuk.append(szoveg[i])
        nagybetukszama += 1
    i += 1
print(nagybetukszama)
print(nagybetuk)
print()

# Task 3
print("Harmadik feladat")
szamok = [3, 7, 2, 0, 1, 1, 6]
# def: keresd meg melyik sorszamon talalhato az elso paros szam a listaban es irasd ki
# def: az elso paros szam sorszama utan tegyel be a listaba egy 16-ost es irasd ki a listat
# def: ird ki, hogy a listaban hany 1-es van
parosindex = -1
i = 0
while i < len(szamok) and parosindex <= -1:
    if szamok[i] % 2 == 0:
        parosindex = i
    i += 1
print(parosindex)
szamok.insert(parosindex + 1, 16)
print(szamok)
print(szamok.count(1))
print()

# Task 4
# def: kerj be egy random szoveget a felhasznalotol.
# def: ha csak magas hangrendű betű van benne, akkor ird ki hogy csak magas van benne
# def: ha csak mely, akkor azt hogy csak mely
# def: ha vegyesen van benne, azt hogy vegyesen van benne
# def: hint = count()
print("Negyedik feladat")

magasak = ["e", "é", "i", "í", "ü", "ű", "ö", "ő"]
melyek = ["a", "á", "u", "ú", "o", "ó"]

szoveg = input("Adj meg egy szoveget: \n")
csakmagas = True
csakmely = True

i = 0
while i < len(szoveg):
    if magasak.count(szoveg[i]) > 0:
        csakmely = False
    elif melyek.count(szoveg[i]) > 0:
        csakmagas = False
    i += 1

if csakmagas:
    print("Csak magas.")
elif csakmely:
    print("Csak mely.")
else:
    print("Vegyes.")
print()

# Task 5
print("Otodik feladat")
# def: kerj be egy szamot a felhasznalotol
# def: add hozza a faktorialisat, aztan oszd el kettovel
# def: a szamot alakitsd egessze, hogy ne legyenek tizedesjegyek a vegen
# def: az igy kapott szam ele tegyel ket nullát. pl.: 564 --> 00564
# def: ird ki
szam = int(input("Adj meg egy szamot: \n"))
fakt = 1
i = 1
while i <= szam:
    fakt *= i
    i += 1
szam += fakt
szam /= 2
szam = int(szam)
szam = str(szam)
szam = "00" + szam
print(szam)
