
# variables
n: str | int = 0
matriz = []
result = []

def capturarValorN():
    valor = int(input("Ingresa un valor para el ancho y alto de la matriz (n mayor igual que 2 y menor igual que 10): "))
    if valor < 2 or valor > 10:
        return "**** Valor ingresado incorrecto ****"
    else:
        return valor
    
def llenarMatriz():
    matrizAux = []
    if isinstance(n,str):
        return "ERROR: No se puede crear la matriz"
    else:
        for j in range(n):
            matrizAux.append([j + 1 * i + 1 for i in range(n)])
        return matrizAux
    
def convertirMatrizYOrdenar():
    matrizAux = []
    for l in matriz:
        for e in l:
            matrizAux.append(e)
    return sorted(matrizAux)
        
def llenarMatrizCaracol():
    matrizAux = [[0 for _ in range(n)] for _ in range(n)]
    direccion = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    direccion_actual = 0  
    fila, columna = 0, 0  

    for elemento in result:
        matrizAux[fila][columna] = elemento 
        print(fila,columna)

        siguiente_fila = fila + direccion[direccion_actual][0]
        siguiente_columna = columna + direccion[direccion_actual][1]

        if (
            0 <= siguiente_fila < n
            and 0 <= siguiente_columna < n
            and matrizAux[siguiente_fila][siguiente_columna] == 0
        ):
            fila, columna = siguiente_fila, siguiente_columna
        else:
            direccion_actual = (direccion_actual + 1) % 4
            fila += direccion[direccion_actual][0]
            columna += direccion[direccion_actual][1]

    return matriz

# capturar valor    
n = capturarValorN()
print(n)
# llenar la matriz
matriz = llenarMatriz()
print(matriz)
#convertirMatrizALista
result = convertirMatrizYOrdenar()
print(result)
#función llenar matriz en caracol
matrizResultante = llenarMatrizCaracol()
print(matrizResultante)



