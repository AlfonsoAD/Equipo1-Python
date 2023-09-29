# 7 Formateo y conversiones
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
# del día de hoy en el formato seleccionado.

from datetime import date

# diccionarios
formatos = {
    1:"YYYY/MM/DD",
    2:"MM/DD/YYYY"
}

sintaxis_format = {
    "YYYY/MM/DD":"%Y/%b/%d",
    "MM/DD/YYYY":"%b/%d/%Y",
}

def mostrar_menu():
    print("**** Menú ****")
    print("Selecciona el formato de la fecha ingresando el número de opción:")
    print("1 - YYYY/MM/DD")
    print("2 - M/DD/YYYY")

def capturar_opcion() -> int:
    opcion_elegida = input("Opción elegida: ")
    return int(opcion_elegida)

def formatear_fecha(op):
    fecha = date.today()
    print(fecha)
    formato = formatos[op]
    fecha_formateada = fecha.strftime(sintaxis_format[formato])
    print(fecha_formateada)
    

def main():
    mostrar_menu()
    opcion = capturar_opcion()
    if opcion > 0 and opcion <= 2:
        formatear_fecha(opcion)
    else: print("ERROR: Opción seleccionada inexsistente.")

main()