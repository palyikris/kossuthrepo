# dogaaa
# 1
lista = [1, 2, 3]
szam_str = "".join(map(str, lista))
szam = int(szam_str)
print(szam)

# 2
szo = input("irj egy szót: ")
nagybetuszam = sum(1 for karakter in szo if karakter.isupper())
print(nagybetuszam)

# 3
szamok = {1, 2, 3, 5, 7}

while szam in szamok:
    # ! ciklus nem mukodik
    if szam % 2 == 0:
        print("Megvan az első páros szám a listában:")
        print(szam)
        break
        # ! ugyes

# 4
szoveg = input("irj be egy szoveget: ")


# 5
a = int(input("adj meg egy szamot: "))
i = 1
szorzat = 1
while i <= a:
    szorzat *= i
    i += 1
print(szorzat)
osszeg = szorzat + a
fele = round(osszeg / 2, 0)
# ! nem jo a kerekites, int()
# prompt: print(fele)
# ! nem irtad ki a megoldast
