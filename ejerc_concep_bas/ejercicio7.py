"""
    Longitud de la sombra de un edificio
"""
import math
 
try:
    alt = 20
    ang = math.radians(22)
    longS = 0

    longS = alt/math.tan(ang)
    
    print("\nLa longitud de la sombra que proyecta el edificio es: {:,}".format(longS).replace(',','.'),"m")
except ValueError:
    print("\nError.")