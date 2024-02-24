# 1
lista = [1, 2, 3]
szam_str = "".join(map(str, lista))
szam = int(szam_str)
print(szam)
# ! tipus nincs kiprintelve

# 2
"""szo = input("Írj egy szót: ")
nagybetukszama 

print(nagybetukszama)"""

# 3
"""lista1 = [1,5,2,4,6,8,11]
if szam % 2 == 0:
    print("első páros szám: ", szam)
    break
# ! ezt egy while ciklusban kene
lista1.append(16)
# ! insert
print(lista1)
if szam % 2 == 0:
print("páros számok: ", szam)"""

# 5
szam = int(input("Írj számot: "))
i = 1
szorzat = 1
while i <= szam:
    szorzat *= i
    i += 1
p = szorzat + szam
u = p / 2
z = round(u, 0)
#! nem jo a kerekites, int()
print(z)
