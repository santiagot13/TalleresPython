"""
    5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran
    entre 0 y 100. Además muestre la multiplicación de todos estos.
"""
try:
    N = 100
    impar = ""
    par = ""
    mult = 1
    multPar = 1
    multImpar = 1
    #impares = []

    for i in range (N+1):
        mult *= i
        if i % 2 == 0:
            par += str(i)+"\n"
            multPar *= i
        else:
            impar += str(i)+"\n"
            multiImpar *= i
            
    print("\nNúmeros pares:\n", par)
    print("\nNúmeros impares:\n", impar)
    #Se toma el rango desde cero, así que la multiplicación total y de los números pares da como resultado cero
    print("\nTotal multiplicación:\n",mult)
    print("\nTotal multiplicación Pares:\n",multPar)
    print("\nTotal multiplicación Impares:\n{:,}".format(multImpar).replace(',','.'))
except ValueError:
    print("Error.")