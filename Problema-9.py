"""Problema 9 - Ciclos
Revisa la entrada de peso de 10 maletas en
un ciclo y cuenta cuántas superan el límite de
23 kg."""
MayorDe23=0
for i in range(1,11):
	peso=int(input(f"Ingresa el peso de la maleta {i}: "))
	if(peso>23):
		MayorDe23+=1

print(f"Maleta mayor de 23KG: {MayorDe23}")

