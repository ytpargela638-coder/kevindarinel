"""Problema 6 - Ciclos
Diseñe una aplicación que permita ingresar n
números y muestre y sume los números
pares."""
suma=0
N=int(input("Ingresa el total de numeros que vas a sumar: "))
for i in range(1,N+1):
	sumN=int(input(f"Ingrese el {i} numero: "))
	suma+=sumN
print(f"El total es de: {suma}")