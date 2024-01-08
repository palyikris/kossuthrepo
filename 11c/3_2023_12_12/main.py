# task: ismétlés
# prompt: print es fuggvenyek
print("Hello World")
print("")
print("Hello" + " " + "World")
print("")
print("Hello", "World")
print("")
print(
    """
    Hello
    world
    """
)
print("")
print("Hello\nWorld")
print("")

szoveg = "Hello World"
print(szoveg)
print("")
print(szoveg + "\n" + szoveg)
print(szoveg.upper())
print(szoveg.lower())
print(szoveg.capitalize())
print(szoveg.title())
print(szoveg.replace("o", "a"))
print("")

# prompt: input
input("Adj meg egy szoveget: \n")
print(input("Adj meg egy szoveget: \n"))

szoveg = input("Adj meg egy szoveget: \n")
print(szoveg)

szam = int(input("Adj meg egy szamot: \n"))
print(szam)

szam1 = int(input("Adj meg egy szamot: \n"))
szam2 = int(input("Adj meg egy szamot: \n"))
print(szam1 + szam2)
print(szam1 - szam2)
print(szam1 * szam2)
print(szam1 / szam2)


# task: orai anyag
# prompt: fuggvenyek meg es if else

# len() --> hossz --> hany elem van a listaban
print(len("Hello World"))
print(len([1, 2, 3, 4]))
print(len(input("Adj meg egy szoveget: \n")))

# split() --> szetvalasztas --> szetvalasztja a szoveget a megadott karakter menten es listat csinal belole
print("Hello World".split(" "))
print("Hello World".split("o"))
print(input("Adj meg egy szoveget: \n").split(" "))

# join() --> osszefuzes --> osszefuzi a szoveget a megadott karakter menten
print(" ".join(["Hello", "World"]))
print("o".join(["Hello", "World"]))
print("o".join(input("Adj meg egy szoveget: \n").split(" ")))

# count() --> megszamolas --> megszamolja, hogy hanyszor fordul elo egy karakter a szovegben
print("Hello World".count("o"))
print("Hello World".count("l"))
print(input("Adj meg egy szoveget: \n").count(" "))

# find() --> kereses --> megmondja, hogy egy karakter hanyadik helyen van a szovegben eloszor
# ! a szamozas 0-tol kezdodik
# ! ha nem talalja meg a karaktert, akkor -1-et ad vissza
print("Hello World".find("o"))
print("Hello World".find("l"))
print("Hello World".find("a"))
print(input("Adj meg egy szoveget: \n").find(" "))
print(input("Adj meg egy szoveget: \n").find("a"))

# startswith() --> kezdodik-e --> megmondja, hogy egy karakterrel kezdodik-e a szoveg
print("Hello World".startswith("H"))
print("Hello World".startswith("h"))
print(input("Adj meg egy szoveget: \n").startswith("H"))

# endswith() --> vegzodik-e --> megmondja, hogy egy karakterrel vegzodik-e a szoveg
print("Hello World".endswith("d"))
print("Hello World".endswith("D"))
print(input("Adj meg egy szoveget: \n").endswith("d"))

# islower() --> kisbetus-e --> megmondja, hogy a szoveg kisbetus-e
print("Hello World".islower())
print("hello world".islower())
print(input("Adj meg egy szoveget: \n").islower())

# isupper() --> nagybetus-e --> megmondja, hogy a szoveg nagybetus-e
print("Hello World".isupper())
print("HELLO WORLD".isupper())
print(input("Adj meg egy szoveget: \n").isupper())

# type() --> tipus --> megmondja, hogy milyen tipusu a valtozo
print(type("Hello World"))
print(type(5))
print(type(True))
print(type(5.5))
print(type([1, 2, 3, 4]))
print(type(input("Adj meg egy szoveget: \n")))
print(type(int(input("Adj meg egy szamot: \n"))))
print(type(float(input("Adj meg egy szamot: \n"))))

# prompt: printben valtozok
szoveg = "a"
print("Szeretem " + szoveg + " tejet")
print("Szeretem", szoveg, "tejet")
print(f"Szeretem {szoveg} tejet")

szam = 5
print("Szeretem " + str(szam) + " tejet")
print("Szeretem", szam, "tejet")
print(f"Szeretem {szam} tejet")

# prompt: if else
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

if 5 > 6:
    print("A szam nagyobb mint 6")
elif 5 < 6:
    print("A szam kisebb mint 6")

if 5 == 6 and 5 == 5:
    print("A szam 5")

if 5 == 6 or 5 != 5:
    print("A szam 5")

if not 5 == 6:
    print("A szam nem 6")

# prompt: if else gyakorlas
szam1 = int(input("Adj meg egy szamot: \n"))
szam2 = int(input("Adj meg egy szamot: \n"))

if szam1 == szam2:
    print(f"A {szam1} es a {szam2} az egyenlo")
elif szam1 > szam2:
    print(f"A {szam1} nagyobb mint a {szam2}")
else:
    print(f"A {szam2} nagyobb mint a {szam1}")

szoveg1 = input("Adj meg egy szovegte: \n")
szoveg2 = input("Adj meg egy szoveget: \n")

if szoveg1.lower() == szoveg2.lower():
    print(f"A {szoveg1} es a {szoveg2} az egyenlo")
else:
    print(f"A {szoveg1} es a {szoveg2} nem egyenlo")


# prompt: raadas operatorok
# // --> osztas maradek nelkul
szam1 = 5
szam2 = 2
print(szam1 // szam2)
print(type(szam1 // szam2))

# % --> maradek
# a % b --> a osztva b-vel, es a maradeka
print(szam1 % szam2)
print(type(szam1 % szam2))

# ** --> hatvanyozas
# a ** b --> a hatvanyon b
print(szam1**szam2)
print(type(szam1**szam2))

# prompt: meg raadas operatorok
# += --> a = a + b --> a += b
szam1 = 5
szam2 = 2
print(szam1)
szam1 += szam2
print(szam1)

# -= --> a = a - b --> a -= b
szam1 = 5
szam2 = 2
print(szam1)
szam1 -= szam2
print(szam1)

# *= --> a = a * b --> a *= b
szam1 = 5
szam2 = 2
print(szam1)
szam1 *= szam2
print(szam1)

# /= --> a = a / b --> a /= b
szam1 = 5
szam2 = 2
print(szam1)
szam1 /= szam2
print(szam1)
