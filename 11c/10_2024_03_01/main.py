# pagefor: def es fajlokkal dolgozas

# def
# prompt: arra van, hogy a sajat functionjeinket irjuk meg
# prompt: a functionoknak lehetnek argumentumai
# prompt: a functionoknak lehetnek visszateresi ertekei
# prompt: a functionoknak lehetnek default argumentumai


# task: irj egy functiont, ami egy adott szamot megduplaz
def double(num):
    return num * 2


# def, function nev(argumentumok):
# prompt: a return szoval adjuk meg, hogy mit adjon vissza a function
# prompt: a return utan nem hajtodik vegre a function tobbi resze
# prompt: a return nelkul a function None erteket ad vissza

print(double(5))  # 10
# prompt: a function meghivasa utan a function visszateresi erteket kapjuk meg
# double()
# prompt: ha a function hivaskor nem adunk meg argumentumot, akkor hibat kapunk
# prompt: ha tobbet adunk meg, mint amennyit a function var, akkor is hibat kapunk


# task: irj egy functiont, ami egy adott szamot megduplaz ha paros, es eloszt 2-vel ha paratlan
def doubleBetter(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num // 2


# prompt: if valtozonevvel lehet megnezni, hogy a valtozonak van-e erteke

print(doubleBetter(5))  # 2
print(doubleBetter(10))  # 20


# task: irj egy functiont, ami kap egy listat, es visszaadja a listaban levo szamok osszeget
# task: ha van 10-es szam a listaban, akkor a function ne adja hozza az osszeghez
def sumList(lst):
    szum = 0
    for num in lst:
        if num == 10:
            continue
        szum += num
    return szum


# prompt: ha ciklusban van continue, akkor az adott iteracio semmit nem csinal, de a ciklus tovabb megy
print(sumList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 45


# task: ugyanez a feladat csak ha 10-est talal a listaban, hagyja abba a szamok osszeadasat
def sumList(lst):
    szum = 0
    for num in lst:
        if num == 10:
            break
        szum += num
    return szum


# prompt: ha ciklusban van break, akkor az adott ciklus leall
print(sumList([1, 2, 3, 4, 5, 6, 10, 7, 8, 9]))  # 21


# task: ird meg a __main__ functiont, ami kiirja a programunkat
def __main__():
    print("Ez a programunk")


if __name__ == "__main__":
    __main__()
# prompt: a __main__ function azert van, hogy a programunkat egybol lefuttassuk
# prompt: a __main__ function a programunk indulaskor lefut
# prompt: kaphat argumentumokat, de nem adhat visszateresi erteket

# ------------------------------------------------------------

# def: fajlokkal dolgozas
# prompt: open() function segitsegevel tudunk fajlokat megnyitni
# prompt: a fajl megnyitasa utan a fajl objektumot kapjuk vissza
# prompt: a fajl objektumon lehet olvasni es irni
# prompt: a fajl objektumot le kell zarni, miutan vegeztunk vele

# iras
# prompt: ha a fajl nem letezik, akkor letrejon
# prompt: ha a fajl letezik, akkor felulirja a tartalmat
# prompt: w-vel jeloljuk ha irni akarunk
f = open("kutya.txt", "w")
f.write("Ez egy kutya")
# prompt: a write() function segitsegevel tudunk irni a fajlba
f.close()

f = open("kutya.txt", "w")
print("Ez meg egy kutya", file=f)
# prompt: a print() function segitsegevel tudunk irni a fajlba
f.close()

f = open("kutya.txt", "w")
for i in range(10):
    print("Ez egy kutya", file=f)
f.close()

# prompt: ugy is lehet fajlba irni, hogy nem toroljuk a regi tartalmat
f = open("kutya.txt", "a")
f.write("Ez meg egy kutya")
f.close()

# olvasas
# prompt: ha a fajl nem letezik, akkor hibat kapunk
# prompt: ha a fajl letezik, akkor olvashatjuk
# prompt: r-vel jeloljuk ha olvasni akarunk
f = open("kutya.txt", "r")
print(f.read())
f.close()

# prompt: a read() function segitsegevel tudunk olvasni a fajlbol
# prompt: nem csak az egesz fajlt olvashatjuk, hanem egy adott hosszusagu reszt is
f = open("kutya.txt", "r")
print(f.read(5))
f.close()

# prompt: seek() function segitsegevel tudunk ujraolvasni a fajlt
f = open("kutya.txt", "r")
print(f.read(5))
f.seek(0)
print(f.read(5))
f.close()

# prompt: readline() function segitsegevel tudunk soronkent olvasni a fajlbol
f = open("kutya.txt", "r")
print(f.readline())
f.close()

# prompt: readlines() function segitsegevel tudunk listat kapni a fajl soraitol
f = open("kutya.txt", "r")
print(f.readlines())
f.close()


# task: irj egy functiont, ami egy adott szoveget ir ki egy fajlba
def writeToFile(text, filename):
    f = open(filename, "w")
    f.write(text)
    f.close()


writeToFile("anyad", "anyad.txt")


# task: irj egy functiont, ami beolvassa es feldolgozza az emberek adatait egy fajlbol
def readFromFile(filename):
    f = open(filename, "r")
    f.readline()
    # prompt: az elso sor haszontaalan, mert az emberek adatai csak a masodik sortol kezdodnek
    lines = f.readlines()
    print(lines)
    processedLines = []
    for line in lines:
        line = line.strip().split(", ")
        # prompt: a strip() function segitsegevel tudunk megszabadulni a sorok vegen levo ures helyektol
        # prompt: a split() function segitsegevel tudunk listat kapni a sorok elemeirol
        processedLine = []
        processedLine.append(line[0])
        processedLine.append(int(line[1]))
        processedLine.append(line[2])
        processedLines.append(processedLine)
    return processedLines


# task: irj egy functiont, ami megmondja nev alapjan, hogy hany eves egy ember es mit csinal
def getInfo(name):
    people = readFromFile("emberek.txt")
    for person in people:
        if person[0] == name:
            return [person[1], person[2]]
    return "Nincs ilyen ember"


ember = getInfo("Alice")
print(f"Alice {ember[0]} eves, es {ember[1]} a munkaja")


# task: irj egy functiont, ami csinal egy todo listat egy fajlbol
# task: ha a function stringet kap, akkor irja ki a fajlba
# task: ha a function intet kap, akkor torolja a fajlbol a megadott sorszamu sort
def todoList(action):
    if type(action) == str:
        writeToDo(action)
    elif type(action) == int:
        deleteToDo(action)
    else:
        print("Hibas bemenet!")


def writeToDo(text):
    print(text, file=open("todo.txt", "a"))


def deleteToDo(index):
    f = open("todo.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("todo.txt", "w")
    for i in range(len(lines)):
        if i != index:
            print(lines[i], file=f)
    f.close()


todoList("Ez egy todo")
todoList("Ez meg egy todo")
todoList("Ez egy harmadik todo")
todoList(0)


# task: irj egy functiont, ami segit foglalni ulohelyeket egy fajlban
def numberOfFreeSeats():
    f = open("szekek.txt", "r")
    line = f.readline()
    f.close()
    free = 0
    for seat in line:
        if seat.strip() == "O":
            free += 1
    return free


print(numberOfFreeSeats())


# task: irj egy functiont ami lefoglal ulohelyet
# task: a function intet kapjon, es az int sorszamanak megfelelo helyet foglalja le
def reserveSeat(seat):
    f = open("szekek.txt", "r")
    line = f.readline()
    f.close()
    f = open("szekek.txt", "w")
    newLine = ""
    for i in range(len(line)):
        if i == seat - 1:
            if line[i] == "O":
                newLine += "X"
                print("Sikerult lefoglalni")
            else:
                print("Ez a hely mar foglalt")
                newLine += line[i]
        else:
            newLine += line[i]
    print(newLine, file=f)
    f.close()


reserveSeat(3)
