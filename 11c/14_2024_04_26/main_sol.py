# Task 1: Készíts egy programot, ami megfordítja egy adott szám számjegyeit.
szam = int(input("Adj meg egy számot: "))
# szam = str(szam)[::-1]
uj_szam = ""
for i in str(szam):
    uj_szam = i + uj_szam
print(f"A {szam} fordítva: {uj_szam}")


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


# Task 11: Írj egy programot, ami meghatározza egy adott szám pozitív vagy negatív.
szam = int(input("Adj meg egy számot: "))
if szam > 0:
    print(f"A {szam} szám pozitív.")
elif szam < 0:
    print(f"A {szam} szám negatív.")
else:
    print("A szám nulla.")

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
