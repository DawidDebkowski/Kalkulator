print("Kalkulator do mnożenia kilku czynników")
wynik = 0
o = int(input("Podaj ilość czynników:"))
x = int(input("Podaj czynnik: "))
y = int(input("Podaj czynnik: "))
wynik = x*y
for i in range (o - 2):
    z = int(input("Podaj czynnik: "))
    wynik = wynik * z
print(wynik)

