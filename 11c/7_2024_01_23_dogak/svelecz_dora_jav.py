#5
szam=int(input("Kérek egy számot:"))
i = 1
szorzat = 1
while i <= szam:
    szorzat *= i
    i += 1
print(szorzat)
osszeg= szorzat + szam
fele= round( osszeg / 2,0)
# ! nem jo a kerekites, int()
print(str(0)+str(0)+str(fele))

#1
lista=[1,2,3]
print(str(lista).replace(",","").replace(",","").replace(",",""),"ez egy egész szám")

#3
def elso_paros_index (szamok)
    index = 0
    while index < len (szamok)
        if szamok[index] % 2 == 0:
            return index
        index += 1
        return -1
    return count
# ! nem tanultuk meg a def-et
lista = [1,2,3]
elso_paros = elso_paros_index(lista)
print("Az első páros szám indexe:", elso_paros)
lista.insert(1,16)
# ! az insert jo vonal, csak az elso paros index utan kellett
#4
szöveg=print(input("Kérek egy szöveget:"))
while (szöveg ! =e,é,i,í,ü,ű,ö,ő)
    szam(int(input"Milyen hangrendű a szó:"))
    if (szöveg > e,é,i,í,ü,ű,ö,ő)
        print ("a bekért szöveg magas hangrendű:")
    else:
        print("a bekért szöveg mély hangrendű")
# ! wtf