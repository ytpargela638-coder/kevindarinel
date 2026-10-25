# Problema 19: Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10% anual durante 6 años.
# ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años?[cite: 18]

salario = 1500

# Iteramos durante los 6 años
for anio in range(1, 7):
    # Calculamos el incremento del 10% y se lo sumamos al salario actual
    salario = salario + (salario * 0.10)
    # Mostramos el salario obtenido en cada año
    print("Salario en el año", anio, ":", salario)

print("Salario final tras 6 años:", salario)