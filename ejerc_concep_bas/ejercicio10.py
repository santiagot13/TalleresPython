"""
    Promedio notas del estudiante
"""
import math
 
try:
    mat = 5
    n = 0

    for i in range (mat):
        n += float(input("Digite una nota # %s: \n" %(i+1)))

    print("\nEl promedio de notas del alumno es: ", n/mat)
except ValueError:
    print("\nValores ingresados no válidos.")
    print("\nEl promedio de notas del alumno es: ", n/mat)