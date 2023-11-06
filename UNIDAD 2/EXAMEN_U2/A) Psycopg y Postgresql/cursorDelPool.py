from logger_base import log
from conexion import conexion

class CursorDelPool:
    def __init__(self) -> None:
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        log.debug("Inicio bloque with")
        self.__conexion = conexion.ObtenerConexion()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor
    
    def __exit__(self,tipo_excepcion,valor_excepcion,detalle_excepcion):
        log.debug("Se ejecuta exit")
        if valor_excepcion: 
            self.__conexion.rollback()
        else: 
            self.__conexion.commit()
        self.__cursor.close()
        conexion.LiberarConexion(self.__conexion)

if __name__=="__main__":
    with CursorDelPool() as cursor:
        log.debug("Bloque With")
        cursor.execute("SELECT * FROM usuarios")
        log.debug(cursor.fetchall())
