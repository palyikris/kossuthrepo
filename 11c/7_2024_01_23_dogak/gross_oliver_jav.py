szam = int(input("Adjon meg egy számot: "))
print(szam)
masikszam = input(" Adjon meg egy számot:")
masikszam = int(masikszam)
összeg = szam + masikszam
print(összeg)

if 5 == 5:
    print("Ez a szám 5")

if 5 == 6:
    print("Ez a szám 6")

else:
    print("Ez a szám nem 6")

szam1 = int(input("Adjon meg egy számot: "))
szam2 = int(input("Adjon meg egy számot: "))

if szam1 == szam2:
    print(f"A {szam1} egyenlo a {szam2}-vel")
elif szam1 > szam2:
    print(f"A {szam1} nagyobb mint a {szam2}")


# maradekos osztas

szam = 0
while szam <= 10:
    print(szam)
    szam += 1

szamx = int(input("Adjon meg egy számot: "))
seged = 0
while seged <= szamx:
    if seged % 2 == 0:
        print(seged)
    seged += 1

szamv = int(input("Adjon meg egy számot: "))
segedf = 0
osszeg = 0
while segedf <= szamv:
    if segedf % 2 == 1:
        osszeg += segedf
    segedf += 1
print(osszeg)

szamz = int(input("Adjon meg egy számot: "))
segedd = 1
szorzat = 1
while segedd <= szamz:
    szorzat *= segedd
    segedd += 1
print(szorzat)

#################dolgozat 5.

szamz = int(input("Adjon meg egy számot: "))
a = 1
szorzat = 1
while a <= szam:
    szorzat *= 1
    a += 1
print(szorzat)
összeg = szorzat + szam
fele = round(osszeg / 2, 0)
# ! nem jo a kerekites, int()
print(str(0) + str(0) + str(fele))
