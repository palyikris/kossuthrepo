# 1
lista = [
    1,
    2,
    3,
]
szam_str = "".join(map(str, lista))
szam = int(szam_str)
print(szam)
# ! tipust is kell printelni
# 2
szo = input("adj meg egy szót")
nagybetűszám = sum(1 for karakter in szo if karakter.isupper())
# ! jovicc
print(nagybetűszám)
# 3
szamok = [1, 7, 8, 10, 12, 9, 3]

for szam in szamok:
    # ! nem szabad for
    if szam % 2 == 0:
        print("Megvan az első páros szám a listában:")
        print(szam)
        break
    # ! 16-ost be kellett rakni a listába


# 4
def hangrend(szó):
    mély_magánhangzók = ["a", "á", "o", "ó", "u", "ú"]
    magas_magánhangzók = ["e", "é", "i", "í" "ö", "ő", "ü", "ű"]
    volt_mély = False
    volt_magas = False
    for betű in szó:
        if betű in mély_magánhangzók:
            volt_mély = True
        elif betű in magas_magánhangzók:
            volt_magas = True
    if volt_mély and not volt_magas:
        return "mély"
    elif not volt_mély and volt_magas:
        return "magas"
    elif volt_mély and volt_magas:
        return "vegyes"
    else:
        return "nincs magánhangzó a szóban."


# ! se at in-t, se a def-et nem tanultuk meg
szó = input("írj ide egy szót!")
print(hangrend(szó))
# 5
a = int(input("adj meg egy számot !"))
i = 1
szorzat = 1
while i <= 1:
    szorzat *= 1
    # ! i-vel kell szorozni
    i *= 1
    # ! az i-t nem kell szorozni, hozzaadni kell --> igy vegtelen ciklus
print(szorzat)
osszeg = szorzat + a
fele = round(osszeg / 2, 8)
# ! nem jo a kerekites, int()
# ! nem irtad ki
