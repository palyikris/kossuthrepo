# 5.feladat
# szam=int(input("Adj meg egy számot!:"))
szam = int(input("Adj meg egy számot:"))
i = 1
szorzat = 1
while i <= szam:
    szorzat *= 1
    # ! i-vel kell szorozni
    i *= 1
    # ! nem szorozni, hanem összeadni kell
print(szorzat)
osszeg = szorzat + szam
fele = round(osszeg / 2, 0)
# ! nem jo a kerekites, int()
print(str(0) + str(0) + str(fele))


# 1
lista = [1, 2, 3]
print(str(lista).replace(",", "").replace(",", "").replace(",", ""), "ez a szam nagy")
