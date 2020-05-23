"""
    Calcular vueltas de una llanta en 1 km. Todo se pasa a cm
"""
try:
    dm = 50
    rad = dm/2
    long = 1*(1000/1)*(100/1)
    n = 0

    n = long/(2*rad)

    print("\nEl número de vueltas de la llanta es: {:,}".format(n).replace(',','.'))
except ValueError:
    print("Error.")