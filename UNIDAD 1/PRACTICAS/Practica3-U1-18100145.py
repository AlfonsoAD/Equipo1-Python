#3 Entrada de datos y manipulación. 
# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de 
# manera inversa letra por letra intercalando una letra minuscula a una mayuscula ejemplo Luis : L u I s

nombre = input('Ingresa tu Nombre Completo: ')

sinEspacios = nombre.split()
sinEspacios.reverse()
cadena = ''

for i in range(len(sinEspacios)):
    cont = 0
    for j in reversed(sinEspacios[i]):
        if cont % 2 == 0:
            cadena += j.upper()
        else:
            cadena += j.lower()
        cont += 1
    cadena += ' '

print(cadena)


