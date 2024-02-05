lista = [12, 23, 211]
print(lista)
print(type(lista))
# ! a type az jo gondolat


# 5.
szam = int(input("Kérek egy számot: "))
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
