# pagefor: for loops

# def: for loop

# prompt: mi az a for loop?
# prompt: hogyan mukodik a for loop?
# prompt: hogyan lehet for loopot irni pythonban?
# prompt: mire jo a for loop?
# prompt: while vs for loop
# prompt: hogyan lehet breakelni a for loopot?
# prompt: hogyan lehet continuezni a for loopot?

# prompt: a for loop egy ciklus, ami egy adott szamu ismetlest hajt vegre
# prompt: a for loop ugy mukodik, hogy vegig megy egy adott lista elemein es vegrehajt egy adott kodot
# prompt: a for loopot a for kulcsszoval lehet irni
# prompt: a for loop jo arra, hogy egy adott kodot tobb elemen is vegrehajtsunk
# prompt: a while loop addig fut, amig egy adott feltetel igaz, mig a for loop addig fut, amig az osszes elemet vegig nem ertuk
# prompt: a for loopbol a break kulcsszoval lehet kilepni
# prompt: a for loopbol a continue kulcsszoval lehet folytatni

# code: for loop
for i in range(5):
    print(i)
# prompt: a range() fuggveny egy adott szamu szamot general, amit a for loop vegig megy
# prompt: 0-tol 5-ig megyunk vegig, de az utolso szamot nem irja ki
for i in range(0, 5):
    print(i)
# prompt: 0-tol 5-ig megyunk vegig, de az utolso szamot nem irja ki
for i in range(0, 5, 1):
    print(i)
# prompt: 0-tol 5-ig megyunk vegig, de az utolso szamot nem irja ki
for i in range(5, 0, -1):
    print(i)
# prompt: 0-tol 5-ig megyunk vegig, de az utolso szamot nem irja ki
for i in range(0, 5, 2):
    print(i)
# prompt: kettesevel megyunk vegig a szamokon

# code: break
for i in range(5):
    if i == 3:
        break
    print(i)
# prompt: a break kulcsszoval lehet kilepni a for loopbol

# code: continue
for i in range(5):
    if i == 3:
        continue
    print(i)
# prompt: a continue kulcsszoval lehet folytatni a for loopot --> a 3-at kihagyja

szamok = [1, 2, 3, 4, 5]
for szam in szamok:
    print(szam)
# prompt: a for loop vegig megy egy adott lista elemein es vegrehajt egy adott kodot
for i in range(len(szamok)):
    print(szamok[i])

# Task 1: irj egy programot, ami kiirja az elso 10 szamot
for i in range(1, 11):
    print(i)

# Task 2: irj egy programot, ami kiirja az elso 10 paros szamot
for i in range(2, 21, 2):
    print(i)

# Task 3: irj egy programot, ami kiirja az elso 10 paros szamot, de a 6-os szamot kihagyja
for i in range(2, 21, 2):
    if i == 6:
        continue
    print(i)

# Task 4: irj egy programot, ami kiirja az elso 10 paratlan szamot, de a 6-os szam utan kilep
for i in range(1, 20, 2):
    if i == 7:
        break
    print(i)

# Task 5 (advanced): kerj be egy szamot a felhasznalotol. ennyiszer kerj be egy szamot tole
# task: es tedd bele egy listaba. vegul irasd ki a lista elemeinek osszeget
szam = int(input("Kerj be egy szamot: "))
szamok = []
for i in range(szam):
    szamok.append(int(input("Kerj be egy szamot: ")))
osszeg = 0
for i in szamok:
    osszeg += i
print(f"A szamok osszege: {osszeg}")

# Task 6 (advanced): rendezd a lista elemeit novekvo sorrendbe a sort() hasznalata nelkul
szamok = [5, 3, 1, 4, 2]
novekvo = []
for i in range(len(szamok)):
    legkisebb = szamok[0]
    for j in szamok:
        if j < legkisebb:
            legkisebb = j
    novekvo.append(legkisebb)
    szamok.remove(legkisebb)
print(novekvo)

# Task 7: kerj be egy szamot a felhasznalotol. irasd ki az osszes osztojat
szam = int(input("Kerj be egy szamot: "))
for i in range(1, szam + 1):
    if szam % i == 0:
        print(i)

# Task 8: kerj be egy szamot a felhasznalotol. irasd ki, hogy a szam prim-e
szam = int(input("Kerj be egy szamot: "))
prim = True
for i in range(2, szam):
    if szam % i == 0:
        prim = False
        break

if prim:
    print("A szam prim")
else:
    print("A szam nem prim")

# Task 9: kerj be egy szamot a felhasznalotol. irasd ki addig a szamig az osszes negyzetszamot
szam = int(input("Kerj be egy szamot: "))
for i in range(1, szam + 1):
    print(i**2)

# Task 10 (advanced): kerj be ket szamot a felhasznalotol. irasd ki a legnagyobb kozos osztojukat
szam1 = int(input("Kerj be egy szamot: "))
szam2 = int(input("Kerj be egy masik szamot: "))
lnko = 1
for i in range(1, min(szam1, szam2) + 1):
    if szam1 % i == 0 and szam2 % i == 0:
        lnko = i
print(f"A ket szam legnagyobb kozos osztoja: {lnko}")

# Task 11: kerd be a felhasznalotol a befekteteset, az erdeklodest, es a futamidot. szamold ki a vegso osszeget
befektetes = int(input("Add meg a befektetest: "))
erdeklodes = int(input("Add meg az erdeklodest: "))
futamido = int(input("Add meg a futamidot: "))
osszeg = befektetes
for i in range(futamido):
    osszeg += osszeg * (erdeklodes / 100)
print(f"A vegso osszeg: {osszeg}")
