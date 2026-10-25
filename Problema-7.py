"""Problema 7 - Ciclos
Un sensor en la puerta de una discoteca
registra la edad de 8 personas que intentan
entrar. Usa un contador para determinar
cuántas personas son menores de edad
(menores a 18 años)."""
mayEdad=0
menEdad=0
for i in range(1,9):
	edad=int(input(f"Ingresa la edad de persona {i}: "))
	if(edad>=18):
		mayEdad+=1
	else:
		menEdad+=1
print(f"Personas mayor de edad {mayEdad}")
print(f"Personas menores de edad {menEdad}")

