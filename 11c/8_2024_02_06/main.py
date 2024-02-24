# prompt: ora elso resze a doga megoldasainak atnezesevel lesz
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

# prompt: ha ezzel nem menne el az ora....

# def: for ciklusok

# prompt: a for ciklusokat a while ciklusokkal ellentetben akkor hasznaljuk, ha tudjuk, hogy hany elemen akarunk vegig menni
# prompt: for ciklusokat hasznalunk listakon, stringeken, tuple-ken, dictionary-ken, set-eken
# prompt: for ciklusokat hasznalunk akkor is, ha nem tudjuk hany elemen akarunk vegig menni, de tudjuk, hogy milyen feltetel alapjan akarunk vegig menni
# prompt: for ciklusokat lehet hasznalni hogy vegigmenjunk egy lista elemein

# Task 1
print("Elso feladat")
szamok = [12, 567, 34]
# prompt: printeljuk ki a szamokat for ciklussal
for szam in szamok:
    print(szam)

# Task 2
print("Masodik feladat")
# prompt: printeljuk ki mindegyik szamrol hogy paros vagy paratlan
for szam in szamok:
    if szam % 2 == 0:
        print(f"A {szam} egy paros szam")
    else:
        print(f"A {szam} egy paratlan szam")


# prompt: a for ciklusokat lehet hasznalni a range() fuggveny segitsegevel
# prompt: range() parameterei: range(start, stop, step)
# prompt: start: a szam amivel kezdodik a range
# prompt: stop: a szam amivel veget er a range
# prompt: step: a lepeskoz, ami alapertelmezetten 1

# Task 3
print("Harmadik feladat")
# prompt: printeljuk ki az elso 10 szamot
for i in range(1, 11):
    print(i)
# prompt: fontos hogy a range() fuggveny a stop ertekig nem fogja kiirni a szamot, hanem a stop ertek elott all meg

# Task 4
print("Negyedik feladat")
# prompt: printeljuk ki az elso 20 paros szamot
for i in range(2, 21, 2):
    print(i)

# Task 5
print("Otodik feladat")
# prompt: rakjuk egy listaba az elso 10 3-mal oszthato szamot, majd ezeknek a szamoknak az osszeget
harommaloszthato = []
osszeg = 0
for i in range(3, 31, 3):
    harommaloszthato.append(i)
    osszeg += i

print(harommaloszthato)
print(osszeg)


# def uj operator: in
# prompt: az in operator segitsegevel tudjuk megnezni hogy egy elem benne van-e egy listaban, stringben, dictionary-ben, set-ben
# prompt: a in operator egy logikai erteket ad vissza, igazat ha benne van, hamisat ha nincs benne

# Task 1
print("Elso feladat")
szamok = [12, 567, 34]
# prompt: nezd meg hogy a 12 benne van-e a szamok listaban
if 12 in szamok:
    print("Benne van")

# Task 2
print("Masodik feladat")
# prompt: kerjunk be egy szot es nezzuk meg hogy benne van-e a szovegben a "a" betu
szoveg = input("Adj meg egy szot: \n")
if "a" in szoveg:
    print("Benne van")
else:
    print("Nincs benne")
