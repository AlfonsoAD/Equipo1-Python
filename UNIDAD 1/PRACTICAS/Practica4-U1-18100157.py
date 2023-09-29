'''
#4 Entrada de datos y estructuración. 
Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture 
las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato 
“{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre y una LISTA de 
todas las materias
'''
import os

matricula = {}
materia = ''
listaMaterias = []
creditos = 0
opcion = 1

while opcion == 1:
    materia = input('Ingrese el nombre de la materia: ')
    creditos = int(input('Con cuantos creditos cuenta la materia?: '))
    matricula[materia] = creditos
    opcion = int(input('Falta una materia por agregar?\nINGRESE UN NUMERO\n1.-SI\n2.-NO\n'))
    os.system('cls')

creditos = 0

for i in matricula:
    creditos = creditos + matricula.get(i)
    listaMaterias.append(i)
    print(f'La asignatura {i} tiene {matricula.get(i)} créditos')

print('El total de creditos es: ',creditos)
print(listaMaterias)