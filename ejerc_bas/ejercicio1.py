"""
    1. Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. Si algún
    alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18
    años. EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo.
"""
try:
    contA = 0
    edad = 0
    sumarE = 0
    cont = "si"

    while cont == "si":
        edad = int(input("Digite la edad del alumno:\n"))
        if edad > 18: 
            break   
        sumarE += edad
        contA += 1
        cont = input("¿Desea ingresar más edades de alumnos? si/no:\n").lower()

    print("\nEdad promedio: ", sumarE/contA)
except ValueError:
    print("La edad ingresada No es válida.")