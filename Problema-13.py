# Problema 13: Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada
# mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes[cite: 13].

ahorro = 0

# Se hace esto por los 12 meses que tiene el año
for mes in range(1, 13):
    deposito = float(input("Ingresa lo ahorrado en el mes: "))
    # Sumamos el depósito mensual al total acumulado
    ahorro = ahorro + deposito
    # Mostramos el acumulado mes a mes
    print("Ahorro hasta el mes", mes, ":", ahorro)

print("Ahorro total del año:", ahorro)