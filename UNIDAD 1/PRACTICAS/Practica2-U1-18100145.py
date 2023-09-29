# 2. Manejo y manipulación de elementos de una lista
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 2, y muestre por pantalla la lista resultante.


abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
abecedarioNuevo = [abecedario[i] for i in range(len(abecedario)) if (i % 2 != 0)]
print(abecedarioNuevo)


