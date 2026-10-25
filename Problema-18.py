# Problema 18: Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días)
# y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

pago_hora = float(input("¿Cuánto pagan por hora?: "))
total_horas = 0

# Recorremos los 6 días de la semana laboral
for dia in range(1, 7):
    horas = float(input("Horas trabajadas hoy: "))
    # Sumamos las horas de cada día
    total_horas = total_horas + horas

# Calculamos el sueldo multiplicando las horas totales por el pago por hora
sueldo = total_horas * pago_hora

print("Total de horas en la semana:", total_horas)
print("Sueldo a cobrar:", sueldo)