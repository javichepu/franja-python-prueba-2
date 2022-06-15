#Escribir un programa que contenga una función que reciba una lista de palabras y devuelva la más larga.
# Imprimir por pantalla la palabra resultante.
def encontrar_palabra_mas_larga(palabras):
    palabra_longitud = []

    for p in palabras:
        palabra_longitud.append((len(p), p))
    
    palabra_longitud.sort()

    return palabra_longitud[-1][1]


palabras = ['clarinete', 'violin', 'trompeta', 'tuba','violoncello']

print(encontrar_palabra_mas_larga(palabras))