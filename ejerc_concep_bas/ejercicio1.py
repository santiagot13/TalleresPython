"""
    Calcular área de triángulo
"""
try:
    b = 0
    alt = 0
    a = 0

    b = float(input("Digite la base del triángulo:\n"))
    alt = float(input("Digite la altura del triángulo:\n"))

    a = (b*alt)/2

    print("\nEl área del triángulo es: ",a)
except ValueError:
    print("El valor ingeresado no es válido.")