#elso feladat
lista = [8,3,9]
szam_str = ''.join(map(str, lista))
szam = int(szam_str)
print(szam)
# ! tipus nincs kiirva

#masodik feladat
szo = input("Írj be egy szót: ")
nagybetukszama = sum(1 for karakter in szo if karakter.isupper())
# ! jovicc xd
print(nagybetukszama)

#harmadik feladat
lista1 = [1,5,2,4,6,8,11]
while szam in lista:
    if szam % 2 == 0:
# ! nem jo a loop de jo feltetel


#negyedik feladat



#otodik feladat
szam = int(input("Adj meg egy számot: "))
i = 1
szorzat = 1
while i <= szam:
    szorzat +=1
    # ! szorozni kene kene es az i-vel
    i += 1
print(szorzat)
osszeg = szorzat + szam
fele = round(osszeg / 2,0)
# ! nem jo a kerekites, int()
print(str(0)+str(0)+str(fele))
