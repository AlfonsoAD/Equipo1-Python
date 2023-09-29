# 1 Funciones con n parámetros
# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
# producto total y su suma total.

def Operaciones(*args):
    productoTotal = 1
    sumaTotal = 0

    for num in args:
        productoTotal *= num
        sumaTotal += num;

    return productoTotal,sumaTotal;

resultadoProducto , resultadoSuma = Operaciones(2,3,4,5,6,5,6)

print(f"Producto es  {resultadoProducto}")
print(f"Suma  {resultadoSuma}")
