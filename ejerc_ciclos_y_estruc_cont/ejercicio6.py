"""
    *Cantidad de vocales en una frases
    *Mostrar la frecuencia de aparición de vocales en una frases
"""
import unicodedata

def elimAcentos(fr):
    fr = fr.replace('ñ','#')
    res = ''.join((x for x in unicodedata.normalize('NFD',fr) if unicodedata.category(x) != 'Mn'))
    return res.replace('#','ñ')

try:
    fr = []
    a = ""
    e = ""
    i = ""
    o = ""
    u = ""

    fr = elimAcentos(input("Digite una frase:\n").lower()) 

    a = fr.count("a")
    e = fr.count("e")
    i = fr.count("i")
    o = fr.count("o")
    u = fr.count("u")

    print("\nVeces que aparece la vocal 'a' en la frase:",a)
    print("Veces que aparece la vocal 'e' en la frase:",e)
    print("Veces que aparece la vocal 'i' en la frase:",i)
    print("Veces que aparece la vocal 'o' en la frase:",o)
    print("Veces que aparece la vocal 'u' en la frase:",u)
    print("\nTotal de vocales en la frase:",(a+e+i+o+u))
except ValueError:
    print("\nEl valor ingresado no es válido.")