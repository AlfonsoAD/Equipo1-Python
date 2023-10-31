from logger_base import log
from conecction import Conecction

class Cursor_of_the_pool:
    def __init__(self) -> None:
        self.__conexion = None
        self.__cursor = None
        
    def __enter__(self):
        log.debug("START OF BLOCK WITH")
        self.__conexion = Conecction.obtain_connection()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor
    
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug("EXIT IS EXECUTED")
        if valor_excepcion:
            self.__conexion.rollback()
        else:
            self.__conexion.commit()
        self.__cursor.close()
        Conecction.release_connection(self.__conexion)
    
if __name__ == "__main__":
    with Cursor_of_the_pool() as cursor:
        log.debug("BLOQUE WITH")
        cursor.execute("SELECT * FROM employees")
        log.debug(cursor.fetchall())
        