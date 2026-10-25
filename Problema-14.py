# Problema 14: Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores 
#o iguales a cero y cuántas mayores a cero

cantidad = int(input("¿Cuántas cantidades ingresarás?: "))

mayores = 0
menores_o_iguales = 0

for i in range(cantidad):
    n = float(input("Ingresa un número: "))
    # Evaluamos si es mayor a 0 y si no se va a que es menor o igual
    if n > 0:
        mayores = mayores + 1
    else:
        menores_o_iguales = menores_o_iguales + 1

print("Mayores a cero:", mayores)
print("Menores o iguales a cero:", menores_o_iguales)