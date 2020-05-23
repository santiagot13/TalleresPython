"""
    Dado un diccionario, el cual almacena las calificaciones de un
    alumno, siendo las llaves los nombres de las materia y los valores
    las calificación, mostrar en pantalla el promedio del alumno.

    Ejemplo: calificaciones = {calculo:10, dibujo:5}

    * A partir del diccionario del ejercicio anterior, mostrar en pantalla
    la materia con mejor promedio.
"""

try:
    cal = {"Calculo":10, "Dibujo":5}
    prom = 0
    mProm = 0

    prom = (cal["Calculo"] + cal ["Dibujo"])/len(cal)
    mProm = max(cal, key=cal.get)
    print("\nPromedio alumno: ",prom)
    print("\nLa materia con mejor promedio es: ", mProm)

except ValueError:
    print("\nError.")