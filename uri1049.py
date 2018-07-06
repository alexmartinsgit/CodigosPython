#uri1049.py - Animal
#05.07.18 - Alex Martins

op1 = input()
op2 = input()
op3 = input()

if op3 == "carnivoro":
	print("aguia")
elif op3 == "herbivoro" and op2 == "mamifero":
	print("vaca")
elif op3 == "herbivoro" and op2 == "inseto":
	print("lagarta")
elif op3 == "hematofago" and op2 == "inseto":
	print("pulga")
elif op3 == "hematofago" and op2 == "anelideo":
	print("sanguessuga")
elif op3 == "onivoro" and op2 == "ave":
	print("pomba")
elif op3 == "onivoro" and op2 == "mamifero":
	print("homem")
elif op3 == "onivoro" and op2 == "anelideo":
	print("minhoca")