num =  int(input("Ingrese la cantidad: "))
suma=0

for i in range(1,num):
	N = int(input(f"Ingrese el {i} numero: "))
	suma+=N 
print(f"La suma total es: {suma}")