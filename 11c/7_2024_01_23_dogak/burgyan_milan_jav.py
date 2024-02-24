# első feladat

mylist = [123]
print(str(mylist).replace(",", "").replace("[", "").replace("[", "").replace("]", ""))
# ! nem sikerult a replace
# ! nem jo a tipus es ki sincs irva

# harmdadik feladat

lista = [1, 2, 3]

# ! nincsen szam
while szam < 5:
    if szam % 2 == 0:
        continue
        # ! itt kellett volna befejezni a ciklust es elmenteni a lista egyik elemet
    print(lista)

lista.extend([16])
# ! insert kellett
print(lista)

print(lista.count(1))
# ! ezjo


# negyedik feladat

szamok = []
szamok1 = []
seged = 0
while seged < 5:
    szam = int(input("Kérek egy számot: \n"))
    szamok.append(szam)
    szamok1.append(szam)
    seged += 1
szamok.sort()
legkisebb = szamok[0]
szamok1.remove(legkisebb)
print(szamok1)
# ! wtf
