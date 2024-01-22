# pagefor: lists and while practice

# todo: while loops practice

# Task 1
# Kérjünk be egy számot, amíg az kisebb mint 10, majd írjuk ki, hogy a szám nagyobb mint 10.
szam = int(input("Adj meg egy számot: "))
while szam < 10:
    print(f"A {szam} kisebb mint 10")
    szam = int(input("Adj meg egy másik számot: "))
print("A szám nagyobb mint 10")

# Task 2
szam = int(input("Adj meg egy számot: "))
seged = 0
while seged < szam:
    szamseged = int(input("Adj meg egy másik számot: "))
    if szamseged > 10:
        print(f"A {szamseged} szepen formazva {szamseged}")
    else:
        temp = str(szamseged)
        formazva = "0" + temp
        print(f"A {szamseged} szepen formazva {formazva}")
    seged += 1

# todo: lists practice

# mi az a lista

# def: egy olyan változó, amely több értéket is tárolhat
# def: barmilyen erteket tarolhatunk benne
# def: barmennyi erteket tarolhatunk benne
# def: indexelheto --> elerheto egyes ertekei sorszam alapjan --> 0-tol kezdodik
# def: list[0] --> elso elem, list[-1] --> utolso elem
# def: modosithato --> megvaltoztathatjuk a tartalmat --> tuple nem az
# def: listat [] zarojelben hozunk letre
# def: lista elemet vesszovel valasztjuk el
# def: listaban lehet lista is --> nested list

lista = [1, 2, 3, 4, 5]
print(lista)
print(type(lista))
print(lista[0])
print(lista[1])
print(lista[-1])
# prompt: list() --> listava alakitja a parameterkent megadott erteket
# prompt: list("abc") --> ['a', 'b', 'c']
print(list("abc"))
# prompt: string = karakterek listaja

# listahoz kapcsolodo muveletek

# prompt: len --> hossz
# prompt: lista.append(ertek) --> hozzaadja a listahoz az erteket
# prompt: lista.extend(lista2) --> hozzaadja a listahoz a lista2 elemeit
# prompt: lista.insert(index, ertek) --> beszurja a listaba az erteket az index helyre
# prompt: lista.remove(ertek) --> eltavolitja a listabol az erteket
# prompt: lista.pop(index) --> eltavolitja a listabol az index helyen levo erteket
# prompt: lista.clear() --> torli a lista osszes elemet
# prompt: lista.index(ertek) --> megadja az ertek indexet
# prompt: lista.count(ertek) --> megadja hany ertek van a listaban
# prompt: lista.sort() --> rendezes

lista = [1, 2, 3, 4, 5]
print(lista)
print(len(lista))
lista.append(6)
print(lista)
lista.extend([7, 8, 9])
print(lista)
lista.insert(0, 0)
print(lista)
lista.remove(0)
print(lista)
lista.pop(0)
print(lista)
lista.clear()
print(lista)
seged = 1
while seged < 6:
    lista.append(seged)
    seged += 1
print(lista)
print(lista.index(3))
print(lista.count(3))
lista = [5, 3, 4, 1, 2]
print(lista)
lista.sort()
print(lista)

# list practice

# Task 1
# Kérjünk be 5 számot, tegyuk be egy listába, majd írjuk ki a lista elemeit.
lista = []
seged = 0
while seged < 5:
    szam = int(input("Adj meg egy számot: "))
    lista.append(szam)
    seged += 1
seged = 0
while seged < len(lista):
    print(lista[seged])
    seged += 1

# Task 2
# Kérjünk be 5 számot, majd írjuk ki a legnagyobbat.
lista = []
seged = 0
while seged < 5:
    szam = int(input("Adj meg egy számot: "))
    lista.append(szam)
    seged += 1
lista.sort()
print(lista[-1])

# Task 3
# Kerjunk be egy szamot amit kitorlunk a listabol, majd irjuk ki a listat.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
szam = int(input("Adj meg egy számot: "))
lista.remove(szam)
print(lista)

# Task 4
# Kerjunk egy szamot es azon a sorszamon toroljuk ki a listabol az elemet, majd irjuk ki azt az elemet
lista = [1, 2, 3, 4, 5]
print(lista)
szam = int(input("Adj meg egy számot: "))
print(lista.pop(szam))
print(lista)
