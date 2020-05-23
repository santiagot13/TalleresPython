"""
    4. Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a
    cero y cuántas mayores a cero.
"""
try:
    N = 0
    val = 0
    contMayCero = 0
    contMenIgCero = 0

    N = int(input("Digite el número de iteraciones:\n"))

    for i in range(N):
        val = float(input("Digite un valor # %s:\n" %(i+1))) 
        if valor > 0: 
            contMayCero += 1 
        else:
            contMenIgCero += 1 
    
    print("\nTotal mayor a cero: ", contMayCero,"\nTotal menor o igual a cero:",contMenIgCero)
except ValueError:
    print("El valor ingeresado no es un número válido.")
    print("\nTotal mayor a cero: ", contMayCero,"\nTotal menor o igual a cero:",contMenIgCero)