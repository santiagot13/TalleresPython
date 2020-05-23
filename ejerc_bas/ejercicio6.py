"""
    6. Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8,
    13,…).
"""

try:
    N = 0
    aux = 0
    ini = 0 
    sgte = 1
    sFibonacci = "0"

    N = int(input("Digite la cantidad de números que desea en la serie Fibonacci:\n"))

    for i in range (N):
        sFibonacci += ", "+str(sgte) 
        aux = ini + sgte
        ini = sgte
        sgte = aux
        
    print ("\nSerie de Fibonacci: ",sFibonacci)

except ValueError:
    print("El Valor ingresado No es válido.")