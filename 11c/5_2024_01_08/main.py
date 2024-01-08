# def: Ismetles


# def: print
print("szoveg")
# ! macskakormok

szam = 0
print(szam)

valtozo = "Az eg kek"
print(valtozo)
print(valtozo, " es a fu zold")
print(f"{valtozo} es a fu zold")
print("Az eg kek" + " es a fu zold")

print("A " + str(szam) + " egy szam")

# def: input
szam = input("Adj meg egy szamot: \n")
print(szam)
szam = int(szam)
print(szam)
masikszam = int(input("Adj meg egy masik szamot: \n"))
print(masikszam)
print(szam + masikszam)

# def: if else
# ! aritmetikai muveletek: +, -, *, /
# ! osszehasonlito muveletek: >, <, ==, >=, <=, !=
# ! logikai muveletek: and, or, not
# and --> mindketto igaz kell legyen
# or --> legalabb az egyik igaz kell legyen
# not --> megforditja az erteket

if 5 == 5:
    print("A szam 5")
if 5 == 6:
    print("A szam 6")
else:
    print("A szam nem 6")


szam1 = int(input("Adj meg egy szamot: \n"))
szam2 = int(input("Adj meg egy szamot: \n"))

if szam1 == szam2:
    print(f"A {szam1} es a {szam2} az egyenlo")
elif szam1 > szam2:
    print(f"A {szam1} nagyobb mint a {szam2}")
else:
    print(f"A {szam2} nagyobb mint a {szam1}")


# ! ismetles vege

# def: plusz egy fontos operator
# prompt: %
# prompt: maradekos osztas
# prompt: 5 % 2 = 1
# prompt: 5 % 3 = 2
# prompt: 5 % 5 = 0

# def: while

szam = 0
while szam < 10:
    print(szam)
    szam += 1
# prompt: while ciklus
# prompt: addig ismetel egy reszt amig egy feltetel teljesul
# prompt: while feltetel:
# prompt:     utasitasok
# prompt:     utasitasok
# prompt:     utasitasok
# prompt:     stb.

# def: while ciklus gyakorlas

# Task 1
# prompt: kerjunk be egy szamot es irjuk ki 0-tol addig a szamig a paros szamokat
szam = int(input("Adj meg egy szamot: \n"))
i = 0
while i <= szam:
    if i % 2 == 0:
        print(i)
    i += 1

# Task 2
# prompt: kerjunk be egy szamot es irjuk ki 0-tol mennyi az addig a szamig a paratlan szamok osszege
szam = int(input("Adj meg egy szamot: \n"))
i = 0
osszeg = 0
while i <= szam:
    if i % 2 == 1:
        osszeg += i
    i += 1

# Task 3
# prompt: kerjunk be egy szamot es irjuk ki hogy mennyi a faktorialisa
szam = int(input("Adj meg egy szamot: \n"))
i = 1
faktorialis = 1
while i <= szam:
    faktorialis *= i
    i += 1

# Task 4
# prompt: kerjunk be egy szamot es egy terjedelmet es addig irjuk ki a szam szorzasait amig el nem erjuk a terjedelmet
szam = int(input("Adj meg egy szamot: \n"))
terjedelem = int(input("Adj meg egy terjedelmet: \n"))
i = 1
while i <= terjedelem:
    eredmeny = szam * i
    print(f"{szam} * {i} = {eredmeny}")
    i += 1
