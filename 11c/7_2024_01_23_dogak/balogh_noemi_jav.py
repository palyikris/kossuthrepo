lista = [1, 2, 3]
print(
    str(lista).replace(",", "").replace(" ", "".replace("[", "").replace("]", "")),
    " ez egy nagy szám",
)
# ! nem sikerult a replace
# ! nem int tipusu a szam
# ! nincs kiirva a tipus


# 5.feladat
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# ! nem tanultunk def-et


num = int(input("kérek egy számot: "))
print(factorial(num))
print(factorial(num) + num)
print(int((factorial(num) + num) / 2))
print("00", int((factorial(num) + num) / 2))
# ! van space


# 4
szoveg = str(input("kérek egy szót "))
print(" A ", szoveg, "magas hangrendű")
print(" A ", szoveg, "vegyes hangrendű")
print(" A ", szoveg, "mély hangrendű")


# 2
lista = []
print(lista)
# ! szoveg kellett

# 3
lista = [1, 2, 3]
lista.append(int(16))
# ! insertelni kellett
print(lista)
lista.count(1)
# ! ezt ki kellett volna printelni
