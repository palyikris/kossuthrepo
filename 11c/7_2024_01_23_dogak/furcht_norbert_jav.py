lista = [2, 6, 5]

szam = str(lista[0]) + str(lista[1]) + str(lista[2])
# ! csak akkor mukodik ha ennyi eleme van a listanak
print(szam)
print(type(szam))
# 4. feladat
magas = ["e", "é", "i", "í", "ü", "ű", "ö", "ü"]
# szoveg = input("Adj mege yg szöveget:")

"""print(len(szoveg))
i = 0
while i > len(szoveg):
    if  in szoveg:"""

# 5. feladat
# szam = int(input("Adj meg egy számot!:"))
szam = int(input("Adj meg egy számot"))
i = 1
szorzat = 1
while i <= szam:
    szorzat *= i
    i += 1
print(szorzat)
osszeg = szorzat + szam
fele = round(osszeg / 2, 0)
# ! nem jo a kerekites, int()
print(str(0) + str(0) + str(fele))

# 2. feladat
szoveg = input("Adj meg egy szöveget nagybetűkkel:")
szo = []
i = 0
nagybetu = 0
szoveg1 = list(szoveg)
while i > len(list(szoveg)):
    print(szoveg1.count(szoveg1.isupper(szoveg1)))
    # ! minek a while ciklus?
    i += 1

# 3.
lista = [1, 3, 5, 6, 2]
i = 0
index = 0
for i in range(len(lista)):
    if i % 2 == 0:
        # ! a lista elemeit kene nezned, nem az i-t
        index += 1
        # ! a for-nal nem kell az indexel cseszekedni
print(index + 1)
print(lista[index])
lista.insert(index + 1, 16)
print(lista)
print(lista.count(1))
