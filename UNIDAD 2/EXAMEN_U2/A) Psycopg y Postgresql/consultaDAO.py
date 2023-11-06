from consulta import Consulta
from conexion import conexion
from cursorDelPool import CursorDelPool
from logger_base import log

class consultaDao:

    #Se declara un atributo por cada query a utilizar
    _SELECCIONAR = 'SELECT * FROM consulta ORDER BY id'
    _INSERTAR = 'INSERT INTO consulta(id,id_animal,id_doctor,servicio,cost) VALUES(%s,%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE consulta SET nombre=%s WHERE id =%s'
    _ELIMINAR = 'DELETE FROM consulta WHERE id =%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            consultas=[]
            for r in registros:
                consultas.append(Consulta(r[0],r[1],r[2],r[3],r[4]))
            return consultas 
        
    @classmethod
    def insertar(cls,consulta):
        with CursorDelPool() as cursor:
            valores=(consulta.idConsulta,consulta.idAnimal,consulta.idDoctor,consulta.servicioCon,consulta.costoCon)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,consulta):
        with CursorDelPool() as cursor:
            valores=(consulta.servicioCon,consulta.idConsulta)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,consulta):
        with CursorDelPool() as cursor:
            valores=(consulta.idConsulta,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount