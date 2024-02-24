bekert_szam= int(input("Kerem, adjon meg egy szamot: "))
faktorialis = 1
for i in range( 1, bekert_szam+1):
    faktorialis *=i
    #! a for nem er
osszeg= bekert_szam+ faktorialis
eredmeny= int(osszeg/2)
# ! szeep
eredmeny_str= "00" +
str(eredmeny)
# ! egy sorba mukodott volna
print("Az eredmeny:",
eredmeny_str)
