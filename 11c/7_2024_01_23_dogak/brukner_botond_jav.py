# 1.
lista = [1, 2, 3]
osszeg = int("".join(map(str, lista)))
print(osszeg)
# ! nincs kiprintelve az tipusa

# 2.
szo = "AlmaKorteEper"
nagybetuk = 0
nagybetuk_lista = []

valtozo = 0
while valtozo < len(szo):
    betu = szo[valtozo]
    nagybetuk += betu.isupper()
    # ! ez igy az igaz/hamis erteket adja a nagybetuk valtozonak

    # ! felesleges: nagybetuk_lista
    # valtozo += 1
    # ! vegtelen ciklus

print("Nagybetűk száma:", nagybetuk)
print("Nagybetűk listája:", nagybetuk_lista)

# 3.
lista_input = [4, 14, 35, 63, 72]
uj_lista = list(filter(lambda x: (x % 2 == 0), lista_input))
# ! jovicc xddddd
print("Páros számok: ", uj_lista)

# 5.
szam = int(input("Adj meg egy szamot: "))
valtozo = 1
eredmeny = 1
while valtozo <= szam:
    eredmeny *= szam
    # ! valtozoval kene szorozni az eredmenyt
    valtozo += 1
print(eredmeny)

szam2 = int(input("Adj meg egy másik számot: "))
összeg = szam + szam2
# ! nem ez volt a feladat

fele = round(összeg / 2, 0)
# ! nem jo a kerekites, int()
print(str(0) + str(0) + str(fele))
# ! ez okos
