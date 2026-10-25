"""Problema 12 - Ciclos
Realizar un algoritmo que pida N números (se
pedirá por teclado la cantidad de números a
introducir). El programa debe informar de
cuantos números introducidos son mayores
que 0, menores que 0 e iguales a 0."""
Nmay=0
Nmen=0
N=int(input("Ingresa el total de numeros a ingresar: "))
for i in range(1,N+1):
	Num=int(input("Ingresa el {i}: "))
	if(Num>0):
		Nmay+=1
	else:
		Nmen+=1
print(f"El total de numeros mayores de 0 es de {Nmay} ")
print(f"El total de numeros menores o iguales de 0 es de {Nmen} ")