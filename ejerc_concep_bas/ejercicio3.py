"""
    Convertir grados celcius a fahrenheit
"""
try:
    gradC = 0
    gradF = 0

    gradC = float(input("Ingresar Grados Celcius:\n"))
    gradF = gradC*(9/5) + 32

    print("\nGrados Fahrenheit: ", gradF)
except ValueError:
    print("El valor ingeresado no es válido.")