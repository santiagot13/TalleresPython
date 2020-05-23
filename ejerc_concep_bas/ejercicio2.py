"""
    Calcular dólares a pesos colombianos. Valor del dólar hoy 12-04-2020 = 3.827
"""
try:
    vPeso = 3827
    dol = 0

    dol = float(input("Digite la cantidad de dólares:\n"))

    print("\nEl valor total en pesos colombianos es: ${:,}".format((dol*vPeso)).replace(',','.'))
except ValueError:
    print("El valor ingeresado no es válido.")