# 8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la 
# información de todos los usuarios registrados al momento.  

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
    mi_usuario_nuevo = user()
    mi_usuario_nuevo.registrar(datos[0], datos[1], datos[2], datos[3], datos[4])
    resp = validar_repetido(mi_usuario_nuevo.CURP)
    if not resp:
        lista_usuarios.append(mi_usuario_nuevo)
        mi_usuario_nuevo.__set_user = ""
        mi_usuario_nuevo.__set_password = ""
        mi_usuario_nuevo.__set_name = ""
        mi_usuario_nuevo.__set_curp = ""
        mi_usuario_nuevo.__set_city = ""
    else: print("El usuario ya existe")

def iniciar_sesion():
    credenciales_validas:bool = False
    es_admin:bool = False
    
    print("**** Inicio de sesión ****")
    curp = input("CURP: ")
    password = input("Contraseña: ")
    
    for usuario in lista_usuarios:
        if usuario.CURP.lower() == curp.lower() and usuario.password == password: 
            if usuario.rol == "Administrador":
                es_admin = True
                credenciales_validas = True
                break
            else:
                os.system("cls")
                credenciales_validas = True
                es_admin = False
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
    elif es_admin:
        os.system("cls")
        print("**** Lista usuarios ****\n")
        for usuario in lista_usuarios:
            print(f"Usuario: {usuario.user}")
            print(f"Nombre: {usuario.name}")
            print(f"CURP: {usuario.CURP}")
            print(f"Rol: {usuario.rol}")
            print(f"Ciudad: {usuario.city}\n\n")
                    
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

def usuario_admin():
    datos = ["admin", "admin*", "Alfonso", "ABCDEFG12345", "Nuevo Laredo","Administrador"]
    miUsuario.registrar(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
    lista_usuarios.append(miUsuario)
    
def main():
    usuario_admin()
    while True:
        mostrar_menu()
        op = capturar_opcion()
        elegir_opcion(op)

main()



    
    