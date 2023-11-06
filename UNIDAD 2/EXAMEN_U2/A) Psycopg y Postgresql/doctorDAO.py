from doctor import Doctor
from conexion import conexion
from cursorDelPool import CursorDelPool
from logger_base import log

class DoctorDao:

    #Se declara un atributo por cada query a utilizar
    _SELECCIONAR = 'SELECT * FROM doctor ORDER BY id'
    _INSERTAR = 'INSERT INTO doctor(id,nombre,numerotelefono) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE doctor SET nombre=%s WHERE id =%s'
    _ELIMINAR = 'DELETE FROM doctor WHERE id =%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            doctores=[]
            for r in registros:
                doctores.append(Doctor(r[0],r[1],r[2]))
            return doctores 
        
    @classmethod
    def insertar(cls,doctor):
        with CursorDelPool() as cursor:
            valores=(doctor.idDoctor,doctor.nombreDoctor,doctor.telefonoDoctor)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,doctor):
        with CursorDelPool() as cursor:
            valores=(doctor.nombreDoctor,doctor.idDoctor)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,doctor):
        with CursorDelPool() as cursor:
            valores=(doctor.idDoctor,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount