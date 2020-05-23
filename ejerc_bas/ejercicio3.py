"""
    3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo
    número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una
    estatura registrada.
"""
try:
    est = -1
    sumEst = 0
    contEst = 0

    while est:
        est = float(input("Digite su estatura:\n")) 
        sumEst += est
        contEst += 1
        #Como NO se especifica en qué momento de debe mostrar el promedio, lo muestro en cada iteración
        print("\nEstatura promedio: ", sumEst/contEst,"\n")
except ValueError:
    print("El número ingresado NO es válido.")
    print("\nEstatura promedio: ", sumEst/contEst)
