#uri1018.py - Cédulas
#05.07.18 - Alex Martins

valor = int(input())
a = valor

n100, a = a // 100, a % 100
n50, a = a // 50, a % 50
n20, a = a // 20, a % 20
n10, a = a // 10, a % 10
n5, a = a // 5, a % 5
n2, a = a // 2, a % 2
n1, a = a // 1, a % 1

print(valor)
print("%d nota(s) de R$ 100,00" % n100)
print("%d nota(s) de R$ 50,00"  % n50)
print("%d nota(s) de R$ 20,00"  % n20)
print("%d nota(s) de R$ 10,00"  % n10)
print("%d nota(s) de R$ 5,00"   % n5)
print("%d nota(s) de R$ 2,00"   % n2)
print("%d nota(s) de R$ 1,00"   % n1)