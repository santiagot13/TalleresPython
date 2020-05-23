"""
    *Crear una lista la cual almacene 10 números positivos ingresados
    por el usuario, mostrar en pantalla: la suma de todos los
    números, el promedio, el número mayor y el número menor.
"""

try:
    num = []
    N = 10
    s = 0
    prom = 0
    nMay = 0
    nMen = 0

    for i in range(N):
        num.append(float(input("Digite un valor # %s:\n" %(i+1))))
        s += num[i] 
    
    prom = s/len(num)
    nMay = max(num)
    nMen = min(num)
   
    print("\nSuma total: ", s)
    print("\nPromedio: ", prom)
    print("\nNúmero mayor: ", nMay)
    print("\nNúmero menor: ", nMe)

except ValueError:
    print("\nEl valor ingresado no es válido.")