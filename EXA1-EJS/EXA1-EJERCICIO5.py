def capturar_cadenas():
    x = 0
    cadenas = []
    while True:
        cadena = input(f"Cadena {x + 1} (o 'e' para cancelar): ")
        if cadena.lower() == 'e':
            break
        cadenas.append(cadena)
        x += 1
    return cadenas

def obtener_palabras_y_numeros(cadenas):
    palabras = []
    numeros = []
    for cadena in cadenas:
        palabras.extend([palabra for palabra in cadena.split() 
                        if not palabra.isdigit()])
        numeros.extend([palabra for palabra in cadena.split() 
                        if palabra.isdigit()])
        
        
    return palabras, numeros

cadenas = capturar_cadenas()
palabras, numeros = obtener_palabras_y_numeros(cadenas)

palabras.sort()
numorden = sorted(numeros)

resultado = "Salida --> " + ' '.join(palabras) + '  ' + ' '.join(numorden) + ' '

print(resultado)



