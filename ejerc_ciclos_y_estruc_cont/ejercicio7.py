"""
    *Eliminar vocales de una frase
"""
import unicodedata

def eliminar_acentos(fr):
    fr = fr.replace('ñ','#')
    res = ''.join((x for x in unicodedata.normalize('NFD',fr) if unicodedata.category(x) != 'Mn'))
    return res.replace('#','ñ')

try:
    frOri = ""
    fr = ""

    frOri = eliminar_acentos(input("Digite la frase:\n").lower())
    fr = frOri.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

    print("\nLa frase sin vocales:",fr)
except ValueError:
    print("\nEl valor ingresado NO es válido.")