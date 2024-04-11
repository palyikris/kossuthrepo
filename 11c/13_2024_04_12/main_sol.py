# prompt: Tudnivalók a dogával kapcsolatban:
# - Most könnyebb lesz sokkal, mint az előző dogában.
# - Kapni fogtok egy feladatlapot, amin lesznek gyakorló feladatok.
# - A feladatlapon szereplő feladatokhoz hasonlók lesznek a dogában is
# ! Nem ugyanolyanok ne tanuljátok meg őket!
# - A doga során nem használhattok internetet, jegyzeteket, semmilyen segédeszközt.
# - Cserébe tényleg nagyon basic lesz.abs
# - Javításnál a nem lefutó program 0 pontot ér.
# - 6 feladat lesz, mindegyik 1 jegyet ér. (1-et még el lehet cseszni hogy 5-ös legyen.)
# - Ha egy feladat nem megy, ne ragadjatok rajta sokáig, inkább ugorjatok tovább.
# - Ha egy feladat gátolja a futást, inkább kommentezzétek ki, hogy a többi futni tudjon.
# - A feladatokat a megadott sorrendben szerepeljenek a fájlban, mert úgy fogom írni a teszteket.
# - A neveteket és az osztályotokat a fájl elején kommentként megadva.
# - A fajl neve a sajat nevetek legyen, kisbetukkel, elvalasztva alahuzassal. pl.: palyi_kristof.py


# Task 1: írjunk egy függvényt, ami kiír 10 random számot egy szamok.txt file-ba 1 és 100 között
import random as r


def random_numbers():
    with open("szamok.txt", "w") as f:
        for _ in range(10):
            f.write(str(r.randint(1, 101)) + "\n")


# Task 2: ezután írj egy függvényt, ami megkap egy listányi számot és kiválasztja a legnagyobbat (max függvény nélkül)
def max_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# Task 3: Írj egy függvényt, ami kap egy szót és egy szöveget, és visszaadja, hogy a szó hányszor és hol szerepel a szövegben
def count_word_in_text(word, text):
    text = text.split()
    count = 0
    indexes = []
    for i, t in enumerate(text):
        if t == word:
            count += 1
            indexes.append(i)
    return count, indexes


# Task 4: Írj egy függvényt, ami kap egy számot és visszaadja a faktoriálisát
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


# Task 5: Írj egy függvényt, ami kap egy számot és visszaadja a szám számjegyeinek összegét
def sum_of_digits(num):
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    return sum_digits


# Task 6: Írj egy függvényt, ami kap egy számot és visszaadja, hogy prím-e
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Task 7: Írj egy programot, ami kiírja az összes páros számot 1-től 100-ig.
for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# Task 8: Írj egy programot, ami meghatározza egy adott szám legnagyobb közös osztóját.
szam = int(input("Adj meg egy számot: "))
oszto = int(input("Adj meg egy másik számot: "))
while oszto != 0:
    szam, oszto = oszto, szam % oszto
print(f"A két szám legnagyobb közös osztója: {szam}")


# Task 9: Készíts egy programot, ami kiírja az összes prímszámot 1 és 100 között.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(1, 101):
    if is_prime(i):
        print(i)


# Task 10: Készíts egy programot, ami kitalál egy véletlenszerű számot 1 és 100 között, és lehetővé teszi a felhasználónak, hogy megpróbálja kitalálni.
randomszam = r.randint(1, 101)
tipp = int(input("Tippelj egy számra 1 és 100 között: "))
while tipp != randomszam:
    if tipp < randomszam:
        print("Nagyobbra gondoltam.")
    else:
        print("Kisebbre gondoltam.")
    tipp = int(input("Tippelj újra: "))
print("Gratulálok, eltaláltad!")

# Task 11: Írj egy programot, ami meghatározza egy adott szám pozitív vagy negatív.
szam = int(input("Adj meg egy számot: "))
if szam > 0:
    print(f"A {szam} szám pozitív.")

# Task 12: Készíts egy programot, ami meghatározza egy adott szám abszolút értékét (abs függvény használata nélkül).
szam = int(input("Adj meg egy számot: "))
og = szam
if szam < 0:
    szam *= -1
print(f"A {og} abszolút értéke: {szam}")

# Task 13: Készíts egy programot, ami meghatározza két szám közül melyik a nagyobb.
szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy másik számot: "))
if szam1 > szam2:
    print(f"A nagyobb szám: {szam1}")
else:
    print(f"A nagyobb szám: {szam2}")


# Task 14: Írj egy programot, ami meghatározza egy adott szám páros vagy páratlan.
szam = int(input("Adj meg egy számot: "))
if szam % 2 == 0:
    print(f"A {szam} páros.")
else:
    print(f"A {szam} páratlan.")

# Task 15: Készíts egy programot, ami megfordítja egy adott szám számjegyeit.
szam = int(input("Adj meg egy számot: "))
# szam = str(szam)[::-1]
uj_szam = ""
for i in str(szam):
    uj_szam = i + uj_szam
print(f"A {szam} fordítva: {uj_szam}")


# Task 16: Készíts egy programot, ami kiszámolja egy adott szám pozitív osztóinak számát.
szam = r.randint(1, 101)
osztok = 0
for i in range(1, szam + 1):
    if szam % i == 0:
        osztok += 1

# Task 17: Írj egy programot, ami meghatározza egy adott szám számjegyeinek számát.
szam = int(input("Adj meg egy számot: "))
print(f"A {szam} számjegyeinek száma: {len(str(szam))}")

# Task 18: Írj egy programot, ami meghatározza egy adott szám legkisebb és legnagyobb számjegyét.
szam = r.randint(1, 101)
max_digit = 0
min_digit = 9
for i in str(szam):
    i = int(i)
    if i > max_digit:
        max_digit = i
    if i < min_digit:
        min_digit = i

# Task 19: Készíts egy programot, ami kiírja az összes négyzetszámot 1 és 100 között.
for i in range(1, 101):
    if i**0.5 == int(i**0.5):
        print(i)

# Task 20: Készíts egy programot, ami meghatározza egy adott szám osztható-e 3-mal vagy 5-tel.
szam = int(input("Adj meg egy számot: "))
if szam % 3 == 0 or szam % 5 == 0:
    if szam % 3 == 0 and szam % 5 == 0:
        print(f"A {szam} osztható 3-mal és 5-tel.")
    elif szam % 3 == 0:
        print(f"A {szam} osztható 3-mal.")
    else:
        print(f"A {szam} osztható 5-tel.")
else:
    print(f"A {szam} nem osztható sem 3-mal, sem 5-tel.")

# ! ezek a feladatok előfordulhatnak úgy is, hogy fájlba kell írni olvasni, azt is gyakoroljátok!!
