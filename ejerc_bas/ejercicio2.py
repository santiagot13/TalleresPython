"""
    2. Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un
    ciclo for.
"""
try:
    N = 10
    s = 0

    for i in range(N):
        s += float(input("Digite un valor # %s: \n" %(i+1)))

    print("\nTotal suma: ", s)
except ValueError:
    print("Error.")