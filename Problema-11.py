"""Problema 11 - Ciclos
Revisa en un ciclo el peso registrado de 10
maletas y cuenta cuántas superan el límite de
23 kg."""
p_d=[20, 22, 14, 36, 15, 8, 18, 16,25,40]

contador=0

for i in range(10):

	if (p_d[i]>23):
		contador+=1
		
print(f"El total de maletas mayor de 23KG es:{contador}")