from animal import Animal
from conexion import conexion
from cursorDelPool import CursorDelPool
from logger_base import log

class AnimalDao:

    #Se declara un atributo por cada query a utilizar
    _SELECCIONAR = 'SELECT * FROM animal ORDER BY id'
    _INSERTAR = 'INSERT INTO animal(id,raza,fechaingreso,fechasalida) VALUES(%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE animal SET raza=%s WHERE id =%s'
    _ELIMINAR = 'DELETE FROM animal WHERE id =%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            animales=[]
            for r in registros:
                animales.append(Animal(r[0],r[1],r[2],r[3]))
            return animales 
        
    @classmethod
    def insertar(cls,animal):
        with CursorDelPool() as cursor:
            valores=(animal.idAnimal,animal.razaAnimal,animal.ingresoAnimal,animal.salidaAnimal)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,animal):
        with CursorDelPool() as cursor:
            valores=(animal.razaAnimal,animal.idAnimal)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,animal):
        with CursorDelPool() as cursor:
            valores=(animal.idAnimal,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__=="__main__":
    #animal1 = Animal(id="1",raza="putbull",fechaingreso="2023-05-31",fechasalida="2023-06-01")
    #Inserccion=AnimalDao.insertar(animal1)
    #log.debug(f"Animal agregadas {Inserccion}")

    #animal2 = Animal(id="1",raza="chihuahua")
    #Inserccion=AnimalDao.actualizar(animal2)
    #log.debug(f"ACTUALIZACION EN  {Inserccion}")

    animal3 = Animal(id="1")
    Inserccion=AnimalDao.eliminar(animal3)
    log.debug(f"ANIMAL ELIMINADO EN  {Inserccion}")
