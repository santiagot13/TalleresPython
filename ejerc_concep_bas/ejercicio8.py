"""
    Edad ingresada por usuarios es la misma True o False
"""
try:
    ed1 = 0
    ed2 = 0

    ed1 = int(input("Digite la edad del primer usuario: \n"))
    ed2 = int(input("Digite la edad del segundo usuario: \n"))

    if ed1 == ed2:
        print("\nLas edades son las mismas: ", True)
    else:
        print("\nLas edades no son las mismas: ", False)
except ValueError:
    print("\nValores ingresados no válidos.")