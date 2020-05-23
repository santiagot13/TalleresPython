"""
    Calcular segundo que le toma viajar a luz del sol a Marte. 
    Distancia 227.940.000 millones de Kms
    Velocidad luz = 299.792 km/s
"""
try:
    distSolMarte = 227940000
    vLuz = 299792

    print("\nSegundos que demora la luz en llegar a Marte: {:,}".format((distSolMarte/vLuz)).replace(',','.'),"Seg")
except ValueError:
    print("Error.")