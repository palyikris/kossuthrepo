# Task: Órai munka
# def: Írj egy programot, ami eldönti, hogy két bekért szám közül
# def: melyik a nagyobb, kisebb, vagy egyenlő

szam1 = int(input("Adj egy számot: \n"))
szam2 = int(input("Adj egy számot: \n"))

if szam1 > szam2:
    print(f"A {szam1} nagyobb mint a {szam2}")
elif szam1 < szam2:
    print(f"A {szam2} nagyobb mint a {szam1}")
else:
    print(f"A {szam1} és a {szam2} egyenlő")


# prompt: ober benedek megoldasa

szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot: "))

if szam1 > szam2:
    print("A ", szam1, " nagyobb mint a ", szam2)
elif szam2 > szam1:
    print("A ", szam2, " nagyobb mint a ", szam1)
else:
    print("A két szám egyenlő")
