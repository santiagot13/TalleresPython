"""
    *Dado una lista de frases ingresadas por el usuario, mostrar en
    pantalla todas aquellas que sean palíndromo.
"""
import unicodedata

def elimAentos(frase):
       return ''.join(x for x in unicodedata.normalize('NFKD', frase) if unicodedata.category(x)[0] == 'L').lower()

try:
    palindromos = []
    fOriginal = ""
    N = 0
    aux = ""

    N = int(input("Digite el número de frases que desea ingresar?\n"))

    for i in range(N):
        fOriginal = input("Digite la frase # %s:\n" %(i+1))
        aux = elimAentos(fOriginal)
        if (aux == aux[::-1]): 
            palindromos.append(fOriginal)

    print("\n # de Palíndromos ingresados:")
    for i in range(len(palindromos)): 
            print("- ",palindromos[i])

except ValueError:
    print("\nEl valor ingresado no es válido.")