# pagefor: modulok

# def: Importálás
# example: import <modulnev> as <aliasnev>

# def: Használat
# example: <aliasnev>.<fuggvenynev>()

# Példa
import math as m

print(m.sqrt(4))  # 2.0


# prompt: rengeteg builtin modul van pythonban, amiket érdemes megtanulni
# prompt: a legtöbb modul dokumentációja elérhető a python.org oldalon
# prompt: a modulokat a `pip` segítségével is telepíthetjük
# prompt: a `pip` egy package manager, amivel könnyen telepíthetünk python csomagokat
# prompt: a `pip`-et a terminálban tudjuk használni
# prompt: az igy leszedett modulokat ugyanugy kell importalni mint a beépítetteket
# prompt: példa: `pip install requests` után `import requests`
# prompt: ezzel mar viszont nem fogunk foglalkozni

# ! nagyon fontos modul: random

# def: A random modul segítségével tudunk véletlenszámokat generálni
# def: A modulban számos függvény található, amiket használhatunk
# def: Ezek kozul nezzuk meg a 3 legfontosabbat

# def: random.randint(a, b)
# def: A függvény egy véletlenszámot generál a [a, b] intervallumban
# def: a és b lehetnek bármilyen egész számok

import random as r

print(r.randint(1, 10))  # 3

# def: random.choice(seq)
# def: A függvény egy véletlenszámot választ ki egy listából
# def: A lista elemei lehetnek bármilyen típusúak

print(r.choice([1, 2, 3, 4, 5]))  # 3


# def: random.shuffle(seq)
# def: A függvény egy listát véletlenszerűen kever meg
# def: A lista elemei lehetnek bármilyen típusúak

l = [1, 2, 3, 4, 5]
print(l)
r.shuffle(l)
print(l)

# raadas

# def: random.randrange(start, stop, step)
# def: A függvény egy véletlenszámot generál a [start, stop) intervallumban
# def: A step a lépésköz, alapértelmezetten 1

print(r.randrange(0, 10, 2))  # 8


# task: hasznaljuk a random modult az eddig megtanultakkal egyutt

# task: irj egy fuggvenyt, ami kiir 10 random szamot egy szamok.txt file-ba 1 es 100 kozott
# task: ezutan irj egy functiont ami megkap egy listanyi szamot es kivalasztja a legnagyobbat (max fuggveny nelkul)

f = open("szamok.txt", "w")
for i in range(10):
    f.write(str(r.randint(1, 100)) + " ")
f.close()


def mymax(list):
    maxval = list[0]
    for i in list:
        if i > maxval:
            maxval = i
    return maxval


f = open("szamok.txt", "r")
l = f.read().split()
for i in range(len(l)):
    l[i] = int(l[i])
print(f"A {l} legnagyobb eleme: {mymax(l)}")
f.close()

# task: ugyanehez a feladathoz irjunk egy fuggvenyt ami megmondja az atlagot


def myavg(l):
    listsum = 0
    for i in l:
        listsum += i
    return round(listsum / len(l), 2)


# prompt: kene egy olyan is ami kap egy listat es az elemeit intte alakitja


def convert_to_int(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l


f = open("szamok.txt", "r")
l = f.read().split()
l = convert_to_int(l)
print(f"A {l} atlaga: {myavg(l)}")


# task: irj egy fuggvenyt ami megszamolja, hogy hanyszor van egy szo egy szovegben es hogy melyik indexeken


def count_word(word, text):
    count = 0
    indexes = []
    for i in range(len(text)):
        szo = text[i].strip(",.!?").lower()
        if szo == word.strip(",.!?").lower():
            count += 1
            indexes.append(i + 1)
    return (count, indexes)


f = open("szoveg.txt", "r", encoding="utf-8")
text = f.read().split()
bekert = input("Melyik szot keresed?\n")
print(
    f"A {bekert} szobol {count_word(bekert, text)[0]} darab van a szovegben, az indexei: {count_word(bekert, text)[1]}"
)


# task: kis txt fileok osszefuzese egy functionnel


def merge_files(files, output_file):
    merged_content = ""
    for file in files:
        f = open(file, "r", encoding="utf-8")
        merged_content += f.read() + "\n"
        f.close()
    f = open(output_file, "w", encoding="utf-8")
    f.write(merged_content)
    f.close()


files = ["f1.txt", "f2.txt", "f3.txt"]
merge_files(files, "merged.txt")


# task: szo gyakorisag szamlalo function

# prompt: uj dolog: dictionary
# def: A dictionary egy olyan adatszerkezet, ami kulcs-ertek parokat tartalmaz
# def: A kulcsoknak egyedinek kell lenniuk
# def: A kulcsok lehetnek barmilyen adattipusok
d = {"a": 1, "b": 2, "c": 3}
print(d["a"])  # 1
d["d"] = 4
{"a": 1, "b": 2, "c": 3, "d": 4}

f = open("szoveg.txt", "r", encoding="utf-8")
text = f.read().split()
f.close()


def word_frequency(text):
    freq = {}
    for word in text:
        word = word.strip(",.!?").lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    # prompt: sort the keys by their values
    freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    f = open("gyakorisag.txt", "w", encoding="utf-8")
    for word in freq:
        f.write(f"{word}: {freq[word]}\n")


word_frequency(text)


# task: irj egy fuggvenyt ami megmondja ket szorol hogy anagrammak-e


def is_anagram(s1, s2):
    s1 = s1.lower().strip()
    s2 = s2.lower().strip()
    if len(s1) != len(s2):
        return False
    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    return True


input1 = input("Első szó: ")
input2 = input("Második szó: ")
if is_anagram(input1, input2):
    print("Anagrammák")
else:
    print("Nem anagrammák")
