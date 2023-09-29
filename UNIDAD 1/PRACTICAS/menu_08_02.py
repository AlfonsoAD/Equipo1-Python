#8 Resumen y multi-solución
# 8.2.-Realizar un programa que contenga el siguiente menú 1.- Registro
# 2.- Inicio de sesión
# 3.- Salida
# La opción de registro solicitara al usuario registrarse solicitando la información de los atributos la clase
# exceptuando el atributo Rol que por defecto será rol cliente, no se permitirán usuarios con CURP
# repetido en caso de mostrar mensaje de “El usuario ya existe”
# La opción de inicio de sesión permitirá al usuario introducir sus credenciales al ser correctas desplegar
# en pantalla la información del usuario de lo contrario mostrar mensaje de “datos incorrectos“
import sys
import os
from user_08_01 import user

miUsuario = user()
name_props = ["usuario", "contraseña", "nombre", "curp", "ciudad"]
lista_usuarios = []

def registrar_usuario():
    os.system("cls")
    print("**** Registro ****")
    datos = []
    for prop in name_props:
        dato = input(f"Ingresa tu {prop}:")
        datos.append(dato)
    miUsuario.registrar(datos[0], datos[1], datos[2], datos[3], datos[4])
    resp = validar_repetido(miUsuario.CURP)
    if not resp:
        lista_usuarios.append(miUsuario)
        miUsuario.__set_user = ""
        miUsuario.__set_password = ""
        miUsuario.__set_name = ""
        miUsuario.__set_curp = ""
        miUsuario.__set_city = ""
    else: print("El usuario ya existe")

def iniciar_sesion():
    credenciales_validas:bool = False
    print("**** Inicio de sesión ****")
    curp = input("CURP: ")
    password = input("Contraseña: ")
    
    for usuario in lista_usuarios:
        if usuario.CURP == curp and usuario.password == password:
            os.system("cls")
            credenciales_validas = True
            print("**** Información ****")
            print(f"Usuario: {usuario.user}")
            print(f"Nombre: {usuario.name}")
            print(f"CURP: {usuario.CURP}")
            print(f"Rol: {usuario.rol}")
            print(f"Ciudad: {usuario.city}\n\n")
            break
    if not credenciales_validas:
        os.system("cls")
        print("Datos Incorrectos\n\n")
        
opcion_elegida = {
    1: registrar_usuario,
    2: iniciar_sesion,
    3: sys.exit
}

def mostrar_menu():
    print("**** Menú ****")
    print("Elige una opción")
    print("1 - Registro:")
    print("2 - Inicio de sesión")
    print("3 - Salir")
    
def capturar_opcion() -> int:
    op = input("Opción elegida:")
    return int(op)

def elegir_opcion(op):
    exe = opcion_elegida[op]
    os.system("cls")
    exe()
    
def validar_repetido(curp:str) -> bool:
    existe:bool = False
    for usuario in lista_usuarios:
        if usuario.CURP.lower() == curp.lower():
            existe = True
            break
    return existe
    
def main():
    while True:
        mostrar_menu()
        op = capturar_opcion()
        elegir_opcion(op)

main()



    
    