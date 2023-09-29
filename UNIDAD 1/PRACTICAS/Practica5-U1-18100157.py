'''
#5 Manejo de información 
Escribir una función que reciba n parámetros de llave valor e imprima la información en formato 
“{valor}”: “{llave}” 
'''

def mostrarDiccionario(**Animales):
    for clave, valor in Animales.items():
        print(f'{valor}: {clave}')
    return 'hola'

mostrarDiccionario(perro='gua', gato='miau', vaca='mu', obeja='bee')