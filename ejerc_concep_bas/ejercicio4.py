"""
    Convertir Años a segundos
"""
try:
    lustro = 5
    anosSeg = 60*60*24*365

    print("\nCuántos segundos hay en un lustro: {:,}".format((lustro*anosSeg)).replace(',','.'),"Seg")
except ValueError:
    print("Error.")